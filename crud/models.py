from sqlalchemy import Column, Integer, String

from .database import Base


class Issue(Base):
    __tablename__ = "issue"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
