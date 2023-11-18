from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..repository.issue import (
    createIssue,
    deleteIssue,
    getIssue,
    getIssues,
    updateIssue,
)
from ..schemas import IssueBase, IssueIn

router = APIRouter(tags=["Issue"], prefix="/issue")


@router.get("/", status_code=200, response_model=List[IssueBase])
async def get_issues(db: Session = Depends(get_db)):
    return getIssues(db)


@router.get("/{issueid}", status_code=200, response_model=IssueBase)
async def get_issue(issueid: int, db: Session = Depends(get_db)):
    return getIssue(issueid, db)


@router.post("/", status_code=201, response_model=IssueBase)
async def create_issue(issue: IssueIn, db: Session = Depends(get_db)):
    return createIssue(issue, db)


@router.delete("/{issueid}", status_code=204)
async def del_issue(issueid: int, db: Session = Depends(get_db)):
    deleteIssue(issueid, db)


@router.put("/{issueid}", status_code=202)
async def update_issue(issueid: int, request: IssueIn, db: Session = Depends(get_db)):
    return updateIssue(issueid, db)
