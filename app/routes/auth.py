from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from ..extensions import db
from ..auth_utils import generate_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def register():
    data = request.json

    if User.query.filter_by(email=data["email"]).first():
        return {"error": "User exists"}, 409

    user = User(
        full_name=data["full_name"],
        email=data["email"],
        password_hash=generate_password_hash(data["password"])
    )

    db.session.add(user)
    db.session.commit()

    return {"message": "Registered"}

@auth_bp.post("/login")
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password_hash(user.password_hash, data["password"]):
        return {"error": "Invalid"}, 401

    token = generate_token(user.id)
    return {"token": token}