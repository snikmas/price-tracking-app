from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from ..core.config import config 

# allows run in 1+ threads
engine = create_async_engine(config.db_url, echo=True, connect_args={"check_same_thread": True})
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, bind=engine, autoflush=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

