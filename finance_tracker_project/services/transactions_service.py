from datetime import datetime

from finance_tracker_project.dependencies import get_users_repo
from finance_tracker_project.enums.category import Category
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.models.transaction import Transaction
from finance_tracker_project.models.user_account import UserAccount


class TransactionsService:
    def __init__(self):
        self.users_repo = get_users_repo()

    def add_transaction(self, user: UserAccount, account: BankAccount, amount: float, date: datetime, category_str: str,
                        description: str, transaction_type: str):
        if transaction_type not in ("+", "-"):
            print("Invalid transaction type. Use '+' for income or '-' for expense.")
            return

        try:
            category = Category[category_str.upper()]
        except KeyError:
            category = Category.OTHER

        if transaction_type == "+":
            account.balance += amount
        else:
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
        print("Transaction added successfully.")
