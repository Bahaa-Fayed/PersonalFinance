from flask import Blueprint

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def dashboard():

    return """
    <h1>💰 Personal Finance Manager</h1>

    <hr>

    <h3>الإصدار 0.1.0</h3>

    <p>قاعدة البيانات تعمل بنجاح.</p>
    """
