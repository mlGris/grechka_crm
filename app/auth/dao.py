from app.dao.base import BaseDAO
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from app.dao.models import User, UserRole, UserToProject, Subscription, Project, UserHistory, UsToPrHistory, ProjectHistory, SubscriptionHistory

# ----Классы с индивидуальными методами для моделей----
class UserDAO(BaseDAO[UserHistory]):
    model = User

    @classmethod
    async def get_all_users(cls, session: AsyncSession):
        query = select(cls.model)
        result = await session.execute(query)
        records = result.scalars().all()
        return records
    
    @classmethod
    async def get_username_id(cls,session: AsyncSession, filters: BaseModel):
        filter_dict = filters.model_dump(exclude_unset=True)
        query = select(**filter_dict)
        print(query)  # Выводим запрос для отладки
        result = await session.execute(query)  # Выполняем асинхронный запрос
        records = result.all()  # Получаем все результаты
        return records  # Возвращаем список записей
    
class UserRoleDAO(BaseDAO[UserRole]):
    model = UserRole

class UserToProjectDAO(BaseDAO[UserToProject]):
    model = UserToProject

class SubscriptionDAO(BaseDAO[Subscription]):
    model = Subscription

class ProjectDAO(BaseDAO[Project]):
    model = Project

class UserHistoryDAO(BaseDAO[UserHistory]):
    model = UserHistory

class UsToPrHistoryDAO(BaseDAO[UsToPrHistory]):
    model = UsToPrHistory

class ProjectHistoryDAO(BaseDAO[ProjectHistory]):
    model = ProjectHistory

class SubscriptionHistoryDAO(BaseDAO[SubscriptionHistory]):
    model = SubscriptionHistory
