from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from .database import Base


class Issue(Base):
    __tablename__ = "issue"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    createdAt = Column(DateTime, default=datetime.now())
