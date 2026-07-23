from app.models.account import Account
from app import db


class AccountRepository:

    @staticmethod
    def get_all():
        return Account.query.order_by(Account.name).all()

    @staticmethod
    def get_by_id(account_id):
        return Account.query.get(account_id)

    @staticmethod
    def create(account):
        db.session.add(account)
        db.session.commit()
        return account

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(account):
        db.session.delete(account)
        db.session.commit()
