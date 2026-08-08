from flask import render_template, request

from . import search_bp
from app.services.search_service import SearchService


@search_bp.route("/")
def index():
    """
    صفحة البحث.
    """

    query = request.args.get(
        "q",
        ""
    ).strip()

    date_from = request.args.get(
        "date_from",
        ""
    )

    date_to = request.args.get(
        "date_to",
        ""
    )

    transaction_type = request.args.get(
        "transaction_type",
        ""
    )

    error = None
    transactions = []

    try:

        if any([
            query,
            date_from,
            date_to,
            transaction_type
        ]):

            transactions = (
                SearchService.search_transactions(
                    query=query,
                    date_from=date_from,
                    date_to=date_to,
                    transaction_type=(
                        transaction_type
                        or None
                    )
                )
            )

    except ValueError as e:

        error = str(e)

    return render_template(
        "search/index.html",
        transactions=transactions,
        query=query,
        date_from=date_from,
        date_to=date_to,
        transaction_type=transaction_type,
        error=error
    )