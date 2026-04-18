from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from authlib.jose import jwt
from app.core.config import SECRET_KEY

security = HTTPBearer()


def decode_token(token: str):
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()
        return claims
    except Exception:
        raise HTTPException(status_code=403, detail="Invalid or Expired Token")


def get_current_user(token = Depends(security)):
    return decode_token(token.credentials)


def require_admin(user=Depends(get_current_user)):
    if user.get("role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user