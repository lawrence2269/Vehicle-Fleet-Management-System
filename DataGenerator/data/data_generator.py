from faker import Faker
from faker_vehicle import VehicleProvider
import random
from sqlalchemy.orm import sessionmaker
from config.database import engine
import time
from service import service

fake = Faker()
fake.add_provider(VehicleProvider)


def generate_vehicle_data():
    return fake.vehicle_make(), fake.vehicle_category(), str(fake.year()), random.randint(0, 300000)


def generate_tracking_id():
    prefix = "TRK"
    random_number = random.randint(1, 25000)
    timestamp = int(time.time())
    return f"{prefix}{random_number}{timestamp}"


def generate_vehicle_tracking_data():
    session = sessionmaker(bind=engine)
    db = session()
    vehicles = service.get_vehicles()
    db.close()
    tracking_data = {
        'trackingId': generate_tracking_id(),
        'vehicleId': random.choice([vehicle.vehicleId for vehicle in vehicles]),
        'latitude': random.uniform(-90, 90),
        'longitude': random.uniform(-180, 180),
        'mileage': random.randint(0, 300000),
        'status': random.choice(['running', 'stopped', 'maintenance_required'])
    }
    return tracking_data
