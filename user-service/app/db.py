from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import User
from app.core.config import MONGO_URI

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)

    db = client.get_database("eventflow")   # ✅ safest way

    await init_beanie(
        database=db,
        document_models=[User]
    )