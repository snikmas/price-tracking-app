from sqlalchemy import ForeignKey, String, MetaData, Table, Column, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from ..domain.enums import Gender, Country, Currency, ProductCategory


metadata_obj = MetaData() # this thing registers all tables things

product = Table(
    "product",
    metadata_obj,
    Column("id", String(50), primary_key=True),
    Column("image", String(100)),
    Column("title", String(50), unique=True, nullable=False),
    Column("description", String(100)),
    Column("source_url", String(100)), # or url? for tracking?
    Column("product_category", ProductCategory, nullable=False), 
    Column("tags", String(100)),
    Column("current_price", int),
    
    
    Column("created_at", DateTime, server_default=func.now())
)

# color? do we need it? or create different classes? can add later. inheritance tihng

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'products'

    id: Mapped[bytes]