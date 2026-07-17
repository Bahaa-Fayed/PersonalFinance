from flask import render_template

from . import accounts_bp


@accounts_bp.route("/accounts")
def index():
    return render_template("accounts/index.html")
