from flask import Blueprint
from ..models import Alert

alerts_bp = Blueprint("alerts", __name__)

@alerts_bp.get("")
def get_alerts():
    return {"alerts": [a.title for a in Alert.query.all()]}