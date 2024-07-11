from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, DECIMAL

from app.config.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicleId = Column(Integer, primary_key=True, autoincrement=True)
    make = Column(String(50))
    model = Column(String(50))
    year = Column(String(10))
    mileage = Column(Integer, default=0)


class VehicleTracking(Base):
    __tablename__ = "vehicle_tracking"

    trackingId = Column(String(50), primary_key=True)
    vehicleId = Column(Integer, ForeignKey("vehicles.vehicleId"))
    latitude = Column(DECIMAL(9, 6))
    longitude = Column(DECIMAL(9, 6))
    mileage = Column(Integer, default=0)
    status = Column(String(255))
