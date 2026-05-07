from fastapi import FastAPI
from app.core import logging, config
from app.api.v1 import user, collection, product
from app.db.session import init_db

logging.setup_logging()
app = FastAPI(title=config.config.app_name)
init_db()

# register router
app.include_router(user.router, prefix='/users')
app.include_router(collection.router, prefix='/collections')
app.include_router(product.router, prefix='/products')
