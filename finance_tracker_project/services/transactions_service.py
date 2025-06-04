from datetime import datetime

from finance_tracker_project.dependencies import users_repo
from finance_tracker_project.enums.category import Category
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.models.transaction import Transaction


class TransactionsService:
    def __init__(self):
        self.users_repo = users_repo

    def add_transaction(self, account: BankAccount, amount: float, date: datetime,
                        category_str: str, description: str, transaction_type: str):
        # Validate transaction type
        if transaction_type not in ["+", "-"]:
            print("Invalid transaction type. Use '+' for income and '-' for expense.")
            return

        # Parse category or default to OTHER
        try:
            category = Category[category_str.upper()]
        except KeyError:
            category = Category.OTHER

        # Update balance
        if transaction_type == "+":
            account.balance += amount
        else:
            account.balance -= amount

        # Create and add transaction
        transaction = Transaction(amount, date, category, description, transaction_type)
        account.transactions.append(transaction)

        print(f"Transaction added successfully. New balance: {account.balance:.2f}")
