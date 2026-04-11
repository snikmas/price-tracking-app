import fastapi 
from pydantic import BaseModel

class Product(BaseModel):
    id: bytes
    title: str
    description: str

    category: str
    subcategory: str | None
    url: str

    current_price: float
    history_price: list[float] = []

    created_at: str