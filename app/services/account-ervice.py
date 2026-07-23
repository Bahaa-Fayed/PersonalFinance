from app.models.account import Account
from app.repositories.account_repository import AccountRepository


class AccountService:

    @staticmethod
    def get_all_accounts():
        return AccountRepository.get_all()

    @staticmethod
    def get_account(account_id):
        return AccountRepository.get_by_id(account_id)

    @staticmethod
    def create_account(name, account_type, opening_balance):

        account = Account(
            name=name,
            account_type=account_type,
            currency="EGP",
            opening_balance=opening_balance,
            current_balance=opening_balance
        )

        return AccountRepository.create(account)

    @staticmethod
    def update_account():
        return AccountRepository.update()

    @staticmethod
    def delete_account(account):
        return AccountRepository.delete(account)
