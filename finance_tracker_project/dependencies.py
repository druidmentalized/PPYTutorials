from finance_tracker_project.controllers.bank_controller import BankController
from finance_tracker_project.controllers.session_controller import SessionController
from finance_tracker_project.controllers.transaction_controller import TransactionController
from finance_tracker_project.repositories.banks_repository import BanksRepository
from finance_tracker_project.repositories.transactions_repository import TransactionsRepository
from finance_tracker_project.services.auth_service import AuthService
from finance_tracker_project.services.bank_service import BankAccountService
from finance_tracker_project.services.report_service import ReportService
from finance_tracker_project.repositories.users_repository import UsersRepository

session_controller = SessionController()
bank_controller = BankController()
transaction_controller = TransactionController()
auth_service = AuthService()
report_service = ReportService()
bank_service = BankAccountService()
users_repo = UsersRepository()
banks_repo = BanksRepository()
transactions_repo = TransactionsRepository()