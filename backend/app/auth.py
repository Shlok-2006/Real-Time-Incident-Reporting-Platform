from passlib.context import CryptContext
from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models
from app.database import get_db


pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


# ---- PASSWORD UTILS ----
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)


# ---- CREATE ADMIN (ONE TIME) ----
def create_admin(db: Session, username: str, password: str):
    admin = models.AdminUser(
        username=username,
        password_hash=hash_password(password)
    )
    db.add(admin)
    db.commit()

# ---- AUTH CHECK ----
def admin_auth(token: str = Header(...), db: Session = Depends(get_db)):
    admin = db.query(models.AdminUser).filter(
        models.AdminUser.username == token
    ).first()

    if not admin:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return admin
