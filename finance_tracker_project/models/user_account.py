from datetime import datetime
from typing import Optional

from finance_tracker_project.config.config import LOGIN, PASSWORD_HASH, REGISTRATION_DATE, BANK_ACCOUNTS, DATE_FORMAT
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.utils.json_serializable import JsonSerializable


class UserAccount(JsonSerializable):
    def __init__(
            self,
            username: str,
            password_hash: str,
            registration_date: Optional[datetime] = None,
            bank_accounts: Optional[list[BankAccount]] = None
    ):
        self.username = username
        self.password_hash = password_hash
        self.registration_date = registration_date if registration_date else datetime.now()
        self.bank_accounts = bank_accounts if bank_accounts else []

    def to_json(self) -> dict:
        return {
            LOGIN: self.serialize_value(self.username),
            PASSWORD_HASH: self.serialize_value(self.password_hash),
            REGISTRATION_DATE: self.serialize_value(self.registration_date),
            BANK_ACCOUNTS: self.serialize_value(self.bank_accounts)
        }

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            username=cls.deserialize_value(data[LOGIN]),
            password_hash=cls.deserialize_value(data[PASSWORD_HASH]),
            registration_date=datetime.strptime(cls.deserialize_value(data[REGISTRATION_DATE]), DATE_FORMAT),
            bank_accounts=[BankAccount.from_json(bank_acc) for bank_acc in cls.deserialize_value(data).get(BANK_ACCOUNTS, [])]
        )
