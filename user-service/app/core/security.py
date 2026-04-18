from fastapi import HTTPException
from passlib.context import CryptContext
from authlib.jose import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import ALGORITHM, SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(data: dict):
    header = {"alg": ALGORITHM}
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(hours=1)
    return jwt.encode(header, payload, SECRET_KEY)

def decode_token(token):
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()
    except Exception:
        raise HTTPException(status_code=403,detail="Invalid or Expired Token")
    return claims