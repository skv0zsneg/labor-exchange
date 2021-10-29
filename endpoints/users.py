from typing import List
from fastapi import APIRouter, Depends, status

from models.user import User, UserIn
from .depends import get_user_repository
from repositories.users import UserRepository


router = APIRouter()


@router.get("/", response_model=List[User])
async def read_users(users: UserRepository = Depends(get_user_repository),
                     limit: int = 100, 
                     skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserIn,
                      users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)


@router.put("/", response_model=User)
async def create_user(id: int,
                      user: UserIn,
                      users: UserRepository = Depends(get_user_repository)):
    return await users.update(id=id, u=user)
