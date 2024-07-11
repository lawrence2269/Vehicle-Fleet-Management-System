# Vehicle Fleet Management System

## Overview
The Vehicle Fleet Management System is a real-time application designed to manage vehicle information, track vehicle statuses, and generate maintenance alerts. The system leverages FastAPI for creating REST APIs, and MySQL for data storage.

## Architecture
The project is composed of three main microservices and one data generator:
1. **Data Generator**: Mimicking to generate streaming and static data.
2. **Vehicle Service**: Handles CRUD operations for vehicle data.
3. **Tracking Service**: Manages vehicle tracking and status updates.
4. **Alert Service**: Generates and manages maintenance alerts based on vehicle data.

## Technologies Used
- **Python**
- **FastAPI**
- **MySQL**

## Components

### 1. Vehicle Service
Handles CRUD operations for vehicle data.

#### Endpoints
- `POST /vehicles/`: Create a new vehicle.
- `GET /vehicles/{make}`: Retrieve a vehicle by make.
- `PUT /vehicles/{vehicle_id}`: Update a vehicle by ID.
- `DELETE /vehicles/{vehicle_id}`: Delete a vehicle by ID.

### 2. Tracking Service
Manages vehicle tracking and status updates.

#### Endpoints
- `POST /track/update-tracking`: Update vehicle tracking data.
- `GET /track/{vehicle_id}`: Retrieve the latest tracking data for a vehicle by ID.

### 3. Alert Service
Generates and manages maintenance alerts based on vehicle data.

#### Endpoints
- `GET /alerts/add-alert`: Generate maintenance alerts based on vehicle data.
- `GET /alerts/{vehicle_id}`: Retrieve maintenance alerts for a vehicle by ID.

## Getting Started

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/vehicle-fleet-management.git
   cd vehicle-fleet-management
   
2. **Install the packages:**
   Use pip install -r requirements.txt

3. **Setting up database:**
   - Install MySQL client and MySQL workbench.
   - Set the username, password, and database of your own and update the same in '.env' file in 4 project folders.

4. **Launch the Python files:**
   - Run the following commands in the terminals in the three microservices project
     - **uvicorn app.main:api --reload --port 8000**  for Vehicles microservice.
     - **uvicorn app.main:api --reload --port 8001**  for Vehiclestracking microservice.
     - **uvicorn app.main:api --reload --port 8002**  for alert microservice.
   - Uncomment the lines below '''if __name__ == "__main__"''' in main.py of DataGenerator project, especially for 'for loop' to insert some values in 'Vehicles' table and then you comment it and run the program 
     once again to send streaming data to the microservices

5. **Access the services:**
- **Vehicle Service:** http://127.0.0.1:8000
- **Tracking Service:** http://127.0.0.1:8001
- **Alert Service:** http://127.0.0.1:8002

6. **Usage**
- Use the Vehicle Service to create, read, update, and delete vehicle data.
- Use the Tracking Service to update and retrieve tracking data for vehicles.
- Use the Alert Service to generate and retrieve maintenance alerts.

7. **License**
This project is licensed under the MIT License.
