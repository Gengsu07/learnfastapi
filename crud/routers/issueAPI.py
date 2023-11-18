from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import update
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Issue
from ..schemas import IssueBase, IssueIn

router = APIRouter()


@router.get("/issues", status_code=200, response_model=List[IssueBase])
async def get_issues(db: Session = Depends(get_db)):
    stmt = db.query(Issue).all()
    return [IssueBase.from_orm(x) for x in stmt]


@router.get("/issue/{issueid}", status_code=200, response_model=IssueBase)
async def get_issue(issueid: int, db: Session = Depends(get_db)):
    stmt = db.query(Issue).filter(Issue.id == issueid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"Issue with id:{issueid} is not available"
        )
    return IssueBase.from_orm(stmt)


@router.post("/issue", status_code=201, response_model=IssueBase)
async def create_issue(issue: IssueIn, db: Session = Depends(get_db)):
    newissue = Issue(title=issue.title, description=issue.description)

    db.add(newissue)
    db.commit()

    db.refresh(newissue)
    return newissue


@router.delete("/issue/{issueid}", status_code=204)
async def del_issue(issueid: int, db: Session = Depends(get_db)):
    stmt = db.query(Issue).filter(Issue.id == issueid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"Issue with id:{issueid} is not available"
        )
    db.query(Issue).filter(Issue.id == issueid).delete(synchronize_session=False)
    # del_stmt = delete(Issue).where(Issue.id == issueid)
    # db.execute(del_stmt)
    db.commit()
    return {"Detail": f"Data with id:{issueid} has been deleted"}


@router.put("/issue/{issueid}", status_code=202)
async def update_issue(issueid: int, request: IssueIn, db: Session = Depends(get_db)):
    stmt = db.query(Issue).filter(Issue.id == issueid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"Issue with id:{issueid} is not available"
        )
    stmt_update = (
        update(Issue)
        .where(Issue.id == issueid)
        .values(title=request.title, description=request.description)
    )
    db.execute(stmt_update)
    db.commit()
    return "updated"
