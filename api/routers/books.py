from fastapi import APIRouter, Depends, Query, HTTPException, Request
from api.deps import get_db, api_key_auth
from api.rate_limit import limiter
from utils.config import settings
from bson import ObjectId
from datetime import datetime

router = APIRouter(prefix="/books", tags=["books"])

def _to_jsonable(obj):
    """Recursively convert Mongo types; map _id -> id."""
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, (datetime,)):  # FastAPI can encode datetime
        return obj
    if isinstance(obj, list):
        return [_to_jsonable(x) for x in obj]
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k == "_id":
                out["id"] = _to_jsonable(v)
            else:
                out[k] = _to_jsonable(v)
        return out
    return obj

@router.get("", dependencies=[Depends(api_key_auth)])
@limiter.limit(settings.RATE_LIMIT)
async def list_books(
    request: Request,   # slowapi needs this
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    rating: int | None = Query(None, ge=1, le=5),
    sort_by: str | None = Query(None, pattern="^(rating|price|reviews)$"),
    page: int = 1,
    page_size: int = 20,
    db=Depends(get_db),
):
    if page < 1 or page_size < 1 or page_size > 100:
        raise HTTPException(status_code=400, detail="Invalid pagination")

    # base filter
    q: dict = {}
    if category:
        q["category"] = category
    if rating:
        q["rating"] = rating

    # use aggregation if we need numeric price filter/sort
    use_pipeline = bool(min_price is not None or max_price is not None or sort_by == "price")
    if use_pipeline:
        pipeline = [
            {
                "$addFields": {
                    "_price_num": {
                        "$convert": {
                            "input": {
                                "$replaceAll": {
                                    "input": {
                                        "$replaceAll": {
                                            "input": {"$ifNull": ["$price_incl_tax", ""]},
                                            "find": "£",
                                            "replacement": ""
                                        }
                                    },
                                    "find": ",",
                                    "replacement": ""
                                }
                            },
                            "to": "double",
                            "onError": None,
                            "onNull": None,
                        }
                    }
                }
            },
            {"$match": q} if q else {"$match": {}},
        ]

        price_match = {}
        if min_price is not None:
            price_match["$gte"] = min_price
        if max_price is not None:
            price_match["$lte"] = max_price
        if price_match:
            pipeline.append({"$match": {"_price_num": price_match}})

        pipeline.extend([
            {
                "$facet": {
                    "items": [
                        {"$sort": {"_price_num": 1, "name": 1}},
                        {"$skip": (page - 1) * page_size},
                        {"$limit": page_size},
                        {"$project": {"raw_html": 0}},
                    ],
                    "meta": [{"$count": "total"}],
                }
            }
        ])

        agg = db.books.aggregate(pipeline)
        result = [doc async for doc in agg]
        items = result[0].get("items", []) if result else []
        meta = result[0].get("meta", []) if result else []
        total = (meta[0]["total"] if meta else 0)
        pages = (total + page_size - 1) // page_size
        return {
            "page": page,
            "page_size": page_size,
            "pages": pages,
            "total": total,
            "items": [_to_jsonable(it) for it in items],
        }

    # simple path (no numeric price needs)
    sort_spec = None
    if sort_by == "rating":
        sort_spec = [("rating", 1), ("name", 1)]
    elif sort_by == "reviews":
        sort_spec = [("num_reviews", 1), ("name", 1)]

    total = await db.books.count_documents(q)
    pages = (total + page_size - 1) // page_size
    proj = {"raw_html": 0}
    cursor = db.books.find(q, proj)
    if sort_spec:
        cursor = cursor.sort(sort_spec)
    cursor = cursor.skip((page - 1) * page_size).limit(page_size)

    items = [_to_jsonable(doc) async for doc in cursor]
    return {
        "page": page,
        "page_size": page_size,
        "pages": pages,
        "total": total,
        "items": items,
    }
