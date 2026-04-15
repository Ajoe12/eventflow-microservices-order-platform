from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from app.core.security import decode_token

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    try:
        return decode_token(token.credentials)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

def require_admin(user=Depends(get_current_user)):
    if user.get("role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user