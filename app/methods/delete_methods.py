from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.dao import UserDAO, UserHistoryDAO
from dao.session_maker import connection
from app.dao.schemas import UserPydantic
from asyncio import run
from uuid import UUID
from sqlalchemy import Uuid

@connection(commit=True)
async def delete_user_by_id(session: AsyncSession, user_id: Uuid):
    # Получаем слепок записи
    record = await UserDAO.find_one_or_none_by_id(session=session,data_id=user_id)
    # Сохраняем его в таблицу истории
    await UserHistoryDAO.add(session=session, values=UserPydantic.model_validate(record))
    # Удаляем запись из основной таблицы
    await UserDAO.delete(session=session, filters=UserPydantic.model_validate(user_id))
