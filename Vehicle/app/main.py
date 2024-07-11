from fastapi import FastAPI
from app.routers import vehicles

api = FastAPI()


api.include_router(vehicles.router)


@api.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
