from flask import Blueprint
from ..models import Course

courses_bp = Blueprint("courses", __name__)

@courses_bp.get("")
def courses():
    return {"courses": [c.name for c in Course.query.all()]}