from flask import Blueprint
from ..models import Incident

responder_bp = Blueprint("responder", __name__)

@responder_bp.get("/incidents")
def incidents():
    return {"incidents": [i.title for i in Incident.query.all()]}