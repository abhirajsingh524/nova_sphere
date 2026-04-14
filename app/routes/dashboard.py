from flask import Blueprint
from ..models import User

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.get("/summary")
def summary():
    return {"users": User.query.count()}