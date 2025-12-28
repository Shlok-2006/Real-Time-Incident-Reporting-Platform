from pydantic import BaseModel

class IncidentCreate(BaseModel):
    type: str
    description: str
    location: str
    state: str
    pin: int


class IncidentResponse(BaseModel):
    id: str
    type: str
    description: str
    location: str
    state: str
    pin: int
    severity: str
    severity_confidence: float
    is_duplicate: bool
    duplicate_score: float
    votes: int
    status: str

    class Config:
        from_attributes = True
