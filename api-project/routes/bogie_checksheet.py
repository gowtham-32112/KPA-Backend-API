from flask import Blueprint, request, jsonify
from extensions import db
from models.model import BogieChecksheet
from sqlalchemy.exc import IntegrityError

bogie_bp = Blueprint("bogie_bp", __name__)

@bogie_bp.route("/api/forms/bogie-checksheet", methods=["POST"])
def create_bogie_checksheet():
    data = request.get_json()

    try:
        form = BogieChecksheet(
            form_number=data.get("formNumber"),
            inspection_by=data.get("inspectionBy"),
            inspection_date=data.get("inspectionDate"),
            bogie_details=data.get("bogieDetails"),
            bogie_checksheet=data.get("bogieChecksheet"),
            bmbc_checksheet=data.get("bmbcChecksheet")
        )
        db.session.add(form)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "data": form.to_dict()
        }), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Form with this number already exists!"}), 409

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
