import models
from database import SessionLocal, engine
from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/financial_data")
def read_financedata(db: Session = Depends(get_db)):
    finance_data = db.execute(select(models.FinanceData)).all()
    return finance_data
