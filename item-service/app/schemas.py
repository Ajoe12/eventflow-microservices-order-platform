from pydantic import BaseModel
from typing import Optional

class CreateItem(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class UpdateItem(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None


class ItemResponse(BaseModel):
    id: str
    name: str
    description: str
    price: float
    quantity: int