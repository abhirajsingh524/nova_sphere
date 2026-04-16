from .extensions import db
from .models import User
from werkzeug.security import generate_password_hash

def seed_database():
    if User.query.first():
        return

    user = User(
        full_name="Arpit Singh",
        email="arpit@example.com",
        password_hash=generate_password_hash("password123")
    )
    user1 =User(
        full_name="om jaiswal",
        email="om@example.com",
        password_hash=generate_password_hash("password123")
    )

    db.session.add(user)
    db.session.add(user1)
    db.session.commit()