from flask import Blueprint
from ..models import User

admin_bp = Blueprint("admin", __name__)

@admin_bp.get("/overview")
def overview():
    return {"total_users": User.query.count()}