import uuid

TOKENS = {}

def generate_token(user_id):
    token = str(uuid.uuid4())
    TOKENS[token] = user_id
    return token

def verify_token(token):
    return TOKENS.get(token)