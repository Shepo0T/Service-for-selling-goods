from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_cxt.hash(password)


def check_password(hashed_password: str, password_in_db) -> bool:
    return pwd_cxt.verify(password_in_db, hashed_password)