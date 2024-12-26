from datetime import datetime
from typing import Annotated
from uuid import UUID
from sqlalchemy import Identity, Integer, String, Uuid, TIMESTAMP, text, func
from sqlalchemy.orm import DeclarativeBase , Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession

from app.config import database_url

# Создаем асинхронный движок для работы с базой данных
engine = create_async_engine(url=database_url)
# Создаем фабрику сессий для взаимодействия с базой данных
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Создаем аннотации
uniq_str_an = Annotated[str, mapped_column(String, unique=True)]
pk_uuid_an = Annotated[UUID, mapped_column(Uuid, primary_key=True)]
uuid_an = Annotated[UUID,  mapped_column(Uuid)]

#Базовый класс для моделей без версий
class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True # Класс абстрактный, чтобы не создавать отдельную таблицу для него

    def __repr__(self) -> str:
        """Строковое представление объекта для удобства отладки."""
        return f"<{self.__class__.__name__}(id={self.id}, created_at={func.now()})>"
    
# Базовый класс для моделей таблиц историй
class HistoryBase(Base):
    __abstract__ = True # Класс абстрактный, чтобы не создавать отдельную таблицу для него
    
    id: Mapped[uuid_an]
    vers_id: Mapped[int] = mapped_column(Integer, Identity(), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), index=True)
    updated_by_id: Mapped[str] = mapped_column(String, server_default=text("'sys_user'"))


