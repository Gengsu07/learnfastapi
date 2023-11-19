from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..hashing import Verify
from ..models import User
from ..schemas import Login, Token
from ..token import create_access_token

router = APIRouter(tags=["Authentication"])


@router.post("/login", status_code=202, response_model=Token)
def Login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=401,
            detail=f"User with email:{request.username} not exist",
        )
    passw_verif = Verify(request.password, user.password)
    if not passw_verif:
        raise HTTPException(
            status_code=401,
            detail="invalid credentials",
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
