from datetime import datetime

from finance_tracker_project.config.config import AMOUNT, DATE, CATEGORY, DESCRIPTION, TRANSACTION_TYPE, DATE_FORMAT
from finance_tracker_project.enums.category import Category
from finance_tracker_project.utils.json_serializable import JsonSerializable


class Transaction(JsonSerializable):
    def __init__(self, amount: float, date: datetime, category: Category, description: str, transaction_type: str):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description
        self.transaction_type = transaction_type

    def to_json(self):
        return {
            AMOUNT: self.serialize_value(self.amount),
            DATE: self.serialize_value(self.date),
            CATEGORY: self.serialize_value(self.category),
            DESCRIPTION: self.serialize_value(self.description),
            TRANSACTION_TYPE: self.serialize_value(self.transaction_type)
        }

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            amount=cls.deserialize_value(data[AMOUNT]),
            date=datetime.strptime(cls.deserialize_value(data[DATE]), DATE_FORMAT),
            category=Category(cls.deserialize_value(data[CATEGORY])),
            description=cls.deserialize_value(data[DESCRIPTION]),
            transaction_type=cls.deserialize_value(data[TRANSACTION_TYPE])
        )