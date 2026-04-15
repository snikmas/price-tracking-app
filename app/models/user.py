from typing import List, Optional
from sqlalchemy import ForeignKey, String, MetaData, Table, Column, LargeBinary, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from ..domain.enums import Gender, Country, Currency


metadata_obj = MetaData()

users = Table(
    "users", 
    metadata_obj,
    Column("id", String(50), primary_key=True),
    Column("nickname", String(50), unique=True, nullable=False),
    Column("full_name", String(100)),
    Column("password", String(255), nullable=False),
    Column("gender", Gender, default=None),
    Column("country", Country, default=None),
    Column("email", String(100), default=None, nullable=False),
    Column("phone", String(30), default=None, nullable=False),
    Column("currency", Currency, default=Currency.USD),

    Column("created_at", DateTime, server_default=func.now())
)

user_notifications = Table(
    "user_notifications",
    metadata_obj,
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("email_notifications", bool, default=True),
    Column("phone_notifications", bool, default=True),
    Column("notify_if_higher_price", bool, default=True),
    Column("notify_if_lower_price", bool, default=True),

    Column("created_at", DateTime, server_default=func.now())
)


# base calss - used for dec
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[bytes]