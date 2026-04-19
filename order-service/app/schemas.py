from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    item_id: str
    quantity: int


class CreateOrder(BaseModel):
    items: List[OrderItem]


class UpdateOrderStatus(BaseModel):
    status: str