from flask import render_template

from . import settings_bp


@settings_bp.route("/settings")
def index():
    return render_template("settings/index.html")
