from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.schemas.schemas import VehicleCreate, VehicleUpdate
from app.config.database import get_db, Base, engine
from app.service import service

router = APIRouter(
    prefix="/vehicles",
    responses={404: {"description": "Not found"}},
)

# Create all tables
Base.metadata.create_all(bind=engine)


@router.post("/create-vehicles", response_model=None)
async def add_vehicles(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    service.create_vehicle(vehicle, db)
    return JSONResponse(content={"message": "Record added"})


@router.get("/")
async def get_all_vehicles(db: Session = Depends(get_db)):
    return JSONResponse(content=jsonable_encoder(service.get_vehicles(db)))


@router.get("/{vehicle_make}")
async def get_vehicles_by_make(vehicle_make: str, db: Session = Depends(get_db)):
    vehicles = service.get_vehicles_by_make(vehicle_make, db)
    if not vehicles:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return JSONResponse(content=jsonable_encoder(vehicles))


@router.delete("/{vehicle_id}")
async def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle_by_id = service.get_vehicles_by_id(vehicle_id, db)
    if not vehicle_by_id:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    is_deleted = service.delete_vehicle(vehicle_id, db)
    if is_deleted:
        return JSONResponse(content={"message": "Record removed"})


@router.put("/{vehicle_id}")
async def update_vehicle(vehicle_id: int, vehicle_update: VehicleUpdate, db: Session = Depends(get_db)):
    updated_vehicle = service.update_vehicle(vehicle_id, vehicle_update, db)
    if not updated_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return JSONResponse(content={"message": "Record updated"})
