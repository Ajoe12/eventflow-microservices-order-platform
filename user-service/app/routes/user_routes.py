from fastapi import APIRouter, HTTPException, Depends
from app.schemas import UserCreate, UserLogin
from app.models import User
from app.auth import hash_password, verify_password, create_token
from app.dependencies import require_admin

router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate):
    existing = await User.find_one(User.email == user.email)
    if existing:
        raise HTTPException(status_code=400, detail="User exists")

    new_user = User(
        email=user.email,
        password=hash_password(user.password),
        role="USER"
    )

    await new_user.insert()
    return {"message": "User created"}

@router.post("/login")
async def login(user: UserLogin):
    db_user = await User.find_one(User.email == user.email)

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({
        "user_id": str(db_user.id),
        "role": db_user.role
    })

    return {"access_token": token}

# 🔥 Admin-only route
@router.get("/admin")
async def admin_dashboard(user=Depends(require_admin)):
    return {"message": "Welcome Admin"}