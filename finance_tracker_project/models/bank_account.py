from finance_tracker_project.enums.currency import Currency
from finance_tracker_project.models.transaction import Transaction


class BankAccount:

    def __init__(self, name: str, currency: Currency, transactions: list[Transaction]):
        self.name = name
        self.currency = currency
        self.transactions = transactions

    @staticmethod
    def from_dict(bank_dict: dict) -> "BankAccount":
        return BankAccount(
            name=bank_dict["name"],
            currency=Currency([bank_dict["currency"]]),
            transactions=[Transaction.from_dict(t) for t in bank_dict.get("transactions", [])],
        )