from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid
from app.database import SessionLocal
from app import models, schemas
from app.ai.deduplication import check_duplicate
from app.ai.severity import predict_severity

router = APIRouter(prefix="/incidents", tags=["Incidents"])



# ---- DB Dependency ----
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---- CREATE INCIDENT ----
@router.post("", response_model=schemas.IncidentResponse)
def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):

    existing = db.query(models.Incident.description).all()
    existing_texts = [e[0] for e in existing]

    is_dup, dup_score = check_duplicate(incident.description, existing_texts)
    severity, confidence = predict_severity(incident.description)

    new_incident = models.Incident(
        id=str(uuid.uuid4()), 
        type=incident.type,
        description=incident.description,
        location=incident.location,
        state=incident.state,
        pin=incident.pin,
        severity=severity,
        severity_confidence=confidence,
        is_duplicate=is_dup,
        duplicate_score=dup_score
    )

    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)

    # 🔹 add timeline entry
    db.add(models.IncidentStatusHistory(
        incident_id=new_incident.id,
        status="reported"
    ))
    db.commit()

    return new_incident




# ---- GET ALL INCIDENTS ----
@router.get("", response_model=list[schemas.IncidentResponse])
def get_incidents(db: Session = Depends(get_db)):
    return (
        db.query(models.Incident)
        .order_by(models.Incident.created_at.desc())
        .all()
    )


# ---- UPVOTE ----
@router.post("/{incident_id}/upvote")
def upvote_incident(
    incident_id: str,
    db: Session = Depends(get_db)
):
    incident = db.query(models.Incident).filter(
        models.Incident.id == incident_id
    ).first()

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    incident.votes += 1
    db.commit()

    return {"message": "Upvoted"}


# ---- TIMELINE ----
@router.get("/{incident_id}/timeline")
def get_incident_timeline(
    incident_id: str,
    db: Session = Depends(get_db)
):
    history = (
        db.query(models.IncidentStatusHistory)
        .filter(models.IncidentStatusHistory.incident_id == incident_id)
        .order_by(models.IncidentStatusHistory.changed_at)
        .all()
    )
    return history
