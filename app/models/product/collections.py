import fastapi
from pydantic import BaseModel

class Collection(BaseModel):
    
    id: bytes
    title: str
    description: str

    author_id: bytes
    created_at: str