from sqlalchemy import create_engine, text
from ..core.config import config 

# allows run in 1+ threads
engine = create_engine(config.db_url, echo=True, connect_args={"check_same_thread": True})
# the prupose of engine - get a session object


# not here
# with engine.connect() as conn:
    # result = conn.execute(text("hi"))