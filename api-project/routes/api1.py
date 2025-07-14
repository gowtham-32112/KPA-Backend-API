from flask import Blueprint, request, jsonify
from extensions import db
from models.model import KPAForm
from sqlalchemy.exc import IntegrityError

api1_bp = Blueprint("api1", __name__)

@api1_bp.route("/form", methods=["POST"])
def create_form():
    data = request.get_json()

    if not all(key in data for key in ("name", "phone", "email")):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        form = KPAForm(
            name=data["name"],
            phone=data["phone"],
            email=data["email"]
        )
        db.session.add(form)
        db.session.commit()
        return jsonify({"message": "Form entry created successfully", "data": form.to_dict()}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Phone number already exists!"}), 409

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@api1_bp.route("/form", methods=["GET"])
def get_forms():
    try:
        forms = KPAForm.query.all()
        return jsonify([form.to_dict() for form in forms]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
