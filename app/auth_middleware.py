from flask import request
from .auth_utils import verify_token

def require_auth():
    token = request.headers.get("Authorization")
    if not token:
        return None
    return verify_token(token)