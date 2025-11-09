from fastapi import Depends, HTTPException, Header
from db.mongo import init_mongo
from utils.config import settings

async def get_db():
    return await init_mongo()

async def api_key_auth(x_api_key: str = Header(..., alias="X-API-Key")):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return True

def pagination_params(page: int = 1, page_size: int = 20):
    page = max(1, page); page_size = min(max(1, page_size), 100)
    skip = (page-1)*page_size
    return {"skip": skip, "limit": page_size}
