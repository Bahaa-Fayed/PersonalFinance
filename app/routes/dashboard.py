from flask import Blueprint

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def home():
    return """
    <h1>Personal Finance Manager</h1>
    <p>Version 0.1.0</p>
    """
