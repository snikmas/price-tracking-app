from pydantic import BaseModel, Field
from domain.enums import Gender, Country, Currency
from datetime import datetime

class User(BaseModel):
    id: str
    nickname: str
    full_name: str
    password: str #passwrod hash
    gender: Gender | None
    country: Country | None
    email: str | None
    phone: str | None
    currency: Currency = Currency.USD

    created_at: datetime = Field(default_factory=datetime.now)

class UserNotifications(BaseModel):
    user_id: str
    email_notifications: bool = True
    phone_notifications: bool = True
    notify_if_higher_price: bool = True
    notify_if_lower_price: bool = True

    created_at: datetime = Field(default_factory=datetime.now)