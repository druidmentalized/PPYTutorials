from finance_tracker_project.errors.AuthenticationError import AuthenticationError
from finance_tracker_project.errors.DifferentPasswordsError import DifferentPasswordsError
from finance_tracker_project.errors.DuplicateUserError import DuplicateUserError
from finance_tracker_project.models.user_account import UserAccount
from finance_tracker_project.ui.console import print_header, print_option, input_option, input_info, print_info, print_error

from finance_tracker_project.utils.utils import clear_screen
from finance_tracker_project.context import get_auths_service, get_sessions_controller


class AuthsController:

    def __init__(self) -> None:
        self.auth_service = get_auths_service()
        self.session_controller = get_sessions_controller()

    def run(self) -> None:
        users_list = self.auth_service.load_users_index()
        while True:
            self._print_options()
            choice = input_option("Choose an option: ")
            if choice == "1":
                user = self.login(users_list)
                if user:
                    self.session_controller.run_session(user)
            elif choice == "2":
                user = self.register()
                if user:
                    self.session_controller.run_session(user)
            elif choice == "e":
                break
            else:
                print_error("Invalid choice. Please try again.")
            clear_screen()

    def login(self, users_list: list[dict]) -> UserAccount | None:
        username = input_info("Username: ")
        password = input_info("Password: ")
        try:
            return self.auth_service.login(username, password, users_list)
        except AuthenticationError as e:
            print_error(str(e))
            return None

    def register(self) -> UserAccount | None:
        username = input_info("Username: ")
        password = input_info("Password: ")
        confirm_password = input_info("Confirm Password: ")
        try:
            return self.auth_service.register(username, password, confirm_password)
        except DifferentPasswordsError | DuplicateUserError as e:
            print_error(str(e))
            return None

    def _print_options(self) -> None:
        print_header("-- Finance Tracker --")
        print_option(1, "Login")
        print_option(2, "Register")
        print_option("e", "Exit")