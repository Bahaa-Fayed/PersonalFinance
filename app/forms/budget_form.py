from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DecimalField,
    DateField,
    SubmitField,
)
from wtforms.validators import DataRequired, NumberRange

from app.models.budget import Budget


class BudgetForm(FlaskForm):

    category_id = SelectField(
        "الفئة",
        coerce=int,
        validators=[DataRequired()],
    )

    amount = DecimalField(
        "قيمة الميزانية",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0.01),
        ],
    )

    period = SelectField(
        "الفترة",
        choices=[
            (key, value)
            for key, value in Budget.PERIODS.items()
        ],
        validators=[DataRequired()],
    )

    start_date = DateField(
        "تاريخ البداية",
        validators=[DataRequired()],
    )

    end_date = DateField(
        "تاريخ النهاية",
        validators=[DataRequired()],
    )

    submit = SubmitField("حفظ")