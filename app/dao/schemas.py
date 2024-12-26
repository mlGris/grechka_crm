from uuid import UUID
from pydantic import BaseModel, ConfigDict


class UserPydantic(BaseModel):
    id: UUID
    name: str
    mid_name: str | None 
    surname: str | None 
    login: str
    password: str
    email: str
    phone_num: str | None = None

    model_config = ConfigDict(from_attributes=True)

class UpdateUserPydantic(BaseModel):
    id: UUID | None = None
    name: str | None = None
    mid_name: str | None = None
    surname: str | None = None
    login: str | None = None
    password: str | None = None
    email: str | None = None
    phone_num: str | None = None

    model_config = ConfigDict(from_attributes=True)

class UsernameIdPydantic(BaseModel):
    id: UUID
    name: str

    model_config = ConfigDict(from_attributes=True)