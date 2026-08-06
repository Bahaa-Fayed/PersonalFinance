from sqlalchemy import func
from app import db
from app.models import Budget, Transaction
from app.repositories.budget_repository import BudgetRepository


class BudgetService:

    @staticmethod
    def get_all_budgets():

        return BudgetRepository.get_all()

    @staticmethod
    def get_budget(budget_id):

        return BudgetRepository.get_by_id(
            budget_id
        )

    @staticmethod
    def create_budget(
        category_id,
        amount,
        period,
        start_date,
        end_date,
    ):

        budget = Budget(
            category_id=category_id,
            amount=amount,
            period=period,
            start_date=start_date,
            end_date=end_date,
        )

        return BudgetRepository.create(
            budget
        )

    @staticmethod
    def update_budget(
        budget,
        category_id,
        amount,
        period,
        start_date,
        end_date,
    ):

        budget.category_id = category_id
        budget.amount = amount
        budget.period = period
        budget.start_date = start_date
        budget.end_date = end_date

        BudgetRepository.update()

        return budget

    @staticmethod
    def delete_budget(
        budget,
    ):

        BudgetRepository.delete(
            budget
        )

    @staticmethod
    def get_progress(
        budget,
    ):

        spent = (
            Transaction.query.with_entities(
                func.coalesce(
                    func.sum(
                        Transaction.amount
                    ),
                    0,
                )
            )
            .filter(
                Transaction.transaction_type == "expense",
                Transaction.category_id == budget.category_id,
                Transaction.transaction_date >= budget.start_date,
                Transaction.transaction_date <= budget.end_date,
            )
            .scalar()
        )

        remaining = budget.amount - spent

        percentage = (
            (spent / budget.amount) * 100
            if budget.amount > 0
            else 0
        )

        return {
            "spent": spent,
            "remaining": remaining,
            "percentage": round(
                percentage,
                2,
            ),
        }
    @staticmethod
    def get_spent_amount(budget):
        """
        حساب إجمالي المصروفات الخاصة بالميزانية.
        """

        spent = (
            db.session.query(
                func.coalesce(func.sum(Transaction.amount), 0)
            )
            .filter(
                Transaction.transaction_type == "expense",
                Transaction.category_id == budget.category_id,
                Transaction.transaction_date >= budget.start_date,
                Transaction.transaction_date <= budget.end_date,
            )
            .scalar()
        )

        return float(spent or 0)
        
    @staticmethod
    def get_progress(budget):
        """
        حساب نسبة استهلاك الميزانية.
        """

        spent = BudgetService.get_spent_amount(budget)

        amount = float(budget.amount or 0)

        if amount > 0:
            percentage = round((spent / amount) * 100, 1)
        else:
            percentage = 0

        remaining = amount - spent

        if percentage >= 100:
            color = "danger"
        elif percentage >= 80:
            color = "warning"
        elif percentage >= 50:
            color = "info"
        else:
            color = "success"

        return {
            "spent": spent,
            "remaining": remaining,
            "percentage": min(percentage, 100),
            "actual_percentage": percentage,
            "color": color,
            "is_warning": percentage >= 80,
            "is_over": percentage >= 100,
        }