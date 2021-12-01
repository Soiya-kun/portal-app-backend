from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class ModelName(str, Enum):
    x = "x"
    y = "y"
    z = "z"


class RestInfo(BaseModel):
    name: str
    date: int
    morning: bool = False
    afternool: bool = False
    reason: Optional[str] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def testpost():
    return {"testpost": "testpost"}


@app.get("/testuser")
async def getUser():
    return {"user_id": "testuser"}


@app.get("/{user_id}")
async def getAnotherUser(user_id: str, a: int = 0, b: int = 0):
    if user_id == ModelName.x:
        return {"user_id": "x_man", "result": a + b}
    elif user_id == ModelName.y:
        return {"user_id": "y_man", "result": a + b}
    elif user_id == ModelName.z:
        return {"user_id": "z_man", "result": a + b}
    else:
        return {"user_id": user_id, "result": a + b}


@app.post("/{user_id}")
async def postRest(restInfo: RestInfo):
    return restInfo
