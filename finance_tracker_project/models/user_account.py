from datetime import datetime

from finance_tracker_project.models.bank_account import BankAccount


class UserAccount:

    def __init__(self, username: str, password_hash: str,
                 registration_date: datetime, bank_accounts: list[BankAccount]):
        self.username = username
        self.password_hash = password_hash
        self.registration_date = registration_date
        self.bank_accounts = bank_accounts

    @staticmethod
    def from_dict(user_dict: dict) -> "UserAccount":
        return UserAccount(
            username=user_dict["username"],
            password_hash=user_dict["password_hash"],
            registration_date=user_dict["registration_date"],
            bank_accounts=[BankAccount.from_dict(bank_acc) for bank_acc in user_dict.get("bank_accounts", [])]
        )

    @staticmethod
    def to_dict(user_account: "UserAccount") -> dict:
        ...