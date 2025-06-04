from finance_tracker_project.config.config import ACCOUNT_NAME, CURRENCY, TRANSACTIONS, BALANCE
from finance_tracker_project.enums.currency import Currency
from finance_tracker_project.models.transaction import Transaction


class BankAccount:

    def __init__(self, name: str, currency: Currency, balance: float, transactions: list[Transaction]):
        self.name = name
        self.currency = currency
        self.balance = balance
        self.transactions = transactions

    @staticmethod
    def from_dict(bank_dict: dict) -> "BankAccount":
        return BankAccount(
            name=bank_dict[ACCOUNT_NAME],
            currency=Currency(bank_dict[CURRENCY]),
            balance=bank_dict[BALANCE],
            transactions=[Transaction.from_dict(t) for t in bank_dict.get(TRANSACTIONS, [])],
        )

    @staticmethod
    def to_dict(bank_account: "BankAccount") -> dict:
        return {
            ACCOUNT_NAME: bank_account.name,
            CURRENCY: bank_account.currency,
            BALANCE: bank_account.balance,
            TRANSACTIONS: [Transaction.to_dict(transaction) for transaction in bank_account.transactions],
        }