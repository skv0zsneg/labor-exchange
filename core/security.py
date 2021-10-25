from jose import jwt
from typing import Optional
from datetime import datetime, timedelta
from passlib.context import CryptContext

from .config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    pwd_context.verify(password, hash)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({'exp': datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> Optional[dict]:
    try:
        encoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except jwt.JWSError:
        return None
    return encoded_jwt