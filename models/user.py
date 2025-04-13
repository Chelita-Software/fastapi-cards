from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(index=True, unique=True)
    name: str
    password: str
    role: str
