import os
from flask import Flask, render_template
from dotenv import load_dotenv
from .extensions import db
from . import models  # noqa: ensure models are registered with SQLAlchemy

def create_app():
    load_dotenv()

    app = Flask(__name__, template_folder="../templates")

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///temp.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        from .seed import seed_database
        seed_database()

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/health")
    def health():
        return {"status": "ok"}

    # register routes
    from .routes import auth, alerts, chat, courses, dashboard, admin, profile, responder, sos

    app.register_blueprint(auth.auth_bp, url_prefix="/api/auth")
    app.register_blueprint(alerts.alerts_bp, url_prefix="/api/alerts")
    app.register_blueprint(chat.chat_bp, url_prefix="/api/chat")
    app.register_blueprint(courses.courses_bp, url_prefix="/api/courses")
    app.register_blueprint(dashboard.dashboard_bp, url_prefix="/api/dashboard")
    app.register_blueprint(admin.admin_bp, url_prefix="/api/admin")
    app.register_blueprint(profile.profile_bp, url_prefix="/api/profile")
    app.register_blueprint(responder.responder_bp, url_prefix="/api/responder")
    app.register_blueprint(sos.sos_bp, url_prefix="/api/sos")

    return app