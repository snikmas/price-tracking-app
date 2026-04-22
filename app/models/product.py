from pydantic import BaseModel, Field
from ..domain.enums import ProductCategory
from datetime import datetime

class Product:
    id: str
    image: str
    title: str 
    description: str 
    source_url: str
    product_category: ProductCategory
    tags: list[str]
    current_price: int

    created_at: datetime = Field(default_factory=datetime.now)
    
