from flask import Blueprint, jsonify, request
from app import db
from app.models import baza

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return jsonify({"status": "ok", "message": "Baza API is running (test)"})

@main.route("/baza", methods=["GET"])
def get_baza():
    wpisy = baza.query.all()
    return jsonify([wpis.to_dict() for wpis in wpisy])

@main.route("/baza", methods=["POST"])
def create_wpis():
    data = request.get_json()

    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "title i content są wymagane"}), 400

    wpis = baza(title=data["title"], content=data["content"])
    db.session.add(wpis)
    db.session.commit()

    return jsonify(wpis.to_dict()), 201