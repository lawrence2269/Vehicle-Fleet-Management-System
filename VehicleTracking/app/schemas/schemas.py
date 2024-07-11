from decimal import Decimal
from pydantic import BaseModel


class VehicleTrackingBase(BaseModel):
    trackingId: str
    vehicleId: int
    latitude: Decimal
    longitude: Decimal
    mileage: int
    status: str


class VehicleTrackingCreate(VehicleTrackingBase):
    pass


class VehicleTracking(VehicleTrackingBase):
    class config:
        from_attributes = True


class VehicleBase(BaseModel):
    make: str
    model: str
    year: str
    mileage: int


class Vehicle(VehicleBase):
    class Config:
        from_attributes = True
