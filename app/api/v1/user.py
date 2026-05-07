from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.schemas.user import User, UserNotifications
from app.db.session import get_db
from app.services import user_service

from app.models.user import UserCreate
from app.core.logging import logging

import app.exceptions.user as user_exceptions

router = APIRouter()

@router.get('/')
async def get_all_users(
    session: AsyncSession = Depends(get_db),
) -> dict[str, list[dict]]:
    result = await user_service.get_all_users(session)
    return {"users": jsonable_encoder(result)}

@router.get("/{id}")
async def get_user(
    *,
    id: Annotated[str, Path(title="the user's id")],
    session: AsyncSession = Depends(get_db),
) -> dict[str, dict]:
    result = await user_service.get_user(session, id)
    if result is None:
        raise HTTPException(status_code=404, detail="The user not found")
    return {"user": jsonable_encoder(result)}

@router.get("/{id}/settings_notifications")
async def get_settings_notifications(
    *,
    id: Annotated[str, Path(title="the user's id")],
    session: AsyncSession = Depends(get_db),
) -> dict[str, dict]:
    result = await user_service.get_user_notifications(session, id)
    if result is None:
        raise HTTPException(status_code=404, detail="The user settings not found")
    return {"settings_notifications": jsonable_encoder(result)}

@router.post("/create")
async def create_user(
    *,
    user_data: Annotated[UserCreate, Body(title="the user data")],
    session: AsyncSession = Depends(get_db),
) -> dict[str, dict]:
    # check if its exist
    user = User(**user_data.model_dump())
    existing_user = await user_service.get_user(session=session, user_id=user.id)
    if existing_user is not None:
        raise HTTPException(
            status_code=409,
            detail='Nickname already exists'
        )
    
    logging.info(f"\n\n\n\nT HE USER IS EXISTS: {existing_user} its a none")
    try:
        result = await user_service.create_user(session, user)
        return {"user": jsonable_encoder(result)}
    except user_exceptions.UserAlreadyExist:
        raise HTTPException(409, "User already exists!")

@router.delete("/{user_id}/delete")
async def delete_user(
    *,
    user_id: Annotated[str, Path(title="the user's id")],
    session: AsyncSession = Depends(get_db),
) -> dict[str, str]:
    result = await user_service.delete_user(session, user_id=user_id)
    if not result:
        raise HTTPException(status_code=404, detail="The user not found")
    return {"result": "success"}

@router.get("/{id}/friends")
async def get_user_friends(
    *,
    id: Annotated[str, Path(title="the user's id")],
) -> dict[str, str]:
    return {"result": f"Friends for user {id} are not implemented yet"}
