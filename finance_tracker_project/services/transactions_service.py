import warnings
from datetime import datetime

from finance_tracker_project.context import get_users_repo
from finance_tracker_project.enums.category import Category
from finance_tracker_project.errors.InvalidAmountError import InvalidAmountError
from finance_tracker_project.errors.InvalidTransactionTypeError import InvalidTransactionTypeError
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.models.transaction import Transaction
from finance_tracker_project.models.user_account import UserAccount
from finance_tracker_project.warnings.NegativeBalanceWarning import NegativeBalanceWarning


class TransactionsService:
    def __init__(self) -> None:
        self.users_repo = get_users_repo()

    def add_transaction(self, user: UserAccount, account: BankAccount, amount: float, date: datetime, category_str: str,
                        description: str, transaction_type: str) -> None:
        if transaction_type not in ("+", "-"):
            raise InvalidTransactionTypeError("Invalid transaction type. Use '+' for income or '-' for expense.")

        try:
            category = Category[category_str.upper()]
        except KeyError:
            category = Category.OTHER

        if amount < 0:
            raise InvalidAmountError("Amount must be positive number.")

        if transaction_type == "+":
            account.balance += amount
        else:
            if account.balance - amount < 0:
                warnings.warn("This transaction would result in a negative balance.", NegativeBalanceWarning)
            account.balance -= amount

        new_transaction = Transaction(
            amount=amount,
            date=date,
            category=category,
            description=description,
            transaction_type=transaction_type
        )
        account.transactions.append(new_transaction)
        self.users_repo.save_user_profile(user)
