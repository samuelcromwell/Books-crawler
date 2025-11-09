from motor.motor_asyncio import AsyncIOMotorClient
from utils.config import settings

_client: AsyncIOMotorClient | None = None
_db = None

async def init_mongo():
    global _client, _db
    if _client is None:
        _client = AsyncIOMotorClient(settings.MONGO_URI)  
        _db = _client[settings.MONGO_DB]
    return _db

async def close_mongo():
    global _client
    if _client:
        _client.close()
        _client = None
