from finance_tracker_project.models.user_account import UserAccount


class BankAccountService:
    def create_bank_account(self, user: UserAccount, bank_name: str, currency: str):
        ...
