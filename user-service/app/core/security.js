from passlib.context import CryptContext
from authlib.jose import jwt
import datetime
from app.core.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(data: dict):
    header = {"alg": ALGORITHM}
    payload = data.copy()
    payload["exp"] = int((datetime.datetime.utcnow() + datetime.timedelta(hours=1)).timestamp())
    return jwt.encode(header, payload, SECRET_KEY)

def decode_token(token):
    return jwt.decode(token, SECRET_KEY)