from finance_tracker_project.models.user_account import UserAccount


class AuthManager:
    def run(self):
        self.load_users()
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

    def load_users(self):
        ...

    def login(self) -> UserAccount | None:
        ...

    def register(self) -> UserAccount | None:
        ...

    def run_session(self, user: UserAccount):
        ...
