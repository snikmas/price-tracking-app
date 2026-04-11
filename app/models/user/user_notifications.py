import fastapi
from pydantic import BaseModel


class UserNotifications(BaseModel):
    
    user_id: bytes
    email_notifications: bool = True
    phone_notifications: bool = True
    notify_if_higher_price: bool = True
    notify_if_lower_price: bool = True

    created_at: str