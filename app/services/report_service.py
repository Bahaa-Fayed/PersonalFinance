from app.repositories.report_repository import ReportRepository


class ReportService:
    """
    Service المسؤول عن تجهيز بيانات التقارير.
    """

    @staticmethod
    def get_summary():
        """
        ملخص مالي عام.
        """

        income = float(
            ReportRepository.get_total_income() or 0
        )

        expenses = float(
            ReportRepository.get_total_expenses() or 0
        )

        balance = income - expenses

        transactions = (
            ReportRepository.get_transaction_count()
        )

        return {
            "income": income,
            "expenses": expenses,
            "balance": balance,
            "transactions": transactions,
            "income_text": f"{income:,.2f} ج.م",
            "expenses_text": f"{expenses:,.2f} ج.م",
            "balance_text": f"{balance:,.2f} ج.م",
        }

    @staticmethod
    def get_account_balances():
        """
        الحصول على الحسابات مع أرصدتها.
        """

        return (
            ReportRepository
            .get_account_balances()
        )

    @staticmethod
    def get_expenses_by_category():
        """
        تجهيز تقرير المصروفات حسب الفئة.
        """

        categories = (
            ReportRepository
            .get_expenses_by_category()
        )

        result = []

        for item in categories:

            result.append({
                "category": item.category,
                "total": float(item.total),
                "total_text": (
                    f"{float(item.total):,.2f} ج.م"
                )
            })

        return result
    @staticmethod
    def get_income_by_category():
        """
        تجهيز تقرير الدخل حسب الفئة.
        """
    
        categories = (
            ReportRepository
            .get_income_by_category()
        )
    
        result = []
    
        for item in categories:
    
            result.append({
                "category": item.category,
                "total": float(item.total),
                "total_text": (
                    f"{float(item.total):,.2f} ج.م"
                )
            })
    
        return result
    @staticmethod
    def get_transfers():
        """
        الحصول على جميع التحويلات بين الحسابات.
        """
    
        transfers = (
            ReportRepository
            .get_transfers()
        )
    
        result = []
    
        total = 0
    
        for transfer in transfers:
    
            amount = float(
                transfer.amount or 0
            )
    
            total += amount
    
            result.append({
                "from_account": (
                    transfer.from_account.name
                    if transfer.from_account
                    else "-"
                ),
                "to_account": (
                    transfer.to_account.name
                    if transfer.to_account
                    else "-"
                ),
                "amount": amount,
                "amount_text": (
                    f"{amount:,.2f} ج.م"
                ),
                "date": transfer.transaction_date,
                "date_text": (
                    transfer.transaction_date.strftime(
                        "%d/%m/%Y"
                    )
                    if transfer.transaction_date
                    else ""
                ),
                "description": (
                    transfer.description or ""
                )
            })
    
        return {
            "count": len(result),
            "total": total,
            "total_text": (
                f"{total:,.2f} ج.م"
            ),
            "transfers": result
        }
    @staticmethod
    def get_report_data():
        """
        تجهيز جميع بيانات صفحة التقارير.
        """
    
        return {
            "summary": ReportService.get_summary(),
            "accounts": (
                ReportService.get_account_balances()
            ),
            "income_categories": (
                ReportService.get_income_by_category()
            ),
            "expense_categories": (
                ReportService.get_expenses_by_category()
            ),
            "transfers": (
                ReportService.get_transfers()
            ),
        }