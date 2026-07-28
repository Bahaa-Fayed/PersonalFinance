from datetime import datetime

from app import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    CATEGORY_TYPES = {
        "income": "Income",
        "expense": "Expense",
    }

    category_type = db.Column(
        db.String(20),
        nullable=False
    )

    color = db.Column(
        db.String(20),
        default="#0d6efd"
    )

    icon = db.Column(
        db.String(50),
        default="tag"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    @property
    def category_type_label(self):

        return self.CATEGORY_TYPES.get(
            self.category_type,
            self.category_type
        )

    def __repr__(self):

        return (
            f"<Category "
            f"{self.name}>"
        )
    @property
    def category_type_label(self):

        return {
            "income": "دخل",
           "expense": "مصروف",
       }.get(
            self.category_type,
            self.category_type
       )