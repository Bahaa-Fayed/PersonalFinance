from app import db
from app.models import Transaction


class TransactionRepository:

    @staticmethod
    def get_all():
        return (
            Transaction.query
            .order_by(Transaction.transaction_date.desc())
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