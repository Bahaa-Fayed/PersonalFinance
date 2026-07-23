from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DecimalField,
    SubmitField
)
from wtforms.validators import DataRequired, Length


class AccountForm(FlaskForm):

    name = StringField(
        "اسم الحساب",
        validators=[
            DataRequired(),
            Length(max=100)
        ]
    )

    account_type = SelectField(
        "نوع الحساب",
        choices=[
            ("cash", "نقدي"),
            ("bank", "حساب بنكي"),
            ("wallet", "محفظة إلكترونية"),
            ("credit", "بطاقة ائتمان")
        ],
        validators=[DataRequired()]
    )

    currency = SelectField(
        "العملة",
        choices=[
            ("EGP", "جنيه مصري"),
            ("USD", "دولار أمريكي"),
            ("EUR", "يورو")
        ],
        default="EGP"
    )

    opening_balance = DecimalField(
        "الرصيد الافتتاحي",
        default=0
    )

    submit = SubmitField("حفظ")
