from fastapi import FastAPI
from .core import *
from app.api.v1 import *

logging.setup_logging()
app = FastAPI(title=config.config.app_name)

# register router
app.include_router(user, pref='users')
app.include_router(collection, prefix='/collections')
app.include_router(product, prefix='/products')
