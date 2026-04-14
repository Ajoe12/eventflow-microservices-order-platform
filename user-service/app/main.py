from fastapi import FastAPI
from app.routes import user_routes
from app.db import init_db

app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()

app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"message": "User Service Running"}