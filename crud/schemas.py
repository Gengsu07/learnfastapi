from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class IssueIn(BaseModel):
    title: str
    description: str


class IssueBase(IssueIn):
    id: int
    createdAt: Optional[datetime]

    class Config:
        orm_mode = True
