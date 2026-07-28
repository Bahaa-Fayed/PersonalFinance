from datetime import date, datetime

from app import db


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    # الحساب المصدر (مصروف أو تحويل)
    from_account_id = db.Column(
        db.Integer,
        db.ForeignKey("accounts.id"),
        nullable=True
    )

    # الحساب الوجهة (دخل أو تحويل)
    to_account_id = db.Column(
        db.Integer,
        db.ForeignKey("accounts.id"),
        nullable=True
    )

    amount = db.Column(
        db.Float,
        nullable=False
    )

    TRANSACTION_TYPES = {
        "income": "Income",
        "expense": "Expense",
        "transfer": "Transfer",
    }

    transaction_type = db.Column(
        db.String(20),
        nullable=False
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=True
    )

    description = db.Column(
        db.Text
    )

    transaction_date = db.Column(
        db.Date,
        default=date.today,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    from_account = db.relationship(
        "Account",
        foreign_keys=[from_account_id],
        backref="outgoing_transactions"
    )

    to_account = db.relationship(
        "Account",
        foreign_keys=[to_account_id],
        backref="incoming_transactions"
    )
    category = db.relationship(
        "Category",
        backref="transactions"
    )

    def __repr__(self):
        return (
            f"<Transaction {self.id} "
            f"{self.transaction_type} "
            f"{self.amount}>"
        )
