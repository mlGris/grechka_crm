from sqlalchemy import Text, ForeignKey, Uuid, String
from sqlalchemy.orm import Mapped, relationship, mapped_column 
from app.dao.database import HistoryBase, Base, uniq_str_an, uuid_an, pk_uuid_an

# Модель справочника ролей пользователя
class UserRole(Base):
    __tablename__ = "dic_users_roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[uniq_str_an]

    subscriptions: Mapped[list["UserToProject"]] = relationship(
        back_populates="dic_user_roles",
    )

class User(Base):
    __tablename__ = "users"

    id: Mapped[pk_uuid_an]
    name: Mapped[str] = mapped_column(String, index=True)
    mid_name: Mapped[str| None] = mapped_column(String, index=True)
    surname: Mapped[str | None] = mapped_column(String, index=True)
    login: Mapped[uniq_str_an]
    password: Mapped[str]
    email: Mapped[uniq_str_an]
    phone_num: Mapped[str | None]

    projects: Mapped[list["Project"]] = relationship(
        back_populates="users",
        secondary="users_to_projects",
        lazy="joined",
    )

    subscriptions: Mapped[list["Subscription"]] = relationship(
        back_populates="user",
        lazy="joined",
        cascade="all, delete-orphan",
    )


class UserHistory(HistoryBase):
    __tablename__= "users_history"

    name: Mapped[str]
    mid_name: Mapped[str| None]
    surname: Mapped[str | None]
    login: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    phone_num: Mapped[str | None]

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[pk_uuid_an]
    name: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    db_name: Mapped[uniq_str_an]
    
    users: Mapped[list["User"]] = relationship(
        back_populates="projects",
        secondary="users_to_projects",
    )
    
class ProjectHistory(HistoryBase):
    __tablename__= "projects_history"

    name: Mapped[str]
    description: Mapped[str] = mapped_column(Text, nullable=True)
    db_name: Mapped[str]

class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[pk_uuid_an]
    name: Mapped[uniq_str_an]
    description: Mapped[str | None]
    price: Mapped[float]
    duration: Mapped[int]
    user_id: Mapped[Uuid] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(
        back_populates="subscriptions",
    )

class SubscriptionHistory(HistoryBase):
    __tablename__= "subscriptions_history"

    name: Mapped[str]
    description: Mapped[str | None]
    price: Mapped[float]
    duration: Mapped[int]
    user_id: Mapped[uuid_an] 

class UserToProject(Base):
    __tablename__ = "users_to_projects"

    id: Mapped[pk_uuid_an]
    project_id: Mapped[Uuid] = mapped_column(ForeignKey("projects.id"))
    user_id: Mapped[Uuid] = mapped_column(ForeignKey("users.id"))
    dic_user_role_id: Mapped[int | None] = mapped_column(ForeignKey("dic_users_roles.id"))

    dic_user_roles: Mapped["UserRole"] = relationship(
        back_populates="subscriptions",
    )

class UsToPrHistory(HistoryBase):
    __tablename__= "us_to_pr_history"

    project_id: Mapped[uuid_an] 
    user_id: Mapped[uuid_an] 
    dic_user_role_id: Mapped[int | None] 