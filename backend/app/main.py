from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.middleware.cors import CORSMiddleware

from app.domains.entities.login_token import LoginToken
from app.drivers.security import create_access_token

import app.api.deps as deps
import app.usecases as usecases
import app.domains.entities as entities

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
async def root(token: str = Depends(oauth2_scheme)):
    return {"message": "Hello World"}


@app.post("/token", response_model=LoginToken)
async def login_for_access_token(
    *,
    form_data: OAuth2PasswordRequestForm = Depends(),
    uu: usecases.UserUsecase = Depends(deps.get_user_usecase)
):
    user: Optional[entities.User] = uu.authenticate(
        form_data.username, form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
