from app.models.debt import Debt
from app.repositories.debt_repository import DebtRepository


class DebtService:

    @staticmethod
    def get_all_debts():
        return DebtRepository.get_all()

    @staticmethod
    def get_debt(debt_id):
        return DebtRepository.get_by_id(
            debt_id
        )

    @staticmethod
    def create_debt(form):

        debt = Debt(
            person_name=form.person_name.data,
            debt_type=form.debt_type.data,
            total_amount=form.total_amount.data,
            paid_amount=form.paid_amount.data or 0,
            due_date=form.due_date.data,
            notes=form.notes.data
        )

        DebtService._update_status(
            debt
        )

        DebtRepository.create(
            debt
        )

        return debt

    @staticmethod
    def update_debt(
        debt_id,
        form
    ):

        debt = DebtRepository.get_by_id(
            debt_id
        )

        debt.person_name = (
            form.person_name.data
        )

        debt.debt_type = (
            form.debt_type.data
        )

        debt.total_amount = (
            form.total_amount.data
        )

        debt.paid_amount = (
            form.paid_amount.data
        )

        debt.due_date = (
            form.due_date.data
        )

        debt.notes = (
            form.notes.data
        )

        DebtService._update_status(
            debt
        )

        DebtRepository.update()

        return debt

    @staticmethod
    def delete_debt(
        debt_id
    ):

        debt = DebtRepository.get_by_id(
            debt_id
        )

        DebtRepository.delete(
            debt
        )

    @staticmethod
    def register_payment(
        debt_id,
        amount
    ):

        debt = DebtRepository.get_by_id(
            debt_id
        )

        if amount <= 0:
            return debt
        debt.paid_amount = round(
            debt.paid_amount + amount,
            2
        )

        if debt.paid_amount > debt.total_amount:
            debt.paid_amount = (
                debt.total_amount
            )

        DebtService._update_status(
            debt
        )

        DebtRepository.update()

        return debt

    @staticmethod
    def _update_status(
        debt
    ):

        if debt.remaining_amount <= 0:

            debt.status = "paid"

        else:

            debt.status = "open"