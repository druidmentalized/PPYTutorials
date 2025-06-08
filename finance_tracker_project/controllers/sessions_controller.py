from finance_tracker_project.config.config import GENERAL_SPENDING_REPORT_FILE, GENERAL_CATEGORY_SPENDING_REPORT_FILE
from finance_tracker_project.context import get_banks_controller, get_reports_service
from finance_tracker_project.errors.NoReportableTransactionsError import NoReportableTransactionsError
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.models.user_account import UserAccount
from finance_tracker_project.ui.console import print_header, print_option, input_option, print_info, print_error, \
    print_success, input_info


class SessionsController:
    def __init__(self) -> None:
        self.banks_controller = get_banks_controller()
        self.reports_service = get_reports_service()

    def run_session(self, user: UserAccount) -> None:
        while True:
            self._print_options()
            choice = input_option("Choose an option: ")

            if choice == "1":
                self.enter_bank_account(user)
            elif choice == "2":
                self.banks_controller.create_bank_account(user)
            elif choice == "3":
                self.generate_spending_report(user.bank_accounts)
            elif choice == "4":
                self.generate_category_report(user.bank_accounts)
            elif choice == "e":
                print_info("Exiting session...\n")
                break
            else:
                print_info("Invalid input. Please try again.")

    def _print_options(self) -> None:
        print_header("\n--- Session Menu ---")
        print_option(1, "Enter bank account")
        print_option(2, "Create bank account")
        print_option(3, "Generate general report")
        print_option(4, "Generate general category report")
        print_option("e", "Exit session")

    def enter_bank_account(self, user: UserAccount) -> None:
        if not user.bank_accounts:
            print_info("No bank accounts found. Please create one first.")
            return

        print_header("\n--- Bank Accounts ---")
        for idx, bank_acc in enumerate(user.bank_accounts):
            print_option(idx + 1, f"{bank_acc.name} ({bank_acc.currency.name})")

        try:
            choice = int(input_option("Choose an account by number: ")) - 1
            if 0 <= choice < len(user.bank_accounts):
                self.banks_controller.run_bank_session(user, user.bank_accounts[choice])
            else:
                print_error("Invalid choice. Please try again.")
        except ValueError:
            print_error("Invalid input. Please enter a number.")

    def generate_spending_report(self, accounts: list[BankAccount]) -> None:
        try:
            self.reports_service.generate_spending_report(accounts)
            print_success("General spending report generated successfully.")
            choice = input_info("Would you like to export report to the Excel spreadsheet? (Y/n)")
            if choice.strip().lower() == "y":
                self.reports_service.export_spending_report_to_excel(accounts, GENERAL_SPENDING_REPORT_FILE)
                print_success(f"Spending report exported to {GENERAL_SPENDING_REPORT_FILE}")
        except NoReportableTransactionsError as e:
            print_error(str(e))

    def generate_category_report(self, accounts: list[BankAccount]) -> None:
        try:
            self.reports_service.generate_category_report(accounts)
            print_success("General category spending report generated successfully.")
            choice = input_info("Would you like to export report to the Excel spreadsheet? (Y/n)")
            if choice.strip().lower() == "y":
                self.reports_service.export_category_report_to_excel(accounts, GENERAL_CATEGORY_SPENDING_REPORT_FILE)
                print_success(f"Category report exported to {GENERAL_CATEGORY_SPENDING_REPORT_FILE}")
        except NoReportableTransactionsError as e:
            print_error(str(e))
