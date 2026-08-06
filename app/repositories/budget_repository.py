from app import db
from app.models.budget import Budget


class BudgetRepository:

    @staticmethod
    def get_all():
        return Budget.query.order_by(Budget.start_date.desc()).all()

    @staticmethod
    def get_by_id(budget_id):
        return Budget.query.get(budget_id)

    @staticmethod
    def create(budget):
        db.session.add(budget)
        db.session.commit()
        return budget

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(budget):
        db.session.delete(budget)
        db.session.commit()