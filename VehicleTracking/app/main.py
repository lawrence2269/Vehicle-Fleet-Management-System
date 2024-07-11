from fastapi import FastAPI
from app.routers import vehicletracking


api = FastAPI()


api.include_router(vehicletracking.router)


@api.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
