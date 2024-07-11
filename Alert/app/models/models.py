from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

from app.config.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicleId = Column(Integer, primary_key=True, autoincrement=True)
    make = Column(String(50))
    model = Column(String(50))
    year = Column(String(10))
    mileage = Column(Integer, default=0)


class Alert(Base):
    __tablename__ = "alerts"
    alertId = Column(Integer, primary_key=True, autoincrement=True)
    vehicleId = Column(Integer, ForeignKey("vehicles.vehicleId"))
    alert = Column(String(255))
