from pydantic import BaseModel, Field
from ..domain.enums import ProductCategory
from datetime import datetime

class Product(BaseModel):
    id: str
    image: str
    title: str 
    description: str 
    source_url: str
    product_category: ProductCategory
    tags: list[str]
    current_price: int

    created_at: datetime = Field(default_factory=datetime.now)
    
class ProductCreate(BaseModel):
    image: str | None = None
    title: str
    description: str | None = None
    source_url: str
    product_category: ProductCategory
    tags: list[str] = []
    current_price: int
    
