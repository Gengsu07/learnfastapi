from pydantic import BaseModel


class IssueIn(BaseModel):
    title: str
    description: str


class IssueBase(IssueIn):
    id: int

    class Config:
        orm_mode = True
