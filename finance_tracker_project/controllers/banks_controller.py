from finance_tracker_project.config.config import PAGE_SIZE
from finance_tracker_project.dependencies import reports_service, banks_service, transactions_controller
from finance_tracker_project.enums.currency import Currency
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.models.user_account import UserAccount


class BanksController:

    def __init__(self):
        self.transaction_controller = transactions_controller
        self.report_service = reports_service
        self.bank_service = banks_service

    def run_bank_session(self, account: BankAccount):
        while True:
            print(f"\n-- {account.name} ({account.currency.name}) --")
            print("1. View balance")
            print("2. Add transaction")
            print("3. View transactions")
            print("4. Generate spending report.")
            print("5. Generate category spending report.")
            print("e. Back to main menu")
            choice = input("Choose an option: ")S

            if choice == "1":
                self.show_balance(account)
            elif choice == "2":
                self.transaction_controller.add_transaction(account)
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
        print("-- New Bank Account --")
        bank_name = input("Bank name: ")
        print("\nSupported currencies:", ", ".join([e.name for e in Currency]))
        currency = input("Currency(abbreviation/sign): ")
        self.bank_service.create_bank_account(user, bank_name, currency)

    def show_balance(self, account: BankAccount):
        print(f"Current balance of {account.name}: {account.balance}{account.currency.name}")

    def view_transactions(self, account: BankAccount):
        transactions = list(reversed(account.transactions))

        total = len(transactions)
        curr_page = 0

        while True:
            start = curr_page * PAGE_SIZE
            end = start + PAGE_SIZE
            page = transactions[start:end]

            if not page:
                print("No transactions found.")
                break

            print(f"\n--- Transactions (Page {curr_page + 1}) ---")
            for i, transaction in enumerate(page, start=1):
                print(f"{start + i}. {transaction}")

            print("\n[n] Next page  |  [p] Previous page  |  [e] Exit")
            choice = input("Choose an option: ").strip().lower()

            if choice == "n":
                if end >= total:
                    print("You're at the last page.")
                else:
                    curr_page += 1
            elif choice == "p":
                if curr_page == 0:
                    print("You're at the first page.")
                else:
                    curr_page -= 1
            elif choice == "e":
                break
            else:
                print("Invalid input.")