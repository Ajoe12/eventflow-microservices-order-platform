from fastapi import FastAPI
from app.routes import item_routes
from app.db import init_db
import threading
from app.utils.kafka_consumer import start_consumer


app = FastAPI()

@app.on_event("startup")
async def start_db():
    # db startup
    await init_db()
    
    # 🔹 Kafka consumer
    thread = threading.Thread(target=start_consumer)
    thread.daemon = True
    thread.start()

app.include_router(item_routes.router)

@app.get("/")
def root():
    return {"message": "Item Service Running"}