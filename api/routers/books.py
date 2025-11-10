from typing import Literal
from fastapi import APIRouter, Depends, Query, HTTPException, Request
from bson import ObjectId
from datetime import datetime
from api.deps import get_db, api_key_auth
from api.rate_limit import limiter
from utils.config import settings

router = APIRouter(prefix="/books", tags=["books"])

def _to_jsonable(obj):
    """Recursively convert Mongo types; map _id -> id."""
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, (datetime,)):
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
    request: Request,   # required by slowapi
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    rating: int | None = Query(None, ge=1, le=5),
    sort_by: Literal["rating","price","reviews"] | None = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db=Depends(get_db),
):
    # base filter
    q: dict = {}
    if category:
        q["category"] = category
    if rating is not None:
        q["rating"] = rating

    # Decide if we need aggregation (numeric price filter/sort)
    use_pipeline = (min_price is not None) or (max_price is not None) or (sort_by == "price")

    if use_pipeline:
        # Build robust _price_num:
        # - If already number, use as-is
        # - Else, strip "£" and commas, then convert to double
        pipeline = [
            {
                "$addFields": {
                    "_price_num": {
                        "$cond": [
                            {"$isNumber": "$price_incl_tax"},
                            "$price_incl_tax",
                            {
                                "$convert": {
                                    "input": {
                                        "$replaceAll": {
                                            "input": {
                                                "$replaceAll": {
                                                    "input": {
                                                        "$ifNull": ["$price_incl_tax", ""]
                                                    },
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
                        ]
                    }
                }
            },
            {"$match": q} if q else {"$match": {}},
        ]

        price_match = {}
        if min_price is not None:
            price_match["$gte"] = float(min_price)
        if max_price is not None:
            price_match["$lte"] = float(max_price)
        if price_match:
            pipeline.append({"$match": {"_price_num": price_match}})

        # Sorting: if price sort requested, sort on computed numeric field, else default by name
        sort_stage = {"$sort": {"_price_num": 1, "name": 1}} if sort_by == "price" else {"$sort": {"name": 1}}

        pipeline.extend([
            {
                "$facet": {
                    "items": [
                        sort_stage,
                        {"$skip": (page - 1) * page_size},
                        {"$limit": page_size},
                        # Exclude raw HTML & helper
                        {"$project": {"_raw_html": 0, "raw_html": 0, "_price_num": 0}},
                    ],
                    "meta": [{"$count": "total"}],
                }
            }
        ])

        agg = db.books.aggregate(pipeline)
        result = [doc async for doc in agg]
        bucket = result[0] if result else {}
        items = bucket.get("items", [])
        meta = bucket.get("meta", [])
        total = (meta[0]["total"] if meta else 0)
        pages = (total + page_size - 1) // page_size

        return {
            "page": page,
            "page_size": page_size,
            "pages": pages,
            "total": total,
            "items": [_to_jsonable(it) for it in items],
        }

    # Simple path (no numeric price required)
    # Sort directions: rating ↓, reviews ↓; fallback by name ↑
    sort_spec = None
    if sort_by == "rating":
        sort_spec = [("rating", -1), ("name", 1)]
    elif sort_by == "reviews":
        # Standardize the field name used in storage; choose "reviews"
        sort_spec = [("reviews", -1), ("name", 1)]

    total = await db.books.count_documents(q)
    pages = (total + page_size - 1) // page_size

    proj = {"_raw_html": 0, "raw_html": 0}  # exclude snapshots if either naming exists
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
