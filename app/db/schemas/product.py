from datetime import datetime

from sqlalchemy import DateTime, Enum as SqlEnum, Integer, JSON, String, func
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4
from ...domain.enums import ProductCategory
from .user import Base
from app.core.logging import logging


class Product(Base):
    __tablename__ = "products"
    id: Mapped[str] = mapped_column(default=lambda: str(uuid4()), primary_key=True)
    image: Mapped[str] = mapped_column(String(200), nullable=False)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(300), nullable=False)
    source_url: Mapped[str] = mapped_column(String(300), nullable=False)
    product_category: Mapped[ProductCategory] = mapped_column(
        SqlEnum(ProductCategory), default=ProductCategory.T_SHIRTS
    )
    tags: Mapped[list[str]] = mapped_column(JSON, default=list)
    current_price: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    def __repr__(self) -> str:
        return f"<Product id={self.id!r} title={self.title!r}>"
