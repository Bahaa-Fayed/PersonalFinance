from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from app.forms.budget_form import BudgetForm
from app.services.budget_service import BudgetService
from app.services.category_service import CategoryService
from . import budgets_bp
@budgets_bp.route("/budgets")
def index():



    budgets = BudgetService.get_all_budgets()

    return render_template(
        "budgets/index.html",
        budgets=budgets,
    )
@budgets_bp.route("/new", methods=["GET", "POST"])
def new():

    form = BudgetForm()

    form.category_id.choices = [
        (c.id, c.name)
        for c in CategoryService.get_all_categories()
    ]

    if form.validate_on_submit():

        BudgetService.create_budget(
            category_id=form.category_id.data,
            amount=float(form.amount.data),
            period=form.period.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
        )

        flash(
            "تم إنشاء الميزانية بنجاح.",
            "success",
        )

        return redirect(
            url_for("budgets.index")
        )

    return render_template(
        "budgets/new.html",
        form=form,
    )
@budgets_bp.route(
    "/<int:budget_id>/edit",
    methods=["GET", "POST"],
)
def edit(budget_id):

    budget = BudgetService.get_budget(
        budget_id
    )

    if budget is None:

        flash(
            "الميزانية غير موجودة.",
            "danger",
        )

        return redirect(
            url_for("budgets.index")
        )

    form = BudgetForm(obj=budget)

    form.category_id.choices = [
        (c.id, c.name)
        for c in CategoryService.get_all_categories()
    ]

    if form.validate_on_submit():

        BudgetService.update_budget(
            budget,
            category_id=form.category_id.data,
            amount=float(form.amount.data),
            period=form.period.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
        )

        flash(
            "تم تحديث الميزانية.",
            "success",
        )

        return redirect(
            url_for("budgets.index")
        )

    return render_template(
        "budgets/edit.html",
        form=form,
        budget=budget,
    )
@budgets_bp.route(
    "/<int:budget_id>/delete",
    methods=["POST"],
)
def delete(budget_id):

    budget = BudgetService.get_budget(
        budget_id
    )

    if budget is None:

        flash(
            "الميزانية غير موجودة.",
            "danger",
        )

    else:

        BudgetService.delete_budget(
            budget
        )

        flash(
            "تم حذف الميزانية.",
            "success",
        )

    return redirect(
        url_for("budgets.index")
    )
