from fastapi import FastAPI
from app.routers import alerts


api = FastAPI()


api.include_router(alerts.router)


@api.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
