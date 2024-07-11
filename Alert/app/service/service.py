from app.dao import dao
from app.schemas.schemas import AlertCreate
from sqlalchemy.orm import Session


def add_alerts(alert_create: AlertCreate, db: Session):
    return dao.add_alerts(alert_create, db)


def get_alert_data(vehicle_id: int, db: Session):
    return dao.get_alert_data(vehicle_id, db)
