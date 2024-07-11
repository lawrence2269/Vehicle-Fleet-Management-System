from pydantic import BaseModel


class AlertBase(BaseModel):
    vehicleId: int
    alert: str


class AlertCreate(AlertBase):
    pass


class Alert(AlertBase):
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
