from finance_tracker_project.controllers.bank_controller import BankController
from finance_tracker_project.controllers.session_controller import SessionController
from finance_tracker_project.services.auth_service import AuthService
from finance_tracker_project.services.report_service import ReportService
from finance_tracker_project.repositories.users_repository import UsersRepository

session_controller = SessionController()
bank_controller = BankController()
auth_service = AuthService()
report_service = ReportService()
users_repo = UsersRepository()