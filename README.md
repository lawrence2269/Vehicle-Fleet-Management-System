# Vehicle Fleet Management System

## Overview
The Vehicle Fleet Management System is a real-time application designed to manage vehicle information, track vehicle statuses, and generate maintenance alerts. The system leverages FastAPI for creating complex REST APIs, PostgreSQL for data storage, Apache Kafka for real-time data streaming, and Docker for containerization.

## Architecture
The project is composed of three main microservices:
1. **Vehicle Service**: Handles CRUD operations for vehicle data.
2. **Tracking Service**: Manages vehicle tracking and status updates.
3. **Alert Service**: Generates and manages maintenance alerts based on vehicle data.

## Technologies Used
- **Python**
- **FastAPI**
- **PostgreSQL**
- **Apache Kafka**
- **Docker**

## Components

### 1. Vehicle Service
Handles CRUD operations for vehicle data.

#### Endpoints
- `POST /vehicles/`: Create a new vehicle.
- `GET /vehicles/{vehicle_id}`: Retrieve a vehicle by ID.
- `PUT /vehicles/{vehicle_id}`: Update a vehicle by ID.
- `DELETE /vehicles/{vehicle_id}`: Delete a vehicle by ID.

### 2. Tracking Service
Manages vehicle tracking and status updates.

#### Endpoints
- `POST /track/`: Update vehicle tracking data.
- `GET /track/{vehicle_id}`: Retrieve the latest tracking data for a vehicle by ID.

### 3. Alert Service
Generates and manages maintenance alerts based on vehicle data.

#### Endpoints
- `GET /alerts/`: Generate maintenance alerts based on vehicle data.
- `GET /alerts/{vehicle_id}`: Retrieve maintenance alerts for a vehicle by ID.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/vehicle-fleet-management.git
   cd vehicle-fleet-management
   
2. **Set up the Docker environment:**
Create a docker-compose.yml file to set up PostgreSQL, Kafka, and the microservices.
<pre>
  <code>
    version: '3'
services:
  postgres:
    image: postgres:latest
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: fleet_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  kafka:
    image: wurstmeister/kafka:latest
    environment:
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
    ports:
      - "9092:9092"
    depends_on:
      - zookeeper

  zookeeper:
    image: wurstmeister/zookeeper:latest
    ports:
      - "2181:2181"

  vehicle_service:
    build:
      context: .
      dockerfile: Dockerfile_vehicle_service
    ports:
      - "8000:8000"
    depends_on:
      - postgres
      - kafka

  tracking_service:
    build:
      context: .
      dockerfile: Dockerfile_tracking_service
    ports:
      - "8001:8001"
    depends_on:
      - postgres
      - kafka

  alert_service:
    build:
      context: .
      dockerfile: Dockerfile_alert_service
    ports:
      - "8002:8002"
    depends_on:
      - postgres
      - kafka

volumes:
  postgres_data:
  </code>
</pre>

3. **Build and run the services:**
   docker-compose up --build

4. **Access the services:**
- **Vehicle Service:** http://localhost:8000
- **Tracking Service:** http://localhost:8001
- **Alert Service:** http://localhost:8002

5. **Usage**
- Use the Vehicle Service to create, read, update, and delete vehicle data.
- Use the Tracking Service to update and retrieve tracking data for vehicles.
- Use the Alert Service to generate and retrieve maintenance alerts.

6. **License**
   
This project is licensed under the MIT License.

8. **Acknowledgements**
   
Thanks to the FastAPI, Docker, PostgreSQL, and Apache Kafka communities for their excellent tools and documentation.
