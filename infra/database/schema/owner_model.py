from datetime import datetime
import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from infra.database.session_db import engine


class OwnerModel(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(max_length=255)
    last_name: str | None = Field(default=None, max_length=255)
    id_card: int
    phone: int
    date_of_birth: datetime = None
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    password: str | None = Field(default=None, min_length=8, max_length=40)
