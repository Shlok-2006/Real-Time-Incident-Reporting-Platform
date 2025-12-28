from http.client import HTTPException
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Incident
from app.database import get_db
from app import models
from datetime import datetime

router = APIRouter(tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def admin_auth(token: str = Header(...)):
    if token != "admin":
        raise Exception("Unauthorized")

@router.put("/incident/{incident_id}/status")
def update_status(
    incident_id: str,
    status: str,
    db: Session = Depends(get_db),
    _: str = Depends(admin_auth)
):
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    incident.status = status
    db.commit()
    return {"message": "Status updated"}

@router.put("/incident/{incident_id}/status")
def update_status(
    incident_id: str,
    status: str,
    db: Session = Depends(get_db),
    token: str = Header(None)
):
    if token != "admin":
        raise HTTPException(status_code=403, detail="Unauthorized")

    incident = db.query(models.Incident).filter(
        models.Incident.id == incident_id
    ).first()

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    incident.status = status

    history = models.IncidentStatusHistory(
        incident_id=incident.id,
        status=status
    )
    db.add(history)

    db.commit()
    return {"message": "Status updated"}
