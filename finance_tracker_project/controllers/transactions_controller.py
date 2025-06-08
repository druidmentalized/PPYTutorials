from datetime import datetime

from finance_tracker_project.config.config import DATE_FORMAT, DATE_FORMAT_READABLE
from finance_tracker_project.context import get_transactions_service
from finance_tracker_project.errors.BlankDataError import BlankDataError
from finance_tracker_project.errors.InvalidAmountError import InvalidAmountError
from finance_tracker_project.errors.InvalidTransactionTypeError import InvalidTransactionTypeError
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.models.user_account import UserAccount
from finance_tracker_project.ui.console import print_error, input_info, print_header, print_positive


class TransactionsController:
    def __init__(self) -> None:
        self.transactions_service = get_transactions_service()

    def gather_transaction_input(self) -> tuple[float, datetime, str, str, str] | None:
        try:
            amount = float(input_info("Transaction amount: "))
        except ValueError:
            print_error("Transaction amount must be a number")
            return None

        try:
            user_input = input_info(f"Transaction date ({DATE_FORMAT_READABLE}), blank for today: ")
            date = datetime.strptime(user_input, DATE_FORMAT) if user_input else datetime.today()
        except ValueError:
            print_error(f"Invalid date format. Please use {DATE_FORMAT_READABLE}.")
            return None

        category = input_info("Transaction category: ")
        description = input_info("Transaction description: ")
        transaction_type = input_info("Transaction type(+/-): ")
        return amount, date, category, description, transaction_type

    def add_transaction(self, user: UserAccount, account: BankAccount) -> None:
        print_header("-- Adding Transaction --")
        data = self.gather_transaction_input()
        if data is None:
            return

        amount, date, category, description, transaction_type = data
        try:
            self.transactions_service.add_transaction(user, account, amount, date, category, description, transaction_type)
            print_positive("Transaction added successfully.")
        except (InvalidAmountError, InvalidTransactionTypeError, BlankDataError) as e:
            print_error(str(e))
