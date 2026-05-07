from fastapi import FastAPI
from app.core.logging import setup_logging
import app.core as core
from app.api.v1 import user, collection, product
from app.db.session import init_db
import logging
from contextlib import asynccontextmanager

setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    logging.info("init db")
    yield

app = FastAPI(
    title=core.config.config.app_name,
    lifespan=lifespan
    )

# register router
app.include_router(user.router, prefix='/users')
app.include_router(collection.router, prefix='/collections')
app.include_router(product.router, prefix='/products')
