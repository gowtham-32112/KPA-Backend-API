from flask import Blueprint, request, jsonify
from extensions import db
from models.model import WheelSpecification
from sqlalchemy.exc import IntegrityError

wheel_bp = Blueprint("wheel_bp", __name__)

@wheel_bp.route("/api/forms/wheel-specifications", methods=["POST"])
def submit_wheel_specification():
    data = request.get_json()

    try:
        form = WheelSpecification(
            form_number=data.get("formNumber"),
            submitted_by=data.get("submittedBy"),
            submitted_date=data.get("submittedDate"),
            fields=data.get("fields")
        )

        db.session.add(form)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Wheel specification submitted successfully.",
            "data": {
                "formNumber": form.form_number,
                "submittedBy": form.submitted_by,
                "submittedDate": form.submitted_date,
                "status": "Saved"
            }
        }), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Form with this number already exists."}), 409

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# ✅ GET: Fetch forms using filters
@wheel_bp.route("/api/forms/wheel-specifications", methods=["GET"])
def get_wheel_specifications():
    form_number = request.args.get("formNumber")
    submitted_by = request.args.get("submittedBy")
    submitted_date = request.args.get("submittedDate")

    query = WheelSpecification.query

    if form_number:
        query = query.filter_by(form_number=form_number)
    if submitted_by:
        query = query.filter_by(submitted_by=submitted_by)
    if submitted_date:
        query = query.filter_by(submitted_date=submitted_date)

    results = query.all()

    return jsonify({
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": [item.to_dict() for item in results]
    }), 200
