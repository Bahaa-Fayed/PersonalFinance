from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    SelectField,
    SubmitField,
)

from wtforms.validators import (
    DataRequired,
    Length,
)


class CategoryForm(FlaskForm):

    name = StringField(
        "اسم الفئة",
        validators=[
            DataRequired(),
            Length(min=2, max=100),
        ],
    )

    category_type = SelectField(
        "نوع الفئة",
        choices=[
            ("income", "دخل"),
            ("expense", "مصروف"),
        ],
        validators=[
            DataRequired(),
        ],
    )

    submit = SubmitField(
        "حفظ"
    )