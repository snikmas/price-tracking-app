from models.user import User, UserNotifications
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

async def get_user(session: AsyncSession, user_id: str) -> User:
    task = select(User).where(User.id == user_id)
    result = await session.execute(task)
    return result.scalars().first()

async def get_all_users(session: AsyncSession) -> list[User]:
    task = select(User)
    result = await session.execute(task)
    return result.scalars.all()

async def create_user(session: AsyncSession, user_data: User) -> User:
    new_user = User(**user_data.model_dump())

    session.add(new_user) # how to do.. that check if it was succesfull or not
    await session.commit()
    await session.refresh(new_user)
    return new_user

async def delete_user(session: AsyncSession, user_id: str) -> bool:
    db_user = await session.get(User, user_id)
    if not db_user: return None

    await session.delete(db_user)
    await session.commit()
    return True

async def update_user(session: AsyncSession, new_user: User, user_id: str):
    # 1. fetch a thing
    db_user = await session.get(User, user_id)
    if not db_user: return None

    for key, value in new_user.model_dump().items():
        setattr(db_user, key, value)

    await session.commit()
    await session.refresh(db_user)
    return db_user # its good to return an obj/ not just bool