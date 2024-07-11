
from models.models import Vehicle
from schemas.schemas import VehicleCreate
from dao import dao


def create_vehicle(vehicle_create: VehicleCreate) -> Vehicle:
    return dao.create_vehicle(vehicle_create)


def get_vehicles():
    return dao.get_vehicles()


def get_vehicles_by_make(make: str):
    return dao.get_vehicles_by_make(make=make)
