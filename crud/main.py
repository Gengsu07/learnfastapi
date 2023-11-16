from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from crud import models, schemas
from crud.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gengsu Tracker Issue")


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/issue", status_code=201, response_model=schemas.IssueBase)
async def create_issue(issue: schemas.IssueIn, db: Session = Depends(get_db)):
    newissue = models.Issue(title=issue.title, description=issue.description)

    db.add(newissue)
    db.commit()

    db.refresh(newissue)
    return newissue


# query using ORM Query Style (db.query(models.Issue))
@app.get("/issues", status_code=200, response_model=List[schemas.IssueBase])
async def get_issue(db: Session = Depends(get_db)):
    issues = db.query(models.Issue).all()
    return [schemas.IssueBase.from_orm(issue) for issue in issues]


# query using SQL Expression select() Style (select(models.Issue))
@app.get("/issue/{issueid}", status_code=200, response_model=schemas.IssueBase)
async def get_issue_byid(issueid: int, db: Session = Depends(get_db)):
    # stmt = select(models.Issue).where(models.Issue.id == issueid)
    stmt = db.query(models.Issue).filter(models.Issue.id == issueid).first()
    # issue = db.execute(stmt).scalars().first()
    # return schemas.IssueBase.from_orm(stmt)
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"Issue with id:{issueid} is not available"
        )
    return stmt


@app.delete("/issue/{issueid}", status_code=204)
async def del_issue(issueid: int, db: Session = Depends(get_db)):
    stmt = db.query(models.Issue).filter(models.Issue.id == issueid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"Issue with id:{issueid} is not available"
        )
    db.query(models.Issue).filter(models.Issue.id == issueid).delete(
        synchronize_session=False
    )
    # del_stmt = delete(models.Issue).where(models.Issue.id == issueid)
    # db.execute(del_stmt)
    return {"Detail": f"Data with id:{issueid} has been deleted"}
