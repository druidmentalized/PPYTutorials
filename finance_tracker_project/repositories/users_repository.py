import json
import os

from finance_tracker_project.config.config import INDEX_FILE, USERS_DIR, LOGIN, PASSWORD_HASH
from finance_tracker_project.models.user_account import UserAccount


class UsersRepository:
    def __init__(self, path=INDEX_FILE):
        self.path = path

    def load_users_index(self) -> list[dict]:
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def load_user_profile(self, username: str) -> UserAccount | None:
        try:
            path = os.path.join(USERS_DIR, f"{username}.json")
            with open(path, "r") as f:
                data = json.load(f)
                return UserAccount.from_dict(data)
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def save_user_profile(self, user: UserAccount) -> None:
        path = os.path.join(USERS_DIR, f"{user.username}.json")
        with open(path, "w") as f:
            json.dump(UserAccount.to_dict(user), f, indent=2)

    def add_user_to_index(self, user: UserAccount) -> None:
        index_data = self.load_users_index()
        index_data.append({
            LOGIN: user.username,
            PASSWORD_HASH: user.password_hash
        })
        with open(self.path, "w") as f:
            json.dump(index_data, f, indent=2)
