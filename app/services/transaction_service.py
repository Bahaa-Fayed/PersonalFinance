from app.models import Transaction
from app.repositories.account_repository import AccountRepository
from app.repositories.transaction_repository import TransactionRepository
from app.services.account_service import AccountService


class TransactionService:

    @staticmethod
    def _apply_transaction(
        transaction_type,
        amount,
        from_account,
        to_account,
    ):

        if transaction_type == "income":

            AccountService.increase_balance(
                to_account,
                amount,
            )

        elif transaction_type == "expense":

            AccountService.decrease_balance(
                from_account,
                amount,
            )

        elif transaction_type == "transfer":

            AccountService.transfer_balance(
                from_account,
                to_account,
                amount,
            )

    @staticmethod
    def _reverse_transaction(transaction):

        if transaction.transaction_type == "income":

            account = AccountRepository.get_by_id(
                transaction.to_account_id
            )

            AccountService.decrease_balance(
                account,
                transaction.amount,
            )

        elif transaction.transaction_type == "expense":

            account = AccountRepository.get_by_id(
                transaction.from_account_id
            )

            AccountService.increase_balance(
                account,
                transaction.amount,
            )

        elif transaction.transaction_type == "transfer":

            from_account = AccountRepository.get_by_id(
                transaction.from_account_id
            )

            to_account = AccountRepository.get_by_id(
                transaction.to_account_id
            )

            AccountService.transfer_balance(
                to_account,
                from_account,
                transaction.amount,
            )

    @staticmethod
    def create(
        transaction_type,
        amount,
        from_account_id=None,
        to_account_id=None,
        category_id=None,
        description=None,
        transaction_date=None,
    ):

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than zero."
            )
        amount = float(amount)

        if transaction_type not in Transaction.TRANSACTION_TYPES:
            raise ValueError(
                "Invalid transaction type."
            )

        from_account = None
        to_account = None

        if from_account_id:

            from_account = AccountRepository.get_by_id(
                from_account_id
            )

            if from_account is None:

                raise ValueError(
                    "Source account not found."
                )

        if to_account_id:

            to_account = AccountRepository.get_by_id(
                to_account_id
            )

            if to_account is None:

                raise ValueError(
                    "Destination account not found."
                )

        if (
            transaction_type == "transfer"
            and from_account_id == to_account_id
        ):

            raise ValueError(
                "Source and destination accounts cannot be the same."
            )

        TransactionService._apply_transaction(
            transaction_type,
            amount,
            from_account,
            to_account,
        )

        transaction = Transaction(
            transaction_type=transaction_type,
            amount=amount,
            from_account_id=from_account_id,
            to_account_id=to_account_id,
            category_id=category_id,
            description=description,
            transaction_date=transaction_date,
        )

        return TransactionRepository.create(
            transaction
        )

    @staticmethod
    def update(
        transaction_id,
        transaction_type,
        amount,
        from_account_id=None,
        to_account_id=None,
        category_id=None,
        description=None,
        transaction_date=None,
    ):

        transaction = TransactionRepository.get_by_id(
            transaction_id
        )

        if transaction is None:

            raise ValueError(
                "Transaction not found."
            )

        TransactionService._reverse_transaction(
            transaction
        )

        from_account = None
        to_account = None

        if from_account_id:

            from_account = AccountRepository.get_by_id(
                from_account_id
            )

        if to_account_id:

            to_account = AccountRepository.get_by_id(
                to_account_id
            )
        amount = float(amount)
        TransactionService._apply_transaction(
            transaction_type,
            amount,
            from_account,
            to_account,
        )

        transaction.transaction_type = transaction_type
        transaction.amount = amount
        transaction.from_account_id = from_account_id
        transaction.to_account_id = to_account_id
        transaction.category_id = category_id
        transaction.description = description
        transaction.transaction_date = transaction_date

        TransactionRepository.update()

        return transaction

    @staticmethod
    def delete(transaction_id):

        transaction = TransactionRepository.get_by_id(
            transaction_id
        )

        if transaction is None:

            raise ValueError(
                "Transaction not found."
            )

        TransactionService._reverse_transaction(
            transaction
        )

        TransactionRepository.delete(
            transaction
        )

    @staticmethod
    def get_all():

        return TransactionRepository.get_all()

    @staticmethod
    def get_by_id(transaction_id):

        return TransactionRepository.get_by_id(
            transaction_id
        )