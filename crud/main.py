from fastapi import Depends, FastAPI
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


@app.post("/issue", status_code=201)
async def create_issue(issue: schemas.IssueIn, db: Session = Depends(get_db)):
    # newissue = create_new_issue(db, issue)
    newissue = models.Issue(title=issue.title, description=issue.description)

    # Add the new issue to the database
    db.add(newissue)
    db.commit()

    # Refresh the session to ensure we have the latest data (including the generated ID)
    db.refresh(newissue)
    return newissue
