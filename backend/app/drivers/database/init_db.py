from typing import List, Dict, Any

from requests import Session

import app.domains.entities as entities
import app.api.deps as deps


def create_user(db: Session, data: dict) -> None:
    obj_in = entities.UserCreated(**data)
    uu = deps.get_user_usecase(db)
    uu.create(obj_in)


def init_db(db: Session, fixtures: List[Dict[str, Any]]) -> None:
    for data in fixtures:
        eval(f"create_{data['model']}")(db, data["fields"])
