from flask import Blueprint

debts_bp = Blueprint(
    "debts",
    __name__,
    url_prefix="/debts"
)

from . import routes