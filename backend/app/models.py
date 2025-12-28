from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(String(36), primary_key=True, index=True)  # UUID
    type = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    location = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    pin = Column(Integer, nullable=False)

    severity = Column(String(20))
    severity_confidence = Column(Float)

    is_duplicate = Column(Boolean, default=False)
    duplicate_score = Column(Float, default=0.0)

    votes = Column(Integer, default=0)
    status = Column(String(20), default="unverified")
    created_at = Column(DateTime, default=datetime.utcnow)

    status_history = relationship(
        "IncidentStatusHistory",
        back_populates="incident",
        cascade="all, delete-orphan"
    )


class IncidentStatusHistory(Base):
    __tablename__ = "incident_status_history"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(
        String(36),
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False
    )

    status = Column(String(50), nullable=False)
    changed_at = Column(DateTime, default=datetime.utcnow)

    incident = relationship("Incident", back_populates="status_history")



class AdminUser(Base):
    __tablename__ = "admin_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(255))
