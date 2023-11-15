import models
from database import SessionLocal, engine
from fastapi import Depends, FastAPI
from models import Issue
from schemas import IssueIn
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gengsu Tracker Issue")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/issue", status_code=201)
def create_issue(issue=IssueIn, db: Session = Depends(get_db)):
    newissue = Issue(title=issue.title, description=issue.description)
    db.add(newissue)
    db.commit()
    db.refresh(newissue)
    return newissue
