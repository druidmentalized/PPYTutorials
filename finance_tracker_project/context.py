_auths_controller = None
_sessions_controller = None
_banks_controller = None
_transactions_controller = None

_auths_service = None
_reports_service = None
_banks_service = None
_transactions_service = None

_users_repo = None
_banks_repo = None
_transactions_repo = None


def get_auths_controller():
    global _auths_controller
    if _auths_controller is None:
        from finance_tracker_project.controllers.auths_controller import AuthsController
        _auths_controller = AuthsController()
    return _auths_controller


def get_sessions_controller():
    global _sessions_controller
    if _sessions_controller is None:
        from finance_tracker_project.controllers.sessions_controller import SessionsController
        _sessions_controller = SessionsController()
    return _sessions_controller


def get_banks_controller():
    global _banks_controller
    if _banks_controller is None:
        from finance_tracker_project.controllers.banks_controller import BanksController
        _banks_controller = BanksController()
    return _banks_controller


def get_transactions_controller():
    global _transactions_controller
    if _transactions_controller is None:
        from finance_tracker_project.controllers.transactions_controller import TransactionsController
        _transactions_controller = TransactionsController()
    return _transactions_controller


def get_auths_service():
    global _auths_service
    if _auths_service is None:
        from finance_tracker_project.services.auths_service import AuthsService
        _auths_service = AuthsService()
    return _auths_service


def get_reports_service():
    global _reports_service
    if _reports_service is None:
        from finance_tracker_project.services.reports_service import ReportsService
        _reports_service = ReportsService()
    return _reports_service


def get_banks_service():
    global _banks_service
    if _banks_service is None:
        from finance_tracker_project.services.banks_service import BankAccountsService
        _banks_service = BankAccountsService()
    return _banks_service


def get_transactions_service():
    global _transactions_service
    if _transactions_service is None:
        from finance_tracker_project.services.transactions_service import TransactionsService
        _transactions_service = TransactionsService()
    return _transactions_service


def get_users_repo():
    global _users_repo
    if _users_repo is None:
        from finance_tracker_project.repositories.users_repository import UsersRepository
        _users_repo = UsersRepository()
    return _users_repo