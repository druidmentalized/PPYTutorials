import warnings
from datetime import datetime

from finance_tracker_project.context import get_reports_service, get_banks_service, get_transactions_controller
from finance_tracker_project.config.config import PAGE_SIZE, DATE_FORMAT, DATE_FORMAT_READABLE
from finance_tracker_project.enums.currency import Currency
from finance_tracker_project.errors.DuplicateBankError import DuplicateBankError
from finance_tracker_project.errors.InvalidCurrencyError import InvalidCurrencyError
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.models.transaction import Transaction
from finance_tracker_project.models.user_account import UserAccount
from finance_tracker_project.ui.console import print_positive, print_negative, print_header, print_option, input_option, \
    print_info, print_error, input_info
from finance_tracker_project.warnings.NegativeBalanceWarning import NegativeBalanceWarning


class BanksController:

    def __init__(self) -> None:
        self.transactions_controller = get_transactions_controller()
        self.reports_service = get_reports_service()
        self.banks_service = get_banks_service()

    def _print_bank_menu(self, account: BankAccount) -> None:
        print_header(f"\n-- {account.name} ({account.currency.name}) --")
        print_option(1, "View account information")
        print_option(2, "Add transaction")
        print_option(3, "View transactions")
        print_option(4, "Update bank account")
        print_option(5, "Delete bank account")
        print_option(6, "Generate spending report.")
        print_option(7, "Generate category spending report.")
        print_option("e", "Back to main menu")

    def run_bank_session(self, user: UserAccount, bank: BankAccount) -> None:
        while True:
            self._print_bank_menu(bank)
            choice = input_option("Choose an option: ")

            if choice == "1":
                self.show_info(bank)
            elif choice == "2":
                self.transactions_controller.add_transaction(user, bank)
            elif choice == "3":
                self.view_transactions(bank)
            elif choice == "4":
                self.update_bank_account(user, bank)
            elif choice == "5":
                self.delete_bank_account(user, bank)
                return
            elif choice == "6":
                self.reports_service.generate_spending_report([bank])
            elif choice == "7":
                self.reports_service.generate_category_report([bank])
            elif choice == "e":
                break
            else:
                print_info("Invalid choice. Try again.")

    def show_info(self, account: BankAccount) -> None:
        print_header(f"\n-- Information about {account.name} --")

        balance_str = f"Balance: {account.balance} {account.currency.name}"
        if account.balance > 0: print_positive(balance_str)
        else: print_negative(balance_str)

        if account.balance < 0: warnings.warn("Balance of this account is below zero.", NegativeBalanceWarning)

        print_info(f"Creation date: {account.creation_date.strftime(DATE_FORMAT)}")
        print_info(f"Transactions: {len(account.transactions)}")

    def create_bank_account(self, user: UserAccount) -> None:
        print_header("-- Create New Bank Account --")
        bank_name = input_info("Bank name: ")
        print_info(f"\nSupported currencies: {", ".join([e.name for e in Currency])}")
        currency = input_info("Currency(abbreviation/sign): ")
        try:
            self.banks_service.create_bank_account(user, bank_name, currency)
            print_positive(f"Bank account '{bank_name}' created successfully.")
        except DuplicateBankError | InvalidCurrencyError as e:
            print_error(str(e))

    def update_bank_account(self, user: UserAccount, bank: BankAccount) -> None:
        print_header("-- Update Bank Info --")
        bank_name = input_info("Bank name(blank for same): ")
        print_info(f"\nSupported currencies: {", ".join([e.name for e in Currency])}")
        currency = input_info("Currency(abbreviation/sign)(blank for same): ")
        try:
            self.banks_service.update_bank_account(user, bank, bank_name, currency)
            print_positive(f"Bank account '{bank_name}' updated successfully.")
        except DuplicateBankError | InvalidCurrencyError as e:
            print_error(str(e))

    def delete_bank_account(self, user: UserAccount, bank: BankAccount) -> None:
        user_input = input_info("Are you sure you want to delete this account?(Y/n) ")

        if user_input == "Y":
            self.banks_service.delete_bank_account(user, bank)
            print_positive(f"Bank account '{bank}' deleted successfully.")

    def view_transactions(self, account: BankAccount) -> None:
        transactions = list(reversed(account.transactions))

        if not transactions:
            print_info("No transactions found.")
            return

        filtered = self._get_filtered_transactions(transactions)

        if not filtered:
            return

        total_pages = (len(filtered) - 1) // PAGE_SIZE + 1
        curr_page = 0

        while True:
            self._render_transactions_page(filtered, curr_page)
            choice = self._get_paging_input()

            if choice == "n" and curr_page + 1 >= total_pages:
                print_info("You're at the last page.")
            elif choice == "n":
                curr_page += 1
            elif choice == "p" and curr_page == 0:
                print_info("You're at the first page.")
            elif choice == "p":
                curr_page -= 1
            elif choice == "e":
                break

    def _render_transactions_page(self, transactions: list, curr_page: int) -> None:
        start = curr_page * PAGE_SIZE
        end = start + PAGE_SIZE
        page = transactions[start:end]

        print_header(f"\n--- Transactions (Page {curr_page + 1}) ---")
        for i, transaction in enumerate(page, start=1):
            text = f"{start + i}. {transaction}"
            if transaction.transaction_type == "+":
                print_positive(text)
            elif transaction.transaction_type == "-":
                print_negative(text)
            else:
                print_info(text)

    def _get_paging_input(self) -> str:
        print_info("\n[n] Next page  |  [p] Previous page  |  [e] Exit")
        return input_option("Choose an option: ").strip().lower()

    def _get_filtered_transactions(self, transactions: list[Transaction]) -> list[Transaction] | None:
        print_header("\n-- Filter Options --")
        print_info("Leave any field blank to skip that filter.")
        date_str = input_info(f"Filter by date ({DATE_FORMAT_READABLE})(blank to skip): ").strip()
        tx_type = input_info("Filter by type (+/-)(blank to skip): ").strip()
        category = input_info("Filter by category(blank to skip): ").strip().lower()

        filtered = transactions

        if date_str:
            try:
                filter_date = datetime.strptime(date_str, DATE_FORMAT).date()
                filtered = [tx for tx in filtered if tx.date.date() == filter_date]
            except ValueError:
                print_error("Invalid date format. Skipping date filter.")

        if tx_type in ("+", "-"):
            filtered = [tx for tx in filtered if tx.transaction_type == tx_type]

        if category:
            filtered = [tx for tx in filtered if tx.category.value.lower() == category]

        if not filtered:
            print_error("No transactions match the filters.")
            return None

        return filtered