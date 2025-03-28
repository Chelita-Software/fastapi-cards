from uuid import UUID

from sqlmodel import Session, select

from models import Card
from schemas import CardUpdateRequest
from utils.db import engine


class CardRepository:
    @classmethod
    def create(cls, titulo: str, descripcion: str, img: str, tags: list[str]) -> Card:
        with Session(engine) as session:
            card = Card(
                titulo=titulo,
                descripcion=descripcion,
                img=img,
                tags=tags,
            )
            session.add(card)
            session.commit()
            session.refresh(card)
        return card

    @classmethod
    def get_all(cls) -> list[Card]:
        with Session(engine) as session:
            statement = select(Card)
            result = session.exec(statement)
            cards = result.all()
        return cards
    
    @classmethod
    def update(cls, id: UUID, data: CardUpdateRequest) -> Card:
        with Session(engine) as session:
            card = session.get(Card, id)
            if not card:
                raise ValueError("Card not found")
            for attr, value in data.model_dump().items():
                if value is not None:
                    setattr(card, attr, value)
            session.add(card)
            session.commit()
            session.refresh(card)
        return card
    
    @classmethod
    def delete(cls, id: UUID) -> None:
        with Session(engine) as session:
            card = session.get(Card, id)
            if not card:
                raise ValueError("Card not found")
            session.delete(card)
            session.commit()
