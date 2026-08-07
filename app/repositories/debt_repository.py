from app import db
from app.models.debt import Debt


class DebtRepository:

    @staticmethod
    def get_all():
        return (
            Debt.query
            .order_by(Debt.created_at.desc())
            .all()
        )

    @staticmethod
    def get_by_id(debt_id):
        return Debt.query.get_or_404(
            debt_id
        )

    @staticmethod
    def create(debt):
        db.session.add(debt)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(debt):
        db.session.delete(debt)
        db.session.commit()