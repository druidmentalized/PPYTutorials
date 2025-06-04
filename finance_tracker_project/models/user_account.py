from datetime import datetime
from typing import Optional

from finance_tracker_project.config.config import LOGIN, PASSWORD_HASH, REGISTRATION_DATE, BANK_ACCOUNTS, DATE_FORMAT
from finance_tracker_project.models.bank_account import BankAccount


class UserAccount:

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

    @staticmethod
    def from_dict(user_dict: dict) -> "UserAccount":
        return UserAccount(
            username=user_dict[LOGIN],
            password_hash=user_dict[PASSWORD_HASH],
            registration_date=datetime.strptime(user_dict[REGISTRATION_DATE], DATE_FORMAT),
            bank_accounts=[BankAccount.from_dict(bank_acc) for bank_acc in user_dict.get(BANK_ACCOUNTS, [])]
        )

    @staticmethod
    def to_dict(user_account: "UserAccount") -> dict:
        return {
            LOGIN: user_account.username,
            PASSWORD_HASH: user_account.password_hash,
            REGISTRATION_DATE: user_account.registration_date.strftime(DATE_FORMAT),
            BANK_ACCOUNTS: [BankAccount.to_dict(bank_acc) for bank_acc in user_account.bank_accounts]
        }
