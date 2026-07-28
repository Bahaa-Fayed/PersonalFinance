from flask_wtf import FlaskForm

from wtforms import (
    SelectField,
    DecimalField,
    StringField,
    DateField,
    SubmitField,
)

from wtforms.validators import (
    DataRequired,
    NumberRange,
    Optional,
)


class TransactionForm(FlaskForm):

    transaction_type = SelectField(
        "نوع الحركة",
        choices=[
            ("income", "دخل"),
            ("expense", "مصروف"),
            ("transfer", "تحويل"),
        ],
        validators=[DataRequired()],
    )

    amount = DecimalField(
        "المبلغ",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0.01),
        ],
    )

    from_account = SelectField(
        "من حساب",
        choices=[],
        coerce=int,
        validators=[Optional()],
    )

    to_account = SelectField(
        "إلى حساب",
        choices=[],
        coerce=int,
        validators=[Optional()],
    )

    category_id = SelectField(
        "الفئة",
        coerce=int,
        choices=[]
    )

    description = StringField(
        "الوصف",
        validators=[Optional()],
    )

    transaction_date = DateField(
        "تاريخ الحركة",
        format="%Y-%m-%d",
        validators=[DataRequired()],
    )

    submit = SubmitField("حفظ")