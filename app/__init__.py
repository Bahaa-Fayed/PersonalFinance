from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)

    # استيراد النماذج حتى يتم تسجيلها في SQLAlchemy
    from app.models import Account

    # تسجيل الـ Blueprints
    from app.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp)

    # إنشاء الجداول إذا لم تكن موجودة
    with app.app_context():
        db.create_all()

    return app
