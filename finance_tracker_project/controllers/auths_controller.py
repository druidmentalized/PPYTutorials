from finance_tracker_project.dependencies import auths_service, sessions_controller
from finance_tracker_project.models.user_account import UserAccount

from finance_tracker_project.utils.utils import clear_screen


class AuthController:

    def __init__(self):
        self.auth_service = auths_service
        self.session_controller = sessions_controller

    def run(self):
        users_list = self.auth_service.load_users_index()
        while True:
            print("-- Finance Tracker --")
            print("1. Login")
            print("2. Register")
            print("e. Exit")
            choice = input("Choose an option: ")
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
            clear_screen()

    def login(self, users_list: list[dict]) -> UserAccount | None:
        username = input("Username: ")
        password = input("Password: ")
        return self.auth_service.login(username, password, users_list)

    def register(self) -> UserAccount | None:
        username = input("Username: ")
        password = input("Password: ")
        confirm_password = input("Confirm Password: ")
        return self.auth_service.register(username, password, confirm_password)