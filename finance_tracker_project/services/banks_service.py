from finance_tracker_project.dependencies import get_users_repo
from finance_tracker_project.enums.currency import Currency
from finance_tracker_project.models.bank_account import BankAccount
from finance_tracker_project.models.user_account import UserAccount

class BankAccountsService:
    CURRENCY_ALIASES = {
        "$": "USD",
        "€": "EUR",
        "zł": "PLN",
        "₽": "RUB",
        "ARS": "ARS"
    }

    def __init__(self):
        self.users_repo = get_users_repo()

    def create_bank_account(self, user: UserAccount, bank_name: str, currency_str: str):
        if any(acc.name.lower() == bank_name.lower() for acc in user.bank_accounts):
            print(f"Bank account with the name '{bank_name}' already exists.")
            return

        normalized = currency_str.strip().upper()
        code = self.CURRENCY_ALIASES.get(normalized, normalized)

        try:
            currency = Currency[code]
        except KeyError:
            print("Invalid currency code.")
            return

        new_account = BankAccount(name=bank_name, currency=currency, balance=0., transactions=[])
        user.bank_accounts.append(new_account)
        self.users_repo.save_user_profile(user)
        print(f"Bank account '{bank_name}' created successfully.")


    def update_bank_account(self, user: UserAccount, bank: BankAccount, bank_name: str, currency_str: str):
        bank_name = bank_name.strip() or bank.name
        currency_str = currency_str.strip() or bank.currency.name

        if bank_name.lower() != bank.name.lower():
            if any(acc.name.lower() == bank_name.lower() and acc is not bank for acc in user.bank_accounts):
                print(f"Bank account with the name '{bank_name}' already exists.")
                return

        normalized = currency_str.upper()
        code = self.CURRENCY_ALIASES.get(normalized, normalized)

        try:
            currency = Currency[code]
        except KeyError:
            print("Invalid currency code.")
            return

        bank.name = bank_name
        bank.currency = currency
        self.users_repo.save_user_profile(user)
        print(f"Bank account '{bank_name}' updated successfully.")


    def delete_bank_account(self, user: UserAccount, bank: BankAccount):
        user.bank_accounts.remove(bank)
        self.users_repo.save_user_profile(user)