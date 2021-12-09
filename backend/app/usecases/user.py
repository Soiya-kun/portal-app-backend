from typing import Optional

from app.domains import entities
from app.repositories.user import IUserRepository


class UserUsecase:
    repo: IUserRepository

    def __init__(self, repo: IUserRepository) -> None:
        self.repo = repo

    def create(self, obj_in: entities.UserCreated) -> Optional[entities.User]:
        return self.repo.create(obj_in=obj_in)

    def authenticate(self, username: str, password: str) -> Optional[entities.User]:
        return self.repo.authenticate(username=username, password=password)
