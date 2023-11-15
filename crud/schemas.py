from datetime import datetime

from pydantic import BaseModel


class IssueIn(BaseModel):
    title: str
    description: str


class IssueBase(IssueIn):
    id: int
    createdAt: datetime

    class Config:
        orm = True
