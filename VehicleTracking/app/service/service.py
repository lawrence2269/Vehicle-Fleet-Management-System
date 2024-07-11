from app.dao import dao
from app.schemas.schemas import VehicleTrackingCreate
from sqlalchemy.orm import Session


def update_tracking_data(vehicle_track: VehicleTrackingCreate, db: Session):
    return dao.update_tracking_data(vehicle_track, db)


def get_tracking_data(vehicle_id: int, db: Session):
    return dao.get_tracking_data(vehicle_id, db)