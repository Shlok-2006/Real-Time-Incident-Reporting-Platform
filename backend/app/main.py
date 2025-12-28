from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import incidents, admin
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Real-Time Incident Reporting Platform",
    description="AI-assisted incident reporting and coordination system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(incidents.router)
app.include_router(admin.router, prefix="/admin")

@app.get("/")
def root():
    return {"status": "Backend is running"}
