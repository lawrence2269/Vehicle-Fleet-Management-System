from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.config.database import get_db, Base, engine
from app.schemas.schemas import AlertCreate
from app.service import service

router = APIRouter(
    prefix="/alert",
    responses={404: {"description": "Not found"}},
)

# Create all tables
Base.metadata.create_all(bind=engine)


@router.post("/add-alert", response_model=None)
async def add_alerts(alert_create: AlertCreate, db: Session = Depends(get_db)):
    service.add_alerts(alert_create, db)
    return JSONResponse(content={"message": "Alert added"})


@router.get("/{vehicle_id}")
async def get_alert_data(vehicle_id: int, db: Session = Depends(get_db)):
    alerts = service.get_alert_data(vehicle_id, db)
    if not alerts:
        raise HTTPException(status_code=404, detail="Alerts not found")
    return JSONResponse(content=jsonable_encoder(alerts))
