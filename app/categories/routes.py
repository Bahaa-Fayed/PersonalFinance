from flask import (
    render_template,
    redirect,
    url_for,
    flash,
)

from . import categories_bp

from app.forms.category_form import CategoryForm
from app.services.category_service import CategoryService


@categories_bp.route("/categories")
def index():

    categories = (
        CategoryService.get_all_categories()
    )

    return render_template(
        "categories/index.html",
        categories=categories,
    )


@categories_bp.route(
    "/categories/new",
    methods=["GET", "POST"],
)
def new():
    
    form = CategoryForm()

    if form.validate_on_submit():

        try:

            CategoryService.create_category(
                name=form.name.data,
                category_type=form.category_type.data,
            )

            flash(
                "تم إنشاء الفئة بنجاح.",
                "success",
            )

            return redirect(
                url_for("categories.index")
            )

        except ValueError as e:

            flash(
                str(e),
                "danger",
            )

    return render_template(
        "categories/new.html",
        form=form,
    )


@categories_bp.route(
    "/categories/<int:category_id>/edit",
    methods=["GET", "POST"],
)
def edit(category_id):

    category = CategoryService.get_category(
        category_id
    )

    if category is None:

        flash(
            "الفئة غير موجودة.",
            "danger",
        )

        return redirect(
            url_for("categories.index")
        )

    form = CategoryForm(obj=category)

    if form.validate_on_submit():

        try:

            CategoryService.update_category(
                category_id=category.id,
                name=form.name.data,
                category_type=form.category_type.data,
            )

            flash(
                "تم تعديل الفئة بنجاح.",
                "success",
            )

            return redirect(
                url_for("categories.index")
            )

        except ValueError as e:

            flash(
                str(e),
                "danger",
            )

    return render_template(
        "categories/new.html",
        form=form,
        edit_mode=True,
    )


@categories_bp.route(
    "/categories/<int:category_id>/delete",
    methods=["POST"],
)
def delete(category_id):

    if CategoryService.delete_category(
        category_id
    ):

        flash(
            "تم حذف الفئة بنجاح.",
            "success",
        )

    else:

        flash(
            "الفئة غير موجودة.",
            "danger",
        )

    return redirect(
        url_for("categories.index")
    )