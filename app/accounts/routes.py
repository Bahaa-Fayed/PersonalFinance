from flask import render_template, redirect, url_for, flash

from . import accounts_bp

from app.services.account_service import AccountService
from app.forms.account_form import AccountForm


@accounts_bp.route("/accounts")
def index():

    accounts = AccountService.get_all_accounts()

    return render_template(
        "accounts/index.html",
        accounts=accounts
    )


@accounts_bp.route("/accounts/new", methods=["GET", "POST"])
def new():

    form = AccountForm()

    if form.validate_on_submit():

        AccountService.create_account(
            name=form.name.data,
            account_type=form.account_type.data,
            opening_balance=form.opening_balance.data
        )

        flash("تم إنشاء الحساب بنجاح.", "success")

        return redirect(url_for("accounts.index"))

    return render_template(
        "accounts/new.html",
        form=form
    )


@accounts_bp.route("/accounts/<int:account_id>/edit", methods=["GET", "POST"])
def edit(account_id):

    account = AccountService.get_account(account_id)

    if account is None:
        flash("الحساب غير موجود.", "danger")
        return redirect(url_for("accounts.index"))

    form = AccountForm(obj=account)

    if form.validate_on_submit():

        AccountService.update_account(
            account_id=account.id,
            name=form.name.data,
            account_type=form.account_type.data,
            opening_balance=form.opening_balance.data
        )

        flash("تم تعديل الحساب بنجاح.", "success")

        return redirect(url_for("accounts.index"))

    return render_template(
        "accounts/new.html",
        form=form,
        edit_mode=True
    )
@accounts_bp.route("/accounts/<int:account_id>/delete", methods=["POST"])
def delete(account_id):

    if AccountService.delete_account(account_id):

        flash("تم حذف الحساب بنجاح.", "success")

    else:

        flash("الحساب غير موجود.", "danger")

    return redirect(url_for("accounts.index"))
