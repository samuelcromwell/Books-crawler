from motor.motor_asyncio import AsyncIOMotorClient
from utils.config import settings

_client = None
db = None

async def init_mongo():
    global _client, db
    _client = AsyncIOMotorClient(settings.MONGO_URI)
    db = _client[settings.MONGO_DB]
    return db

async def close_mongo():
    _client and _client.close()
