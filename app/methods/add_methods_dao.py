from app.auth.dao import UserDAO
from dao.session_maker import connection
from asyncio import run
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.schemas import UserPydantic
from typing import List
from uuid6 import uuid7

@connection(commit=True)
async def add_one_user(user_data: UserPydantic, session: AsyncSession):
    new_user = await UserDAO.add(session=session, values=user_data)
    print(f"Добавлен новый пользователь с ID: {new_user.id}")
    return new_user.id

@connection(commit=True)
async def add_many_users(users_data: List[UserPydantic], session: AsyncSession):
    new_users = await UserDAO.add_many(session=session, instances=users_data)
    user_ids_list = [user.id for user in new_users]
    print(f"Добавлены новые пользователи с ID: {user_ids_list}")
    return user_ids_list