from finance_tracker_project.config.config import LOGIN, PASSWORD_HASH
from finance_tracker_project.models.user_account import UserAccount
from finance_tracker_project.repositories.users_repository import UsersRepository
from finance_tracker_project.utils.hash_utils import Hasher

class AuthService:

    def __init__(self):
        self.users_repo = UsersRepository()

    def load_users_index(self):
        return self.users_repo.load_users_index()

    def login(self, username: str, password: str, users_list: list[dict]) -> UserAccount | None:
        password_hash = Hasher.hash_password(password)

        for user in users_list:
            if user[LOGIN] == username and user[PASSWORD_HASH] == password_hash:
                return self.users_repo.load_user_profile(username)

        print("Login failed. Please try again.")
        return None


    def register(self, username: str, password: str, confirm_password: str) -> UserAccount | None:
        if password != confirm_password:
            print("Passwords do not match.")
            return None
        password_hash = Hasher.hash_password(password)

        if any(user[LOGIN] == username for user in self.users_repo.load_users_index()):
            print("User already exists.")
            return None

        new_user = UserAccount(username, password_hash)
        self.users_repo.add_user_to_index(new_user)
        self.users_repo.save_user_profile(new_user)
        return new_user