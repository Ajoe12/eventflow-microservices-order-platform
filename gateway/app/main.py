from fastapi import FastAPI
from app.routes import user_routes, item_routes
from app.middleware.logging import LoggingMiddleware

app = FastAPI(title="API Gateway")

# 🔹 Middleware
app.add_middleware(LoggingMiddleware)

# 🔹 Routes
app.include_router(user_routes.router)
app.include_router(item_routes.router)


@app.get("/")
def health_check():
    return {"message": "API Gateway Running"}