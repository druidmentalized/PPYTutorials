from finance_tracker_project.models.bank_account import BankAccount


class ReportsService:
    def generate_spending_report(self, accounts_list: list[BankAccount]) -> None:
        ...

    def generate_category_report(self, accounts_list: list[BankAccount]) -> None:
        ...