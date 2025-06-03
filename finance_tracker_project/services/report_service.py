from finance_tracker_project.models.bank_account import BankAccount


class ReportService:
    def generate_spending_report(self, accounts_list: list[BankAccount]):
        ...

    def generate_category_report(self, accounts_list: list[BankAccount]):
        ...