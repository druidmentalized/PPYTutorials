from finance_tracker_project.config.config import LOGIN, PASSWORD_HASH
from finance_tracker_project.context import get_users_repo
from finance_tracker_project.errors.AuthenticationError import AuthenticationError
from finance_tracker_project.errors.BlankDataError import BlankDataError
from finance_tracker_project.errors.DifferentPasswordsError import DifferentPasswordsError
from finance_tracker_project.errors.DuplicateUserError import DuplicateUserError
from finance_tracker_project.models.user_account import UserAccount
from finance_tracker_project.utils.hash_utils import Hasher
class AuthsService:

    def __init__(self) -> None:
        self.users_repo = get_users_repo()

    def load_users_index(self) -> list[dict]:
        return self.users_repo.load_users_index()

    def login(self, username: str, password: str, users_list: list[dict]) -> UserAccount | None:
        if username == "" or password == "":
            raise BlankDataError("Username and password is required(cannot be blank).")
        
        for user in users_list:
            if user[LOGIN] == username:
                if Hasher.check_password(password, user[PASSWORD_HASH]):
                    return self.users_repo.load_user_profile(username)
        raise AuthenticationError("Invalid username or password.")


    def register(self, username: str, password: str, confirm_password: str) -> UserAccount | None:
        if username == "" or password == "":
            raise BlankDataError("Username and password is required(cannot be blank).")
        
        if password != confirm_password:
            raise DifferentPasswordsError("Passwords do not match.")
        password_hash = Hasher.hash_password(password)

        if any(user[LOGIN] == username for user in self.users_repo.load_users_index()):
            raise DuplicateUserError("User already exists.")

        new_user = UserAccount(username, password_hash)
        self.users_repo.add_user_to_index(new_user)
        self.users_repo.save_user_profile(new_user)
        return new_user