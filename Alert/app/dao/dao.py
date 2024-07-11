from app.models.models import Alert
from app.schemas.schemas import AlertCreate
from sqlalchemy.orm import Session


def add_alerts(alert_create: AlertCreate, db: Session):
    db_alert = Alert(vehicleId=alert_create.vehicleId,
                     alert=alert_create.alert)
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert


def get_alert_data(vehicle_id: int, db: Session):
    alert_data = db.query(Alert).filter(Alert.vehicleId == vehicle_id).first()
    return alert_data
