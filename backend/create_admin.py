from app.database import SessionLocal
from app.auth import create_admin

db = SessionLocal()

create_admin(db, "admin", "admin123")

db.close()

print("Admin user created successfully")
