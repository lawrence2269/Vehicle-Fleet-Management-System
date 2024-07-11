from models.models import Vehicle
from schemas.schemas import VehicleCreate
from sqlalchemy.orm import sessionmaker
from config.database import engine
from models.models import Base

Base.metadata.create_all(bind=engine)


def create_vehicle(vehicle_create: VehicleCreate) -> Vehicle:
    session = sessionmaker(bind=engine)
    db = session()
    db_vehicle = Vehicle(make=vehicle_create.make,
                         model=vehicle_create.model,
                         year=vehicle_create.year,
                         mileage=vehicle_create.mileage)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    db.close()
    return db_vehicle


def get_vehicles():
    session = sessionmaker(bind=engine)
    db = session()
    vehicles = db.query(Vehicle).all()
    db.close()
    return vehicles


def get_vehicles_by_make(make: str):
    session = sessionmaker(bind=engine)
    db = session()
    vehicles = db.query(Vehicle).filter(Vehicle.make == make).all()
    db.close()
    return vehicles
