from sqlalchemy import func

from app import db
from app.models.account import Account
from app.models.category import Category
from app.models.transaction import Transaction


class ReportRepository:
    """
    Repository المسؤول عن استعلامات التقارير.
    """

    @staticmethod
    def get_total_income():
        """
        إجمالي الدخل.
        """
        return (
            db.session.query(
                func.coalesce(func.sum(Transaction.amount), 0)
            )
            .filter(
                Transaction.transaction_type == "income"
            )
            .scalar()
        )

    @staticmethod
    def get_total_expenses():
        """
        إجمالي المصروفات.
        """
        return (
            db.session.query(
                func.coalesce(func.sum(Transaction.amount), 0)
            )
            .filter(
                Transaction.transaction_type == "expense"
            )
            .scalar()
        )

    @staticmethod
    def get_transaction_count():
        """
        عدد العمليات.
        """
        return Transaction.query.count()

    @staticmethod
    def get_account_balances():
        """
        جميع الحسابات مرتبة بالاسم.
        """
        return (
            Account.query
            .order_by(Account.name)
            .all()
        )

    @staticmethod
    def get_expenses_by_category():
        """
        إجمالي المصروفات لكل فئة.
        """

        return (
            db.session.query(
                Category.name.label("category"),
                func.coalesce(
                    func.sum(Transaction.amount),
                    0
                ).label("total")
            )
            .join(
                Transaction,
                Transaction.category_id == Category.id
            )
            .filter(
                Transaction.transaction_type == "expense"
            )
            .group_by(
                Category.id,
                Category.name
            )
            .order_by(
                func.sum(Transaction.amount).desc()
            )
            .all()
        )
    @staticmethod
    def get_income_by_category():
        """
        إجمالي الدخل لكل فئة.
        """

        return (
            db.session.query(
                Category.name.label("category"),
                func.coalesce(
                    func.sum(Transaction.amount),
                    0
                ).label("total")
            )
            .join(
                Transaction,
                Transaction.category_id == Category.id
            )
            .filter(
                Transaction.transaction_type == "income"
            )
            .group_by(
                Category.id,
                Category.name
            )
            .order_by(
                func.sum(Transaction.amount).desc()
            )
            .all()
        )
        
    @staticmethod
    def get_transfers():
        """
        جميع التحويلات بين الحسابات.
        """

        return (
            Transaction.query
            .filter(
                Transaction.transaction_type == "transfer"
            )
            .order_by(
                Transaction.transaction_date.desc()
            )
            .all()
        )