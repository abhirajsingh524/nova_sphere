from flask import Blueprint
from datetime import datetime

sos_bp = Blueprint("sos", __name__)

@sos_bp.post("")
def sos():
    return {"status": "sent", "time": datetime.utcnow().isoformat()}