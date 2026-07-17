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
    from app.accounts import accounts_bp
    from app.transactions import transactions_bp
    from app.budgets import budgets_bp
    from app.reports import reports_bp
    from app.settings import settings_bp
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(accounts_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(budgets_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(settings_bp)
    # إنشاء الجداول إذا لم تكن موجودة
    with app.app_context():
        db.create_all()

    return app
