from typing import Generator

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.drivers.database.database import SessionLocal

import app.repositories as repositories
import app.usecases as usecases
import app.interfaces as interfaces

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"api/auth/access-token/", auto_error=False
)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_usecase(db: Session = Depends(get_db)) -> usecases.UserUsecase:
    repo: repositories.IUserRepository = interfaces.SQLUserRepository(db)
    return usecases.UserUsecase(repo)
