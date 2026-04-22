from typing import List, Optional
from sqlalchemy import ForeignKey, String, MetaData, Table, Column, LargeBinary, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from ..domain.enums import Gender, Country, Currency


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(String(40), primary_key=True)
    nickname: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    full_name: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    gender: Mapped[Gender] = mapped_column(Gender, default=None)
    country: Mapped[Country] = mapped_column(Country, default=None)
    email: Mapped[str] = mapped_column(String(50), default=None)
    phone: Mapped[str] = mapped_column(String(30), default=None)
    currency: Mapped[Currency] = mapped_column(Currency, default=Currency.USB)
    
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"""
id: {self.id}
nickname: {self.nickname}
full_name: {self.full_name}
password: {self.password}
gender: {self.gender}
country: {self.country}
email: {self.email}
phone: {self.phone}
currency: {self.currency}

created_at: {self.created_at}
"""

class User_Notifications(Base):
    __table__ = 'user_notifications'

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    email_notifications: Mapped[bool] = mapped_column(default=True)
    phone_notifications: Mapped[bool] = mapped_column(default=True)
    notify_if_higher_price: Mapped[bool] = mapped_column(default=True)  
    notify_if_lower_price: Mapped[bool] = mapped_column(default=True)       

    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"""
user_id: {self.user_id}
email_notifications: {self.email_notifications}
phone_notifications: {self.phone_notifications}
notify_if_higher_price: {self.notify_if_higher_price}
notify_if_lower_price: {self.notify_if_lower_price}
created_at: {self.created_at}
"""
