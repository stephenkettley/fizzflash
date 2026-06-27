from app.db.session import Base, engine
from app.db import models


def init_db():
    """Creates all database tables based on SQLAlchemy models. Safe to run in development."""
    Base.metadata.create_all(bind=engine)
