from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

LocalSession = Session

DATABASE_URL = "sqlite:///./dev.db"
engine = create_engine(
    DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)


class Base(DeclarativeBase):
    pass
