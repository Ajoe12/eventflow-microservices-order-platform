from fastapi import FastAPI
from app.routes import item_routes
from app.db import init_db

app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()

app.include_router(item_routes.router)

@app.get("/")
def root():
    return {"message": "Item Service Running"}