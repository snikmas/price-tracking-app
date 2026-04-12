# file for writing routes that related to user. connects only with service, no business logic. routes
from fastapi import APIRouter, Path
from models import *

from typing import Annotated

router = APIRouter()

# admin route
@router.get()
def get_all_users() -> list[user.User]:
    pass

@router.get("/{id}")
def get_user(*, id: Annotated[bytes, Path(title="the user's id")]) -> user.User:
    pass

@router.get("/{id}/settings_notifications")
def get_settings_notifications(*, id: bytes):
    pass

# later can add orders with friends; queries; annotated metadata etc
@router.get("/{id}/friends")
def get_user_friends(*, id: bytes) -> list[user.User]:
    pass

