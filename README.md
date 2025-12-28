# 🚨 Real-Time Incident Reporting Platform

A full-stack **AI-assisted real-time incident reporting and coordination system** that enables citizens to report incidents in real time and allows administrators to verify, track, and resolve them efficiently.

Built as a **hackathon-ready project** with live updates, admin moderation, and database-backed persistence.

---

## 🌟 Features

### 👥 Public Users
- Report incidents (Fire, Road Accident, Flood, etc.)
- View live incident feed
- Upvote incidents to increase credibility
- Real-time feed auto-refresh (every 3 seconds)

### 🛠️ Admin Dashboard
- View all reported incidents
- Update incident status:
  - `unverified`
  - `in_progress`
  - `resolved`
- Status changes persist in the database
- Admin-controlled moderation workflow

### 🤖 AI Assistance
- Automatic severity prediction
- Duplicate incident detection
- Confidence scoring for severity classification

---

## 🧱 Tech Stack

### Frontend
- HTML
- CSS
- JavaScript (Vanilla JS)
- Fetch API

### Backend
- FastAPI (Python)
- SQLAlchemy ORM
- MySQL (Database)
- Uvicorn (ASGI Server)

### AI / Logic
- NLP-based severity prediction
- Text similarity for duplicate detection

---

## 📁 Project Structure

incident-response-platform/
│
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry point
│   │   ├── database.py          # MySQL connection
│   │   ├── models.py            # DB models
│   │   ├── schemas.py           # Pydantic schemas
│   │   ├── crud.py              # DB operations
│   │   ├── auth.py              # Admin authentication
│   │   ├── deps.py              # Dependencies (DB, auth)
│   │   └── routers/
│   │       ├── incidents.py     # Incident APIs
│   │       └── admin.py         # Admin APIs
│   │
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── index.html               # Incident feed
│   ├── report.html              # Report incident
│   ├── admin.html               # Admin dashboard
│   │
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   ├── api.js               # API calls
│   │   ├── feed.js              # Incident feed logic
│   │   ├── report.js            # Report submission
│   │   └── admin.js             # Admin actions
│   │
│   └── assets/                  # Icons, images
│
├── database/
│   └── schema.sql               # MySQL schema
│
├── README.md                    # Project overview
└── deployment.md                # Deployment steps

---

### ▶️ How to Run the Project (Local)

# 1️⃣ Backend Setup (Required for Full Functionality)

    cd backend
    pip install -r requirements.txt
    uvicorn app.main:app --reload

# 2️⃣ Run the Frontend
    frontend/index.html

---

### 🌍 Deployment Note (IMPORTANT)

🚨 Only the frontend is deployed in the hosted version of this project.
The backend is NOT deployed
API calls will work only when backend is running locally

This is intentional due to:
Hackathon time constraints
Database & AI model dependency

⚠️ For full functionality, please run the backend locally as described above.

---

### 🏆 Use Cases

- Smart city incident monitoring
- Emergency response coordination
- Crowd-sourced incident verification
- Disaster management systems
- Traffic & safety reporting

---

### 🚀 Future Improvements

- Authentication (Admin & Users)
-Real-time WebSocket updates
-Geo-mapping with Google Maps
-Notification system (SMS / Email)
-Mobile app integration

---

