from finance_tracker_project.config.config import ACCOUNT_NAME, CURRENCY, TRANSACTIONS, BALANCE
from finance_tracker_project.enums.currency import Currency
from finance_tracker_project.models.transaction import Transaction
from finance_tracker_project.utils.json_serializable import JsonSerializable


class BankAccount(JsonSerializable):

    def __init__(self, name: str, currency: Currency, balance: float, transactions: list[Transaction]):
        self.name = name
        self.currency = currency
        self.balance = balance
        self.transactions = transactions

    def to_json(self) -> dict:
        return {
            ACCOUNT_NAME: self.serialize_value(self.name),
            CURRENCY: self.serialize_value(self.currency),
            BALANCE: self.serialize_value(self.balance),
            TRANSACTIONS: self.serialize_value(self.transactions),
        }

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            name=cls.deserialize_value(data[ACCOUNT_NAME]),
            currency=Currency(cls.deserialize_value(data[CURRENCY])),
            balance=cls.deserialize_value(data[BALANCE]),
            transactions=[Transaction.from_json(t) for t in cls.deserialize_value(data).get(TRANSACTIONS, [])],
        )