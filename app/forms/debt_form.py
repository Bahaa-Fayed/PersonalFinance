from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    SelectField,
    DecimalField,
    DateField,
    TextAreaField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange,
    Optional
)


class DebtForm(FlaskForm):

    person_name = StringField(
        "اسم الشخص",
        validators=[
            DataRequired(),
            Length(max=150)
        ]
    )

    debt_type = SelectField(
        "نوع الدين",
        choices=[
            ("owed_to_me", "دين لي"),
            ("owed_by_me", "دين علي")
        ],
        validators=[
            DataRequired()
        ]
    )

    total_amount = DecimalField(
        "إجمالي الدين",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0.01)
        ]
    )

    paid_amount = DecimalField(
        "المبلغ المسدد",
        places=2,
        default=0,
        validators=[
            Optional(),
            NumberRange(min=0)
        ]
    )

    due_date = DateField(
        "تاريخ الاستحقاق",
        validators=[
            Optional()
        ]
    )

    notes = TextAreaField(
        "ملاحظات",
        validators=[
            Optional(),
            Length(max=1000)
        ]
    )

    submit = SubmitField(
        "حفظ"
    )