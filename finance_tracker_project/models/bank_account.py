from datetime import datetime

from finance_tracker_project.config.config import ACCOUNT_NAME, CURRENCY, TRANSACTIONS, BALANCE, CREATION_DATE
from finance_tracker_project.enums.currency import Currency
from finance_tracker_project.models.transaction import Transaction
from finance_tracker_project.utils.json_serializable import JsonSerializable


class BankAccount(JsonSerializable):

    def __init__(self, name: str, currency: Currency, balance: float, transactions: list[Transaction]):
        self.name = name
        self.currency = currency
        self.balance = balance
        self.transactions = transactions
        self.creation_date = datetime.now()

    def to_json(self) -> dict:
        return {
            ACCOUNT_NAME: self.serialize_value(self.name),
            CURRENCY: self.serialize_value(self.currency),
            BALANCE: self.serialize_value(self.balance),
            TRANSACTIONS: self.serialize_value(self.transactions),
            CREATION_DATE: self.serialize_value(self.creation_date)
        }

    @classmethod
    def from_json(cls, data: dict):
        currency_data = cls.deserialize_value(data[CURRENCY])
        currency = next(
            (c for c in Currency if [c.code, c.symbol] == currency_data),
            None
        )
        if currency is None:
            raise ValueError(f"{currency_data} is not a valid Currency")

        return cls(
            name=cls.deserialize_value(data[ACCOUNT_NAME]),
            currency=currency,
            balance=cls.deserialize_value(data[BALANCE]),
            transactions=[Transaction.from_json(t) for t in cls.deserialize_value(data).get(TRANSACTIONS, [])],
        )