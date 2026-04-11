# schema for request/response contracts
import fastapi
from pydantic import BaseModel 
from ...domain import * 

class User(BaseModel):
    
    user_id: bytes

    nickname: str
    full_name: str
    password: str 

    gender: enums.Gender | None
    country: enums.Country | None
    
    email: str | None = None
    phone: str | None = None
    currency: enums.Currency | None

    created_at: str 
    

