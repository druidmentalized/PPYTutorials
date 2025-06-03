from finance_tracker_project.dependencies import auth_service, session_controller

from finance_tracker_project.utils.utils import clear_screen


class AuthController:

    def __init__(self):
        self.auth_service = auth_service
        self.session_controller = session_controller

    def run(self):
        users_list = self.auth_service.load_users_index()
        while True:
            print("-- Finance Tracker --")
            print("1. Login")
            print("2. Register")
            print("e. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                user = self.auth_service.login(users_list)
                if user:
                    self.session_controller.run_session(user)
            elif choice == "2":
                user = self.auth_service.register()
                if user:
                    self.session_controller.run_session(user)
            elif choice == "e":
                break
            clear_screen()