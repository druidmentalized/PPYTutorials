from finance_tracker_project.models.user_account import UserAccount
from finance_tracker_project.repositories.users_repository import UsersRepository


class AuthManager:

    def __init__(self):
        self.users_repo = UsersRepository()

    def run(self):
        users_list = self.users_repo.load_users_index()
        while True:
            choice = input("1. Login\n2. Register\n3. Exit\n")
            if choice == "1":
                user = self.login()
                if user:
                    self.run_session(user)
            elif choice == "2":
                user = self.register()
                if user:
                    self.run_session(user)
            elif choice == "3":
                break

    def login(self) -> UserAccount | None:
        ...

    def register(self) -> UserAccount | None:
        ...

    def run_session(self, user: UserAccount):
        ...
