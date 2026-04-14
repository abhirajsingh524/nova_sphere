from flask import Blueprint, request

chat_bp = Blueprint("chat", __name__)

@chat_bp.post("/message")
def chat():
    msg = request.json.get("message", "")
    return {"reply": f"Guidance: {msg}"}