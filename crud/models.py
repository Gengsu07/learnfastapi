from datetime import datetime

from sqlalchemy import Column, Date, Integer, String, Text

from .database import Base


class Issue(Base):
    __tablename__ = "issue"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    createdAt = Column(Date, default=datetime.now())
