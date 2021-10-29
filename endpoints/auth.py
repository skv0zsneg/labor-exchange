from fastapi.param_functions import Depends
from models.token import Token, Login
from .depends import get_user_repository
from core.security import verify_password, create_access_token
from repositories.users import UserRepository
from fastapi import APIRouter, HTTPException, status


router = APIRouter()


@router.post("/", response_model=Token)
async def login(login: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password.")
    return Token(access_token=create_access_token({'sub': user.email}),
                 token_type='Bearer')
    