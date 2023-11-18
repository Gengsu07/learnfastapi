from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..hashing import PassHash
from ..models import User
from ..schemas import ShowUser, UserIn

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", status_code=201, response_model=ShowUser)
async def create_user(request: UserIn, db: Session = Depends(get_db)):
    cekusername = db.query(User).filter(User.username == request.username).first()
    if cekusername:
        raise HTTPException(
            status_code=409,
            detail=f"User with username:{request.username} already exist",
        )

    newuser = User(
        username=request.username,
        email=request.email,
        password=PassHash.hash(request.password),
    )
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser


@router.get("/", status_code=200, response_model=List[ShowUser])
async def get_users(db: Session = Depends(get_db)):
    stmt = db.query(User).all()
    return [ShowUser.from_orm(x) for x in stmt]


@router.get("/{userid}", status_code=200, response_model=ShowUser)
async def get_user(userid: int, db: Session = Depends(get_db)):
    stmt = db.query(User).filter(User.id == userid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"User with id:{userid} is not available"
        )
    return ShowUser.from_orm(stmt)


@router.delete("/{userid}", status_code=204)
async def del_user(userid: int, db: Session = Depends(get_db)):
    stmt = db.query(User).filter(User.id == userid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"User with id:{userid} is not available"
        )
    db.query(User).filter(User.id == userid).delete(synchronize_session=False)
    db.commit()
    return {"detail": f"User id:{userid} has been deleted"}
