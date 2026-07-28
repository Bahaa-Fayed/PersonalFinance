from flask import (
    render_template,
    redirect,
    url_for,
    flash,
)

from . import transactions_bp

from app.forms.transaction_form import TransactionForm
from app.services.account_service import AccountService
from app.services.category_service import CategoryService
from app.services.transaction_service import TransactionService


@transactions_bp.route("/transactions")
def index():

    transactions = TransactionService.get_all()

    return render_template(
        "transactions/index.html",
        transactions=transactions,
    )


@transactions_bp.route(
    "/transactions/new",
    methods=["GET", "POST"],
)
def new():

    form = TransactionForm()

    accounts = AccountService.get_all_accounts()

    account_choices = [
        (account.id, account.name)
        for account in accounts
    ]

    form.from_account.choices = account_choices
    form.to_account.choices = account_choices

    categories = CategoryService.get_all_categories()

    form.category_id.choices = [
        (0, "بدون فئة")
    ]

    for category in categories:

        form.category_id.choices.append(
            (
                category.id,
                category.name,
            )
        )

    if form.validate_on_submit():

        try:

            TransactionService.create(
                transaction_type=form.transaction_type.data,
                amount=form.amount.data,
                from_account_id=form.from_account.data,
                to_account_id=form.to_account.data,
                category_id=form.category_id.data
                if form.category_id.data != 0
                else None,
                description=form.description.data,
                transaction_date=form.transaction_date.data,
            )

            flash(
                "تم إنشاء الحركة بنجاح.",
                "success",
            )

            return redirect(
                url_for("transactions.index")
            )

        except ValueError as e:

            flash(str(e), "danger")

    return render_template(
        "transactions/new.html",
        form=form,
        categories=categories,
    )


@transactions_bp.route(
    "/transactions/<int:transaction_id>/edit",
    methods=["GET", "POST"],
)
def edit(transaction_id):

    transaction = TransactionService.get_by_id(
        transaction_id
    )

    if transaction is None:

        flash(
            "الحركة غير موجودة.",
            "danger",
        )

        return redirect(
            url_for("transactions.index")
        )

    form = TransactionForm(obj=transaction)

    accounts = AccountService.get_all_accounts()

    account_choices = [
        (account.id, account.name)
        for account in accounts
    ]

    form.from_account.choices = account_choices
    form.to_account.choices = account_choices

    categories = CategoryService.get_all_categories()

    form.category_id.choices = [
        (0, "بدون فئة")
    ]

    for category in categories:

        form.category_id.choices.append(
            (
                category.id,
                category.name,
            )
        )

    if form.validate_on_submit():

        try:

            TransactionService.update(
                transaction_id=transaction.id,
                transaction_type=form.transaction_type.data,
                amount=form.amount.data,
                from_account_id=form.from_account.data,
                to_account_id=form.to_account.data,
                category_id=form.category_id.data
                if form.category_id.data != 0
                else None,
                description=form.description.data,
                transaction_date=form.transaction_date.data,
            )

            flash(
                "تم تعديل الحركة بنجاح.",
                "success",
            )

            return redirect(
                url_for("transactions.index")
            )

        except ValueError as e:

            flash(str(e), "danger")

    return render_template(
        "transactions/new.html",
        form=form,
        edit_mode=True,
        categories=categories,
    )


@transactions_bp.route(
    "/transactions/<int:transaction_id>/delete",
    methods=["POST"],
)
def delete(transaction_id):

    try:

        TransactionService.delete(
            transaction_id
        )

        flash(
            "تم حذف الحركة بنجاح.",
            "success",
        )

    except ValueError as e:

        flash(
            str(e),
            "danger",
        )

    return redirect(
        url_for("transactions.index")
    )