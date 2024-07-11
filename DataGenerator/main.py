from service import service
from schemas.schemas import VehicleCreate
from data import data_generator as data
# from producer import kafkaproducer
from decouple import config
import requests
import time


def create_vehicle():
    make, model, year, mileage = data.generate_vehicle_data()
    vehicle_data = VehicleCreate(
        make=make,
        model=model,
        year=year,
        mileage=mileage
    )

    # Insert the vehicle data into the database
    new_vehicle = service.create_vehicle(vehicle_data)

    print(new_vehicle)


def fetch_all_vehicles():
    # Fetch vehicles by make
    vehicles = service.get_vehicles()

    return vehicles


def fetch_vehicles_by_make(make: str):
    # Fetch vehicles by make
    vehicles = service.get_vehicles_by_make(make)

    # Print fetched vehicles
    print(f"Vehicles with make '{make}':")
    for vehicle in vehicles:
        print(f"ID: {vehicle.vehicleId}, Make: {vehicle.make}, Model: {vehicle.model}")

    print(type(vehicles))


if __name__ == "__main__":
    # for i in range(0,50):
    #     create_vehicle()      # Run this function once to insert some sample data into Vehicles table
    # fetch_vehicles_by_make("Toyota")
    while True:
        response = requests.post(config('VEHICLE_TRACK_URL'), json=data.generate_vehicle_tracking_data())
        print(response.json())
        time.sleep(1)
