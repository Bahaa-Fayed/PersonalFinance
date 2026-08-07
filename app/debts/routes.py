from flask import (
    render_template,
    redirect,
    url_for,
    flash
)

from . import debts_bp

from app.forms.debt_form import DebtForm
from app.services.debt_service import DebtService


@debts_bp.route("/")
def index():

    debts = DebtService.get_all_debts()

    return render_template(
        "debts/index.html",
        debts=debts
    )


@debts_bp.route("/new", methods=["GET", "POST"])
def new():

    form = DebtForm()

    if form.validate_on_submit():

        DebtService.create_debt(
            form
        )

        flash(
            "تمت إضافة الدين بنجاح.",
            "success"
        )

        return redirect(
            url_for("debts.index")
        )

    return render_template(
        "debts/new.html",
        form=form,
        title="إضافة دين"
    )


@debts_bp.route(
    "/<int:debt_id>/edit",
    methods=["GET", "POST"]
)
def edit(debt_id):

    debt = DebtService.get_debt(
        debt_id
    )

    form = DebtForm(
        obj=debt
    )

    if form.validate_on_submit():

        DebtService.update_debt(
            debt_id,
            form
        )

        flash(
            "تم تحديث الدين بنجاح.",
            "success"
        )

        return redirect(
            url_for("debts.index")
        )

    return render_template(
        "debts/new.html",
        form=form,
        title="تعديل الدين"
    )


@debts_bp.route(
    "/<int:debt_id>/delete",
    methods=["POST"]
)
def delete(debt_id):

    DebtService.delete_debt(
        debt_id
    )

    flash(
        "تم حذف الدين.",
        "success"
    )

    return redirect(
        url_for("debts.index")
    )