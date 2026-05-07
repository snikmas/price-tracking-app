from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.schemas.user import User, UserNotifications
from sqlalchemy.exc import IntegrityError
import app.exceptions.user as user_exceptions

async def get_user(session: AsyncSession, user_id: str) -> User:
    task = select(User).where(User.id == user_id)
    result = await session.execute(task)

    return result.scalars().first()

async def get_all_users(session: AsyncSession) -> list[User]:
    task = select(User) # select its table
    result = await session.execute(task)
    return result.scalars().all()

async def create_user(session: AsyncSession, user_data: User) -> User:
    try:
        session.add(user_data)
        await session.commit()
        await session.refresh(user_data)
        return user_data
    except IntegrityError:
        await session.rollback()
        raise user_exceptions.UserAlreadyExist(nickname=user_data.nickname)
        

async def delete_user(session: AsyncSession, user_id: str) -> bool:
    db_user = await session.get(User, user_id)
    if not db_user:
        return False

    await session.delete(db_user)
    await session.commit()
    return True

async def update_user(session: AsyncSession, new_user_data: User, user_id: str) -> User | None:
    db_user = await session.get(User, user_id)
    if not db_user:
        return None

    for key, value in new_user_data.__dict__.items():
        if key.startswith("_") or key in {"id", "created_at", "notifications"}:
            continue
        setattr(db_user, key, value)

    await session.commit()
    await session.refresh(db_user)
    return db_user


async def get_user_notifications(session: AsyncSession, user_id: str) -> UserNotifications | None:
    task = select(UserNotifications).where(UserNotifications.user_id == user_id)
    result = await session.execute(task)
    return result.scalars().first()
