from typing import Annotated

from fastapi import APIRouter, Body, Depends, Path, HTTPException
from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import ProductCreate, Product
from app.db.schemas.product import Product as Db_Product
from app.db.session import get_db
from app.services import product_service
from app.core.logging import logging

router = APIRouter()

SessionDbDep = Annotated[AsyncSession, Depends(get_db)]

# dont write user id here cuz it should be handled using another way
# price-track//collections #opens a deafult one? 
# price-track//collections/<custom_name>
# price-track//collections/<custom_name>/product_1
# price-track//collections/
# price-track//collections/<custom_name>
@router.get('/')
async def get_all_products(session: SessionDbDep) -> dict[str, list[dict]]:
    result = await product_service.get_all_products(session)
    return {"products": jsonable_encoder(result)}

@router.get('/{id}')
async def get_product(
    *,
    id: Annotated[str, Path(title="the product's id")],
    session: SessionDbDep
) -> dict[str, dict]:
    result = await product_service.get_product(session, product_id=id)
    if not result:
        raise HTTPException(status_code=404, detail="The product not found")
    return {"product": jsonable_encoder(result)}

@router.post("/create")
async def create_product(
    *,
    product_data: Annotated[ProductCreate, Body(title="the product data")],
    session: SessionDbDep
) -> dict[str, dict]:
    
    existing_product = await product_service.get_product(session=session, source_url=product_data.source_url)
    if existing_product:
        logging.info(f"EXISTING PRODUCT {existing_product}")
        raise HTTPException(
            detail="Product already exists",
            status_code=409
        )
    logging.info(f"EXISTING PRODUCT {existing_product}")
    product = Product(**product_data.model_dump())
     # dump: convert a pydantic model to a dictinary
     # ** convert to a keyword arguemtns(kwargs, "bla": "info")
     # Product(this dict) <- creates a new sqlachemy model 

#     Is equivalent to writing:
#     product = Product(
#     name=product_data.name,
#     price=product_data.price,
#     category=product_data.category)
    logging.info(f"INFO\n\n{product}\n\n")
    result = await product_service.create_product(session, product)
    return {"product": jsonable_encoder(result)}



@router.delete("/{id}/delete")
async def delete_product(
    *,
    product_id: Annotated[str, Path(title="the product's id")],
    session: SessionDbDep
) -> dict[str, str]:
    result = await product_service.delete_product(session, product_id=product_id)
    if not result:
        raise HTTPException(status_code=404, detail="The product not found")
    return {"result": "success"}

# full replacement
@router.put("/{product_id}/update")
async def update_product(
    *,
    product_id: Annotated[str, Path(title="the product's id")],
    new_product_data: Annotated[Product, Body(title="new product's data")],
    session: SessionDbDep
) -> dict[str, str]:
    result = await product_service.update_product(session, new_product=new_product_data, product_id=product_id)
    if not result:
        raise HTTPException(
            status_code=404,
            detail="The product not found"
        )
    return {"result": "success"} 
    