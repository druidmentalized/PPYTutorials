from finance_tracker_project.dependencies import report_service
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.models.user_account import UserAccount


class BankController:

    def __init__(self):
        self.report_service = report_service

    def run_bank_session(self, account: BankAccount):
        while True:
            print(f"\n-- {account.name} ({account.currency.name}) --")
            print("1. View balance")
            print("2. Add transaction")
            print("3. View transactions")
            print("4. Generate spending report.")
            print("5. Generate category spending report.")
            print("e. Back to main menu")
            choice = input("Choose an option: ")

            if choice == "1":
                self.show_balance(account)
            elif choice == "2":
                self.add_transaction(account)
            elif choice == "3":
                self.view_transactions(account)
            elif choice == "4":
                self.report_service.generate_spending_report([account])
            elif choice == "5":
                self.report_service.generate_category_report([account])
            elif choice == "e":
                break
            else:
                print("Invalid choice. Try again.")

    def create_bank_account(self, user: UserAccount):
        ...

    def show_balance(self, account: BankAccount):
        ...

    def add_transaction(self, account: BankAccount):
        ...

    def view_transactions(self, account: BankAccount):
        ...