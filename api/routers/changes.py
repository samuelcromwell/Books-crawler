# api/routers/changes.py
from fastapi import APIRouter, Depends, Request
from api.deps import get_db, api_key_auth
from api.rate_limit import limiter

router = APIRouter(prefix="/changes", tags=["changes"])

@router.get("", dependencies=[Depends(api_key_auth)])
@limiter.limit("100/hour")
async def get_changes(request: Request, db=Depends(get_db), limit: int = 100):  # ✅ request added
    cur = db.changes.find({}).sort([("ts", -1)]).limit(min(limit, 500))
    return [c async for c in cur]
