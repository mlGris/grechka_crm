from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.dao import UserDAO
from dao.session_maker import connection
from app.dao.schemas import UsernameIdPydantic, UserPydantic
from asyncio import run
from uuid import UUID

@connection(commit=False)
async def get_user(session: AsyncSession, data_id: UUID,):
    user = await UserDAO.find_one_or_none_by_id(session=session, data_id=data_id)
    print(UserPydantic.model_validate(user).model_dump())