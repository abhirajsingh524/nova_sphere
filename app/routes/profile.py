from flask import Blueprint
from ..models import User
from ..auth_middleware import require_auth

profile_bp = Blueprint("profile", __name__)

@profile_bp.get("/me")
def me():
    user_id = require_auth()
    if not user_id:
        return {"error": "Unauthorized"}, 401

    user = User.query.get(user_id)
    return {"name": user.full_name}