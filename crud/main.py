from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from crud import models, schemas
from crud.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gengsu Tracker Issue")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/issue", status_code=201, response_model=schemas.IssueBase)
def create_issue(issue=schemas.IssueIn, db: Session = Depends(get_db)):
    # issue_id = Issue(**issue.dict(), createdAt=datetime.now())
    # newissue = Issue(id=issue_id + 1, title=issue.title, description=issue.description)
    # db.add(newissue)
    # db.commit()
    # db.refresh(newissue)
    return "ok"
