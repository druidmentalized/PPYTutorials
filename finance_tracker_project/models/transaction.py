from datetime import datetime

from finance_tracker_project.config.config import AMOUNT, DATE, CATEGORY, DESCRIPTION, TRANSACTION_TYPE, DATE_FORMAT
from finance_tracker_project.enums.category import Category


class Transaction:
    def __init__(self, amount: float, date: datetime, category: Category, description: str, transaction_type: str):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description
        self.transaction_type = transaction_type

    @staticmethod
    def from_dict(transaction_dict: dict) -> "Transaction":
        return Transaction(
            amount=transaction_dict[AMOUNT],
            date=datetime.strptime(transaction_dict[DATE], DATE_FORMAT),
            category=Category(transaction_dict[CATEGORY]),
            description=transaction_dict[DESCRIPTION],
            transaction_type=transaction_dict[TRANSACTION_TYPE],
        )

    @staticmethod
    def to_dict(transaction: "Transaction") -> dict:
        return {
            AMOUNT: transaction.amount,
            DATE: transaction.date.strftime(DATE_FORMAT),
            CATEGORY: transaction.category.value,
            DESCRIPTION: transaction.description,
            TRANSACTION_TYPE: transaction.transaction_type,
        }