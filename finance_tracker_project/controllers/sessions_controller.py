from finance_tracker_project.dependencies import banks_controller, reports_service
from finance_tracker_project.models.user_account import UserAccount


class SessionsController:
    def __init__(self):
        self.bank_controller = banks_controller
        self.report_service = reports_service

    def run_session(self, user: UserAccount):
        while True:
            print("\n--- Session Menu ---")
            print("1. Enter bank account")
            print("2. Create bank account")
            print("3. Generate general report")
            print("4. Generate general category report")
            print("e. Exit session")
            choice = input("Choose an option: ")

            if choice == "1":
                self.enter_bank_account(user)
            elif choice == "2":
                self.bank_controller.create_bank_account(user)
            elif choice == "3":
                self.report_service.generate_spending_report(user.bank_accounts)
            elif choice == "4":
                self.report_service.generate_category_report(user.bank_accounts)
            elif choice == "e":
                print("Exiting session...\n")
                break
            else:
                print("Invalid input. Please try again.")

    def enter_bank_account(self, user: UserAccount):
        if not user.bank_accounts:
            print("No bank accounts found. Please create one first.")
            return

        print("\n--- Bank Accounts ---")
        for idx, bank_acc in enumerate(user.bank_accounts):
            print(f"{idx + 1}. {bank_acc.name} ({bank_acc.currency.name})")

        try:
            choice = int(input("Choose an account by number: ")) - 1
            if 0 <= choice < len(user.bank_accounts):
                self.bank_controller.run_bank_session(user, user.bank_accounts[choice])
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")