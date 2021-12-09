import abc
from typing import Optional

from app.domains import entities


class IUserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def authenticate(self, username: str, password: str) -> Optional[entities.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, obj_in: entities.UserCreated) -> entities.user:
        raise NotImplementedError
