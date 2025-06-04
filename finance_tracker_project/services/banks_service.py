from finance_tracker_project.dependencies import banks_repo, users_repo
from finance_tracker_project.enums.currency import Currency
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.models.user_account import UserAccount


class BankAccountsService:
    def __init__(self):
            self.banks_repo = banks_repo
            self.users_repo = users_repo

    def create_bank_account(self, user: UserAccount, bank_name: str, currency_str: str):
        if any(acc.name.lower() == bank_name.lower() for acc in user.bank_accounts):
            print(f"Bank account with the name '{bank_name}' already exists.")
            return

        try:
            currency = Currency[currency_str.upper()]
        except KeyError:
            print("Invalid currency code.")
            return

            # Create and save
        new_account = BankAccount(name=bank_name, currency=currency, transactions=[])
        user.bank_accounts.append(new_account)
        self.users_repo.save_user_profile(user)
        print(f"Bank account '{bank_name}' created successfully.")
