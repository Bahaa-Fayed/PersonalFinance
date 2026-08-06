from datetime import date, datetime

from app import db


class Budget(db.Model):
    __tablename__ = "budgets"

    id = db.Column(db.Integer, primary_key=True)

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    amount = db.Column(db.Float, nullable=False)

    period = db.Column(
        db.String(20),
        nullable=False,
        default="monthly"
    )

    start_date = db.Column(
        db.Date,
        nullable=False,
        default=date.today
    )

    end_date = db.Column(
        db.Date,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    category = db.relationship(
        "Category",
        backref=db.backref(
            "budgets",
            lazy=True,
            cascade="all, delete-orphan"
        )
    )

    PERIODS = {
        "monthly": "شهري",
        "yearly": "سنوي",
        "custom": "مخصص",
    }

    @property
    def period_label(self):
        return self.PERIODS.get(self.period, self.period)
        
    @property
    def amount_text(self):
        return f"{self.amount:,.2f} ج.م"
    
    @property
    def spent_text(self):
        return f"{self.spent:,.2f} ج.م"

    @property
    def remaining_text(self):
        return f"{self.remaining:,.2f} ج.م"
    @property
    def spent(self):
        from app.services.budget_service import BudgetService

        return BudgetService.get_progress(
            self
        )["spent"]

    @property
    def remaining(self):
        from app.services.budget_service import BudgetService

        return BudgetService.get_progress(
            self
        )["remaining"]

    @property
    def percentage(self):
        from app.services.budget_service import BudgetService

        return BudgetService.get_progress(
            self
        )["percentage"]
    @property
    def start_date_text(self):

        if self.start_date:
            return self.start_date.strftime(
                "%d/%m/%Y"
            )

        return ""

    @property
    def end_date_text(self):

        if self.end_date:
            return self.end_date.strftime(
                "%d/%m/%Y"
            )

        return ""
    @property
    def progress_color(self):
        from app.services.budget_service import BudgetService

        return BudgetService.get_progress(
            self
        )["color"]


    @property
    def is_warning(self):
        from app.services.budget_service import BudgetService

        return BudgetService.get_progress(
            self
        )["is_warning"]


    @property
    def is_over(self):
        from app.services.budget_service import BudgetService

        return BudgetService.get_progress(
            self
        )["is_over"]