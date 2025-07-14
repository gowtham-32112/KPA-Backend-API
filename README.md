# KPA-Backend-API
This project implements two backend APIs using Flask and PostgreSQL based on the Swagger documentation and Postman collection provided by Sarva Suvidhan. It includes full CRUD-like endpoints for bogie checksheet and wheel specification forms, with proper data validation, error handling, and testing via Postman.

**Sarva Suvidhan - KPA Backend API Assignment**
📌 Project Overview
This Flask-based backend project implements two APIs based on the Swagger documentation and Postman collection provided by Sarva Suvidhan for KPA form data management.

🚀 APIs Implemented
1. POST /api/forms/bogie-checksheet
Accepts nested JSON for:
formNumber, inspectionBy, inspectionDate
bogieDetails, bogieChecksheet, bmbcChecksheet
✅ Returns success message with status 201 Created
❌ Handles duplicate formNumber (409 Conflict)
2. POST /api/forms/wheel-specifications
Accepts:
formNumber, submittedBy, submittedDate
Nested fields dictionary with full wheel measurements
✅ Returns saved confirmation and 201 Created
3. GET /api/forms/wheel-specifications
Accepts query params:
formNumber, submittedBy, submittedDate
✅ Returns filtered list of matching entries
🧰 Tech Stack
Backend: Python (Flask)
Database: PostgreSQL
ORM: SQLAlchemy
API Testing: Postman
Environment Config: python-dotenv
yourname_kpa_backend/
├── app.py
├── config.py
├── extensions.py
├── .env
├── requirements.txt
├── README.md
├── bogie_checksheet_body.json
├── wheel_specification_body.json
├── models/
│   └── model.py
├── routes/
│   ├── api1.py
│   ├── api2.py
│   ├── bogie_checksheet.py
│   └── wheel_specifications.py


⚙️ Setup Instructions
1. Clone or unzip the project
git clone <Sarva-Suvidhan-Project> && cd api-project


python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt


3. Setup PostgreSQL
Create database named: kpa_db

Add .env:

bash
DATABASE_URL=postgresql://postgres:admin123@localhost:5432/kpa_db

#run project
python app.py

#create table manually
from app import app
from extensions import db
with app.app_context():
    db.create_all()


Includes:

✅ POST - Bogie Checksheet

✅ POST - Wheel Specification

✅ GET - Wheel Specification
