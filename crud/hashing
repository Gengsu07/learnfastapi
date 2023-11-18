from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PassHash:
    def hash(password: str):
        return pwd_ctx.hash(password)
