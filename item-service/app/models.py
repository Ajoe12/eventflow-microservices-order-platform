from beanie import Document
from datetime import datetime

class Item(Document):
    name: str
    description: str
    price: float
    quantity: int
    created_at: datetime = datetime.utcnow()

    class Settings:
        name = "items"