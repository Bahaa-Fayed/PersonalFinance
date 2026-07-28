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
            current_balance=opening_balance,
        )

        return AccountRepository.create(account)

    @staticmethod
    def update_account(account_id, name, account_type, opening_balance):

        account = AccountRepository.get_by_id(account_id)

        if account is None:
            return None

        account.name = name
        account.account_type = account_type
        account.opening_balance = opening_balance

        AccountRepository.update()

        return account

    @staticmethod
    def delete_account(account_id):

        account = AccountRepository.get_by_id(account_id)

        if account is None:
            return False

        # لاحقًا سنمنع حذف الحساب إذا كانت له حركات مالية.
        AccountRepository.delete(account)

        return True

    @staticmethod
    def increase_balance(account, amount):
        account.current_balance += amount

    @staticmethod
    def decrease_balance(account, amount):
        account.current_balance -= amount

    @staticmethod
    def transfer_balance(from_account, to_account, amount):
        AccountService.decrease_balance(from_account, amount)
        AccountService.increase_balance(to_account, amount)