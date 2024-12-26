from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.dao import UserDAO, UserHistoryDAO
from dao.session_maker import connection
from app.dao.schemas import UserPydantic, UpdateUserPydantic
from sqlalchemy import Uuid

@connection(commit=True)
async def update_user_by_id(session: AsyncSession, user_id: Uuid, values: UpdateUserPydantic):
    # Получаем слепок записи
    record = await UserDAO.find_one_or_none_by_id(session=session,data_id=user_id)
    # Сохраняем его в таблицу истории
    await UserHistoryDAO.add(session=session, values=UserPydantic.model_validate(record))
    # Обновляем запись в основной таблице
    await UserDAO.update(session=session, filters=UserPydantic.model_validate(user_id), values=values)
    # Проверяем есть ли изменения или выполняем роллбек 
    old_vers = UserPydantic.model_validate(record).model_dump()
    new_vers = UserPydantic.model_validate(values).model_dump()
    if old_vers == new_vers:
        await session.rollback()
