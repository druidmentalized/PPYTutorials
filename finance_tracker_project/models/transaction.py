from datetime import datetime

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
            amount=transaction_dict["amount"],
            date=transaction_dict["date"],
            category=transaction_dict["category"],
            description=transaction_dict["description"],
            transaction_type=transaction_dict["transaction_type"],
        )