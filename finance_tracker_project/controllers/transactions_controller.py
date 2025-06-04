from datetime import datetime

from finance_tracker_project.config.config import DATE_FORMAT
from finance_tracker_project.dependencies import transactions_service
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.models.user_account import UserAccount


class TransactionsController:
    def __init__(self):
        self.transactions_service = transactions_service

    def add_transaction(self, user: UserAccount, account: BankAccount):
        print("-- Adding Transaction --")
        try:
            amount = float(input("Transaction amount: "))
        except ValueError:
            print("Transaction amount must be a number")
            return

        try:
            user_input = input(f"Transaction date (format {DATE_FORMAT}), blank for today: ")
            date = datetime.strptime(user_input, DATE_FORMAT) if user_input else datetime.today()
        except ValueError:
            print(f"Invalid date format. Please use {DATE_FORMAT}.")
            return

        category = input("Transaction category: ")
        description = input("Transaction description: ")
        transaction_type = input("Transaction type(+/-): ")

        transactions_service.add_transaction(user, account, amount, date, category, description, transaction_type)