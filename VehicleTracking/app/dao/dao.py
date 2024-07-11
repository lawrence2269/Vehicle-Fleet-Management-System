from app.models.models import VehicleTracking
from app.schemas.schemas import VehicleTrackingCreate
from sqlalchemy.orm import Session


def update_tracking_data(vehicle_track: VehicleTrackingCreate, db: Session):
    db_vehicle_track = VehicleTracking(trackingId=vehicle_track.trackingId,
                                       vehicleId=vehicle_track.vehicleId,
                                       latitude=vehicle_track.latitude,
                                       longitude=vehicle_track.longitude,
                                       mileage=vehicle_track.mileage,
                                       status=vehicle_track.status)
    db.add(db_vehicle_track)
    db.commit()
    db.refresh(db_vehicle_track)
    return db_vehicle_track


def get_tracking_data(vehicle_id: int, db: Session):
    vehicle_tracking_data = db.query(VehicleTracking).filter(VehicleTracking.vehicleId == vehicle_id).first()
    return vehicle_tracking_data
