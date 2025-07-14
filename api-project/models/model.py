from extensions import db 
from datetime import datetime

class KPAForm(db.Model):
    __tablename__ = 'kpa_forms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "created_at": self.created_at.isoformat()
        }
print("✅ KPAForm model loaded.")

class WheelSpecification(db.Model):
    __tablename__ = 'wheel_specifications'

    id = db.Column(db.Integer, primary_key=True)
    form_number = db.Column(db.String(100), nullable=False, unique=True)
    submitted_by = db.Column(db.String(100), nullable=False)
    submitted_date = db.Column(db.String(20), nullable=False)
    fields = db.Column(db.JSON, nullable=False)

    def to_dict(self):
        return {
            "formNumber": self.form_number,
            "submittedBy": self.submitted_by,
            "submittedDate": self.submitted_date,
            "fields": self.fields
        }


class BogieChecksheet(db.Model):
    __tablename__ = 'bogie_checksheet'

    id = db.Column(db.Integer, primary_key=True)
    form_number = db.Column(db.String(100), nullable=False, unique=True)
    inspection_by = db.Column(db.String(100), nullable=False)
    inspection_date = db.Column(db.String(20), nullable=False)
    bogie_details = db.Column(db.JSON, nullable=False)
    bogie_checksheet = db.Column(db.JSON, nullable=False)
    bmbc_checksheet = db.Column(db.JSON, nullable=False)

    def to_dict(self):
        return {
            "formNumber": self.form_number,
            "inspectionBy": self.inspection_by,
            "inspectionDate": self.inspection_date,
            "status": "Saved"
        }
