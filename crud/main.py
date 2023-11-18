from typing import List

from fastapi import Depends, FastAPI, HTTPException
from hashing import PassHash
from sqlalchemy import update
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
    db.commit()
    return {"Detail": f"Data with id:{issueid} has been deleted"}


@app.put("/issue/{issueid}", status_code=202)
async def update_issue(
    issueid: int, request: schemas.IssueIn, db: Session = Depends(get_db)
):
    stmt = db.query(models.Issue).filter(models.Issue.id == issueid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"Issue with id:{issueid} is not available"
        )
    stmt_update = (
        update(models.Issue)
        .where(models.Issue.id == issueid)
        .values(title=request.title, description=request.description)
    )
    db.execute(stmt_update)
    db.commit()
    return "updated"


@app.post("/user", status_code=201, response_model=schemas.UserBase)
async def create_user(request: schemas.UserIn, db: Session = Depends(get_db)):
    cekusername = (
        db.query(models.User).filter(models.User.username == request.username).first()
    )
    if cekusername:
        raise HTTPException(
            status_code=409,
            detail=f"User with username:{request.username} already exist",
        )

    newuser = models.User(
        username=request.username,
        email=request.email,
        password=PassHash.hash(request.password),
    )
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser


@app.get("/user", status_code=200, response_model=List[schemas.UserBase])
async def get_user(db: Session = Depends(get_db)):
    stmt = db.query(models.User).all()
    return [schemas.UserBase.from_orm(x) for x in stmt]


@app.delete("/user/{userid}", status_code=204)
async def del_user(userid: int, db: Session = Depends(get_db)):
    stmt = db.query(models.User).filter(models.User.id == userid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"User with id:{userid} is not available"
        )
    db.query(models.User).filter(models.User.id == userid).delete(
        synchronize_session=False
    )
    db.commit()
    return {"detail": f"User id:{userid} has been deleted"}
