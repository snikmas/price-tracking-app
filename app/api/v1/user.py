# file for writing routes that related to user. connects only with service, no business logic. routes
from fastapi import APIRouter, Path, HTTPException
from models.user import User, UserNotifications
from services import user_service

from typing import Annotated

router = APIRouter()

# admin route
@router.get('/')
def get_all_users() -> list[User]:
    result = user_service.get_all_users()
    if result == None: # do we actually have to send error?
        raise HTTPException(status_code=404, detail="No result")
    return {"users": result}

    pass

@router.get("/{id}")
def get_user(*, id: Annotated[bytes, Path(title="the user's id")]) -> User:
    result = user_service.get_user(id)
    if result == None: 
        raise HTTPException(status_code=404, detail="The user not found")
    return {"user": result}

@router.get("/{id}/settings_notifications")
def get_settings_notifications(*, id: bytes):
    pass

@router.post("/create")
def create_user(*, user: Annotated[User, Path(title="the user data")]) -> dict:
    result = user_service.create_user(user_data=user)
    if result:
        return {"result": "success"}

@router.delete("/{user_id}/delete")
def delete_user(*, user_id: Annotated[str, Path(title="the user's id")]) -> dict:
    result = user_service.delete_user(user_id=user_id)
    if result:
        return {"result": "success"}

# later can add orders with friends; queries; annotated metadata etc
@router.get("/{id}/friends")
def get_user_friends(*, id: bytes) -> list[User]:
    pass

