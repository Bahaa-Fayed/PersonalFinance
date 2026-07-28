from datetime import datetime

from app import db


class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    account_type = db.Column(db.String(50), nullable=False)
    currency = db.Column(db.String(10), default="EGP")
    color = db.Column(db.String(20), default="#0d6efd")
    icon = db.Column(db.String(50), default="wallet")
    opening_balance = db.Column(db.Float, default=0)
    current_balance = db.Column(db.Float, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    ACCOUNT_TYPES = {
        "cash": "💵 نقدي",
        "bank": "🏦 حساب بنكي",
        "wallet": "📱 محفظة إلكترونية",
        "credit": "💳 بطاقة ائتمان",
    }

    @property
    def account_type_label(self):
        return self.ACCOUNT_TYPES.get(
            self.account_type,
            self.account_type
        )

    @property
    def balance_text(self):
        return f"{self.current_balance:,.2f} ج.م"
