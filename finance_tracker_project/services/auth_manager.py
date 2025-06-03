from finance_tracker_project.config.config import LOGIN, PASSWORD_HASH
from finance_tracker_project.models.user_account import UserAccount
from finance_tracker_project.repositories.users_repository import UsersRepository

from finance_tracker_project.utils.hash_utils import Hasher
from finance_tracker_project.utils.utils import clear_screen


class AuthManager:

    def __init__(self):
        self.users_repo = UsersRepository()

    def run(self):
        users_list = self.users_repo.load_users_index()
        while True:
            choice = input("1. Login\n2. Register\n3. Exit\n")
            if choice == "1":
                user = self.login(users_list)
                if user:
                    self.run_session(user)
            elif choice == "2":
                user = self.register()
                if user:
                    self.run_session(user)
            elif choice == "3":
                break
            clear_screen()

    def login(self, users_list: list[dict]) -> UserAccount | None:
        login = input("Login: ")
        password_hash = Hasher.hash_password(input("Password: "))

        for user in users_list:
            if user[LOGIN] == login and user[PASSWORD_HASH] == password_hash:
                return self.users_repo.load_user_profile(login)

        print("Login failed. Please try again.")
        return None

    def register(self) -> UserAccount | None:
        login = input("Login: ")
        password = input("Password: ")
        confirm = input("Confirm password: ")
        if password != confirm:
            print("Passwords do not match.")
            return None
        password_hash = Hasher.hash_password(password)

        if any(user[LOGIN] == login for user in self.users_repo.load_users_index()):
            print("User already exists.")
            return None

        new_user = UserAccount(login, password_hash)
        self.users_repo.add_user_to_index(new_user)
        self.users_repo.save_user_profile(new_user)
        return new_user

    def run_session(self, user: UserAccount):
        while True:
            print("Options:")
            ...