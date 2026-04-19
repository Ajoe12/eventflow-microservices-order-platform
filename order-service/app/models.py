from beanie import Document
from datetime import datetime
from typing import List


class Order(Document):
    user_id: str
    items: List[dict]   # [{item_id, quantity}]
    total_price: float
    status: str = "PENDING"
    created_at: datetime = datetime.utcnow()

    class Settings:
        name = "orders"