from pydantic import BaseModel
import fastapi

class CollectionProducts(BaseModel):
    product_id: bytes
    collection_id: bytes

    created_at: str