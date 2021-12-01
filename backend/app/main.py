from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class ModelName(str, Enum):
    x = "x"
    y = "y"
    z = "z"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user")
async def getUser():
    return {"user_id": "testuser"}


@app.get("/{user_id}")
async def getAnotherUser(user_id: str):
    if user_id == ModelName.x:
        return {"user_id": "x_man"}
    elif user_id == ModelName.y:
        return {"user_id": "y_man"}
    elif user_id == ModelName.z:
        return {"user_id": "z_man"}
    else:
        return {"user_id": user_id}


@app.post("/")
async def testpost():
    return {"testpost": "testpost"}
