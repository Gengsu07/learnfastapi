from database.database import Base
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String, Text


class CommentBase(BaseModel):
    title: str
    text: str


class UserBase(BaseModel):
    username: str
    email: str


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    comment = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
