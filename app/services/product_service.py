from ..models.product import Product
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

# crud for product
async def get_product(session: AsyncSession, product_id: str):
    
    task = select(Product).where(Product.id == product_id)
    
    result = await session.execute(task)
    return result.scalars().first() #im not sure how the result looks like 

async def get_all_products(session: AsyncSession):
    task = select(Product)
    result = await session.execute(task)
    return result.scalars().all()

async def create_product(session: AsyncSession, product_data: Product):
    
    new_product = Product(**product_data.model_dump())
    
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)
    return new_product

async def delete_product(session: AsyncSession, product_id: str):
    db_product = await session.get(Product, product_id)  # its better to call a funciton that you call yourself or fo like that?
    if not db_product: return None

    await session.delete(db_product)
    await session.commit()
    return True

async def update_product(session: AsyncSession, new_product: Product, product_id: str):
    # fetch a thing -> put a new one
    db_product = await session.get(Product, product_id)
    if not db_product: return None

    for key, value in new_product.model_dump().items(): # why no color?
        setattr(db_product, key, value)
    await session.commit()
    await session.refresh(db_product)
    
    return db_product
