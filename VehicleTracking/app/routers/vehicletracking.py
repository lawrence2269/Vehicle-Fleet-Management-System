from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from decouple import config
from app.config.database import get_db, Base, engine
from app.schemas.schemas import VehicleTrackingCreate
from app.service import service
import requests

router = APIRouter(
    prefix="/track",
    responses={404: {"description": "Not found"}},
)

# Create all tables
Base.metadata.create_all(bind=engine)


@router.post("/update-tracking", response_model=None)
async def update_tracking(vehicle_track: VehicleTrackingCreate, db: Session = Depends(get_db)):
    vehicle_track_data = service.update_tracking_data(vehicle_track, db)
    if vehicle_track.mileage >= int(config('MAINTENANCE_THRESHOLD')):
        data = {'vehicleId': vehicle_track.vehicleId,
                'alert': vehicle_track.status}
        response = requests.post(config('ALERT_URL'), json=data)
        print(response.json())
    if not vehicle_track_data:
        raise HTTPException(status_code=500, detail="Some problem occurred")
    return JSONResponse(content={"message": "Record added"})


@router.get("/{vehicle_id}")
async def get_tracking(vehicle_id: int, db: Session = Depends(get_db)):
    vehicles = service.get_tracking_data(vehicle_id, db)
    if not vehicles:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return JSONResponse(content=jsonable_encoder(vehicles))
