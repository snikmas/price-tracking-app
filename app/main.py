from fastapi import FastAPI
from core import logging, config
from api.v1 import user, collection, product

logging.setup_logging()
app = FastAPI(title=config.config.app_name)

# register router
app.include_router(user.router, prefix='/users')
app.include_router(collection.router, prefix='/collections')
app.include_router(product.router, prefix='/products')
