from sqlalchemy.orm import Session
from app import models, schemas

def create_incident(db: Session, incident: schemas.IncidentCreate, severity: str):
    db_incident = models.Incident(
        type=incident.type,
        description=incident.description,
        latitude=incident.latitude,
        longitude=incident.longitude,
        severity=severity
    )
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

def get_incidents(db: Session):
    return db.query(models.Incident).order_by(models.Incident.created_at.desc()).all()

def get_descriptions(db: Session):
    return [i.description for i in db.query(models.Incident).all()]
