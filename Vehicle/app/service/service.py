from app.dao import dao
from app.schemas.schemas import VehicleCreate, VehicleUpdate
from sqlalchemy.orm import Session


def create_vehicle(vehicle: VehicleCreate, db: Session):
    return dao.create_vehicle(vehicle, db)


def get_vehicles(db: Session):
    return dao.get_vehicles(db)


def get_vehicles_by_make(make: str, db: Session):
    return dao.get_vehicles_by_make(make, db)


def get_vehicles_by_id(vehicle_id: int, db: Session):
    return dao.get_vehicles_by_id(vehicle_id, db)


def delete_vehicle(vehicle_id: int, db: Session):
    return dao.delete_vehicle(vehicle_id, db)


def update_vehicle(vehicle_id: int, vehicle_update: VehicleUpdate, db: Session):
    return dao.update_vehicle(vehicle_id, vehicle_update, db)
