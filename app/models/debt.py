from datetime import datetime

from app import db


class Debt(db.Model):
    __tablename__ = "debts"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    person_name = db.Column(
        db.String(150),
        nullable=False
    )

    debt_type = db.Column(
        db.String(20),
        nullable=False
    )

    total_amount = db.Column(
        db.Float,
        nullable=False
    )

    paid_amount = db.Column(
        db.Float,
        nullable=False,
        default=0
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="open"
    )

    due_date = db.Column(
        db.Date
    )

    notes = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    DEBT_TYPES = {
        "owed_to_me": "لي",
        "owed_by_me": "علي"
    }

    STATUS = {
        "open": "مفتوح",
        "paid": "مسدد"
    }

    @property
    def debt_type_label(self):
        return self.DEBT_TYPES.get(
            self.debt_type,
            self.debt_type
        )

    @property
    def status_label(self):
        return self.STATUS.get(
            self.status,
            self.status
        )

    @property
    def remaining_amount(self):
        return max(
            self.total_amount - self.paid_amount,
            0
        )

    @property
    def total_amount_text(self):
        return (
            f"{self.total_amount:,.2f} ج.م"
        )

    @property
    def paid_amount_text(self):
        return (
            f"{self.paid_amount:,.2f} ج.م"
        )

    @property
    def remaining_amount_text(self):
        return (
            f"{self.remaining_amount:,.2f} ج.م"
        )

    @property
    def due_date_text(self):

        if self.due_date:
            return self.due_date.strftime(
                "%d/%m/%Y"
            )

        return ""