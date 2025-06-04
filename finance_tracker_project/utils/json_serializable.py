from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

class JsonSerializable(ABC):

    @abstractmethod
    def to_json(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_json(cls, data: dict):
        pass

    @staticmethod
    def serialize_value(value):
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%d")
        if isinstance(value, Enum):
            return value.value
        if isinstance(value, JsonSerializable):
            return value.to_json()
        if isinstance(value, list):
            return [JsonSerializable.serialize_value(v) for v in value]
        return value

    @staticmethod
    def deserialize_value(value):
        return value