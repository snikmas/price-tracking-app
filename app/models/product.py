from sqlalchemy import ForeignKey, String, MetaData, Table, Column, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from ..domain.enums import Gender, Country, Currency, ProductCategory

metadata_obj = MetaData() # this thing registers all tables things

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[str] = mapped_column(primary_key=True)
    image: Mapped[str] = mapped_column(String(200))
    title: Mapped[str] = mapped_column(String[50], nullable=False)    
    description: Mapped[str] = mapped_column(String(100))
    source_url: Mapped[str] = mapped_column(String(100))
    product_category: Mapped[ProductCategory] = mapped_column(ProductCategory, nullable=False)
    tags: Mapped[list[str]] = mapped_column(list[str]) # is it okay?
    current_price: Mapped[int] = mapped_column(int)
    
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"""<Product: {id}
        Title: {self.title}
        Description: {self.description}
        Category: {self.product_category}
        Current price: {self.current_price}
        Image: {self.image}
        Source_url: {self.source_url}
        Tags: {self.tags}
        Created at: {self.created_at}"""
    
