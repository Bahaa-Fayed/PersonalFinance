from flask import render_template

from . import budgets_bp


@budgets_bp.route("/budgets")
def index():
    return render_template("budgets/index.html")
