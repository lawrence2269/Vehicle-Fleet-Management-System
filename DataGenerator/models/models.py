from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship

from config.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicleId = Column(Integer, primary_key=True,autoincrement=True)
    make = Column(String(50))
    model = Column(String(50))
    year = Column(String(10))
    mileage = Column(Integer, default=0)

    # Define the relationship to VehicleTracking
    #tracking_records = relationship("VehicleTracking", back_populates="vehicle")


# class VehicleTracking(Base):
#     __tabelname__ = "vehicle_tracking"
#
#     trackingId = Column(String, primary_key=True)
#     vehicleId = Column(Integer, ForeignKey("vehicles.vehicleId"))
#     latitude = Column(DECIMAL(9, 6))
#     longitude = Column(DECIMAL(9, 6))
#     mileage = Column(Integer, default=0)
#     status = Column(String)

    # Define the relationship to Vehicle
    #vehicle = relationship("Vehicle", back_populates="tracking_records")
