import json
from typing import Any

from finance_tracker_project.models.user_account import UserAccount


class UsersRepository:
    def __init__(self, path="finance_tracker_project/data/index.json"):
        self.path = path

    def load_users_index(self) -> list[dict]:
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def load_user_profile(self, username: str) -> Any | None:
        try:
            with open(f"finance_tracker_project/data/users/{username}.json", "r") as f:
                data = json.load(f)
                return UserAccount.from_dict(data)
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def save_user_profile(self, user: UserAccount) -> None:
        with open(f"data/users/{user.username}.json", "w") as f:
            json.dump(UserAccount.to_dict(user), f, indent=2)
