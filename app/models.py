from datetime import datetime
from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(255))
    role = db.Column(db.String(50), default="Citizen")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    category = db.Column(db.String(50))
    severity = db.Column(db.String(20))
    description = db.Column(db.Text)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80))
    name = db.Column(db.String(150))

class QuizQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_slug = db.Column(db.String(80))
    question = db.Column(db.Text)
    correct = db.Column(db.String(1))

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    location = db.Column(db.String(150))