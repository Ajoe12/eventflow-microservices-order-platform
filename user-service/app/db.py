from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import User
from app.core.config import MONGO_URI

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(database = client.eventflow, document_models=[User])