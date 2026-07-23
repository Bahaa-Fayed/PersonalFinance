#!/data/data/com.termux/files/usr/bin/bash

cat >> app/accounts/routes.py <<'EOF'


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
EOF

echo "✅ تمت إضافة Route الخاصة بالتعديل."
