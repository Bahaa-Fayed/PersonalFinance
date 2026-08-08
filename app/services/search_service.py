from datetime import datetime

from app.repositories.transaction_repository import (
    TransactionRepository
)


class SearchService:
    """
    Service المسؤول عن البحث في العمليات.
    """

    @staticmethod
    def search_transactions(
        query=None,
        date_from=None,
        date_to=None,
        transaction_type=None
    ):
        """
        البحث في العمليات مع دعم الفترة الزمنية.
        """

        # تنظيف كلمة البحث
        if query:
            query = query.strip()

            if not query:
                query = None

        # تحويل تاريخ البداية
        date_from = SearchService._parse_date(
            date_from
        )

        # تحويل تاريخ النهاية
        date_to = SearchService._parse_date(
            date_to
        )

        # التحقق من الفترة الزمنية
        if date_from and date_to:
            if date_from > date_to:
                raise ValueError(
                    "تاريخ البداية يجب أن يكون "
                    "قبل تاريخ النهاية."
                )

        return TransactionRepository.search(
            query=query,
            date_from=date_from,
            date_to=date_to,
            transaction_type=transaction_type
        )

    @staticmethod
    def _parse_date(value):
        """
        تحويل التاريخ من نص إلى date.
        """

        if not value:
            return None

        if hasattr(value, "year"):
            return value

        try:
            return datetime.strptime(
                value,
                "%Y-%m-%d"
            ).date()

        except (ValueError, TypeError):
            raise ValueError(
                "صيغة التاريخ غير صحيحة."
            )