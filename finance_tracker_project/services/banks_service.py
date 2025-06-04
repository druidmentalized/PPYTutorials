from finance_tracker_project.dependencies import banks_repo, users_repo
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
            self.banks_repo = banks_repo
            self.users_repo = users_repo

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
