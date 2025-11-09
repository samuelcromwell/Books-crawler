# api/routers/books.py
from fastapi import APIRouter, Depends, Query, HTTPException, Request
from bson import ObjectId
from api.deps import get_db, api_key_auth
from api.rate_limit import limiter

router = APIRouter(prefix="/books", tags=["books"])

@router.get("", dependencies=[Depends(api_key_auth)])
@limiter.limit("100/hour")
async def list_books(
    request: Request,   # ✅ slowapi requires this
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    rating: int | None = Query(None, ge=1, le=5),
    sort_by: str | None = Query(None, pattern="^(rating|price|reviews)$"),
    page: int = 1, page_size: int = 20,
    db=Depends(get_db)
):
    q = {}
    if category: q["category"] = category
    if rating: q["rating"] = rating
    if min_price is not None or max_price is not None:
        q["price_incl_tax"] = {}
        if min_price is not None: q["price_incl_tax"]["$gte"] = min_price
        if max_price is not None: q["price_incl_tax"]["$lte"] = max_price

    sort = None
    if sort_by == "rating": sort = [("rating", -1)]
    elif sort_by == "price": sort = [("price_incl_tax", 1)]
    elif sort_by == "reviews": sort = [("num_reviews", -1)]

    page = max(1, page); page_size = min(max(1, page_size), 100)
    cursor = db.books.find(q).skip((page-1)*page_size).limit(page_size)
    if sort: cursor = cursor.sort(sort)
    items = [i async for i in cursor]
    total = await db.books.count_documents(q)
    return {"items": items, "total": total, "page": page, "page_size": page_size}

@router.get("/{book_id}", dependencies=[Depends(api_key_auth)])
@limiter.limit("100/hour")
async def get_book(book_id: str, request: Request, db=Depends(get_db)):  # ✅ request added
    try:
        _id = ObjectId(book_id)
    except Exception:
        raise HTTPException(400, "Invalid id")
    doc = await db.books.find_one({"_id": _id})
    if not doc:
        raise HTTPException(404, "Not found")
    return doc
