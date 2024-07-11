from app.models.models import Vehicle
from app.schemas.schemas import VehicleCreate, VehicleUpdate
from sqlalchemy.orm import Session


def create_vehicle(vehicle: VehicleCreate, db: Session):
    db_vehicle = Vehicle(make=vehicle.make,
                         model=vehicle.model,
                         year=vehicle.year,
                         mileage=vehicle.mileage)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def get_vehicles(db: Session):
    vehicles = db.query(Vehicle).all()
    return vehicles


def get_vehicles_by_make(make: str, db: Session):
    vehicles = db.query(Vehicle).filter(Vehicle.make == make).all()
    return vehicles


def get_vehicles_by_id(vehicle_id: int, db: Session):
    vehicle = db.query(Vehicle).filter(Vehicle.vehicleId == vehicle_id).first()
    return vehicle


def delete_vehicle(vehicle_id: int, db: Session):
    db.query(Vehicle).filter(Vehicle.vehicleId == vehicle_id).delete()
    db.commit()
    return True


def update_vehicle(vehicle_id: int, vehicle_update: VehicleUpdate, db: Session):
    vehicle = db.query(Vehicle).filter(Vehicle.vehicleId == vehicle_id).first()
    if not vehicle:
        return None

    for key, value in vehicle_update.model_dump(exclude_unset=True).items():
        setattr(vehicle, key, value)

    db.commit()
    db.refresh(vehicle)
    return vehicle
