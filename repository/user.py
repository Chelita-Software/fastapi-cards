from uuid import UUID

from sqlmodel import Session, select

from models import User
from schemas import UserUpdateRequest
from utils.db import engine

class UserRepository:
    @classmethod
    def create(cls, email: str, name: str, password: str, role: str) -> User:
        with Session(engine) as session:
            user = User(
                email=email,
                name=name,
                password=password,
                role=role,
            )
            session.add(user)
            session.commit()
            session.refresh(user)
        return user
    
    @classmethod
    def get_all(cls) -> list[User]:
        with Session(engine) as session:
            statement = select(User)
            result = session.exec(statement)
            users = result.all()
        return users
    
    @classmethod
    def get(cls, id: str) -> User | None:
        with Session(engine) as session:
            user = session.get(User, id)
        return user
    
    @classmethod
    def get_by_email(cls, email: str) -> User | None:
        with Session(engine) as session:
            statement = select(User).where(User.email == email)
            result = session.exec(statement)
            user = result.one_or_none()
        return user
    
    @classmethod
    def update(cls, id: UUID, data: UserUpdateRequest) -> User:
        with Session(engine) as session:
            user = session.get(User, id)
            if not user:
                raise ValueError("User not found")
            for attr, value in data.model_dump().items():
                if value is not None:
                    setattr(user, attr, value)
            session.add(user)
            session.commit()
            session.refresh(user)
        return user


    @classmethod
    def delete(cls, id: str) -> None:
        with Session(engine) as session:
            user = session.get(User, id)
            session.delete(user)
            session.commit()
