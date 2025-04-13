from uuid import UUID, uuid4

from sqlalchemy.dialects import sqlite
from sqlmodel import Column, Field, SQLModel


class Card(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    titulo: str
    descripcion: str
    img: str
    tags: list[str] = Field(sa_column=Column(sqlite.JSON))
