from flask import render_template

from . import transactions_bp


@transactions_bp.route("/transactions")
def index():
    return render_template("transactions/index.html")
