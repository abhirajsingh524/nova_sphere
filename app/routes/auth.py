from flask import Blueprint, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from ..extensions import db
from ..auth_utils import generate_token, verify_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def register():
    data = request.json or {}

    name = data.get("name") or data.get("full_name", "")
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")
    role = data.get("role", "Citizen")

    if not name or not email or not password:
        return {"message": "Name, email and password are required"}, 400

    if User.query.filter_by(email=email).first():
        return {"message": "An account with this email already exists"}, 409

    user = User(
        full_name=name,
        email=email,
        password_hash=generate_password_hash(password),
        role=role.capitalize()
    )
    db.session.add(user)
    db.session.commit()

    token = generate_token(user.id)
    return {
        "message": "Registered successfully",
        "token": token,
        "user": {
            "id": user.id,
            "name": user.full_name,
            "email": user.email,
            "role": user.role
        }
    }, 201

@auth_bp.post("/login")
def login():
    data = request.json or {}
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email or not password:
        return {"message": "Email and password are required"}, 400

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return {"message": "Invalid email or password"}, 401

    token = generate_token(user.id)
    return {
        "token": token,
        "user": {
            "id": user.id,
            "name": user.full_name,
            "email": user.email,
            "role": user.role
        }
    }

@auth_bp.get("/me")
def me():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_id = verify_token(token)
    if not user_id:
        return {"message": "Not authenticated"}, 401
    user = User.query.get(user_id)
    if not user:
        return {"message": "User not found"}, 404
    return {
        "user": {
            "id": user.id,
            "name": user.full_name,
            "email": user.email,
            "role": user.role
        }
    }

@auth_bp.post("/logout")
def logout():
    return {"message": "Logged out"}