from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from ..core.config import config
from .schemas.product import Product
from .schemas.user import Base, User, UserNotifications

async_db_url = config.db_url.replace("sqlite:///", "sqlite+aiosqlite:///")

engine = create_async_engine(
    async_db_url,
    echo=True,
    connect_args={"check_same_thread": False},
)

# a session buidler, not a session itself
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False, # prevents data from being cleared after commit, musthave for async (by default it clears everything, yes)
    autoflush=False, # flush - Sends your changes to the database temporarily (before commit); we falsed it -> more predictable behavior
)


async def get_db(): # with this context manager, it automatically: 1) creates a new sessino when you need it 2) closes when you're done 3) handles error/rollbacks safely
    async with AsyncSessionLocal() as session:
        yield session


async def init_db() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
