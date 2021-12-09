from typing import Optional

from sqlalchemy.orm import Session

import app.repositories as repositories
from app.domains import entities
from app.drivers.database import models
from app.drivers.security import verify_password, get_password_hash
from app.drivers.sqlalchemy_to_pydantic import sqlalchemy_to_pydantic


class SQLUserRepository(repositories.IUserRepository):
    def __init__(self, db: Session) -> None:
        self.db: Session = db
        self.model = models.User

    def create(self, obj_in: entities.UserCreated) -> entities.User:
        user = models.User(
            username=obj_in.username,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return sqlalchemy_to_pydantic(user, entities.User)

    def _get_by_username(self, username: str) -> Optional[models.User]:
        return self.db.query(self.model).filter(self.model.username == username).first()

    def authenticate(self, username: str, password: str) -> Optional[entities.User]:
        user: Optional[models.User] = self._get_by_username(username=username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return sqlalchemy_to_pydantic(user, entities.User)
