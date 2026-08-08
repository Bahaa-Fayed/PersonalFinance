from sqlalchemy import or_

from app import db
from app.models import Transaction
from app.models.account import Account
from app.models.category import Category


class TransactionRepository:

    @staticmethod
    def get_all():
        return (
            Transaction.query
            .order_by(
                Transaction.transaction_date.desc()
            )
            .all()
        )

    @staticmethod
    def get_by_id(transaction_id):
        return Transaction.query.get(transaction_id)

    @staticmethod
    def create(transaction):
        db.session.add(transaction)
        db.session.commit()
        return transaction

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(transaction):
        db.session.delete(transaction)
        db.session.commit()

    @staticmethod
    def search(
        query=None,
        date_from=None,
        date_to=None,
        transaction_type=None
    ):
        """
        البحث في العمليات.
        """

        filters = []

        if query:
            search = f"%{query}%"

            filters.append(
                or_(
                    Transaction.description.ilike(search),

                    Transaction.category.has(
                        Category.name.ilike(search)
                    ),

                    Transaction.from_account.has(
                        Account.name.ilike(search)
                    ),

                    Transaction.to_account.has(
                        Account.name.ilike(search)
                    )
                )
            )

        if date_from:
            filters.append(
                Transaction.transaction_date >= date_from
            )

        if date_to:
            filters.append(
                Transaction.transaction_date <= date_to
            )

        if transaction_type:
            filters.append(
                Transaction.transaction_type
                == transaction_type
            )

        return (
            Transaction.query
            .filter(*filters)
            .order_by(
                Transaction.transaction_date.desc()
            )
            .all()
        )