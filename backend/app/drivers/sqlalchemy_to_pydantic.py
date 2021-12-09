from typing import Type, TypeVar

import pydantic

from app.drivers.database.database import Base

ModelType = TypeVar("ModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=pydantic.BaseModel)


def sqlalchemy_to_pydantic(db_obj: ModelType, schema: Type) -> SchemaType:
    return schema(**db_obj.__dict__)
