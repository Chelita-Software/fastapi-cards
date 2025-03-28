from uuid import UUID

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from repository.card import CardRepository
from schemas import CardUpdateRequest
from models import Card

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/cards")
def create_card(data: Card) -> Card:
    """
    Create a new card.
    """
    return CardRepository.create(
        titulo=data.titulo,
        descripcion=data.descripcion,
        img=data.img,
        tags=data.tags,
    )


@app.get("/cards")
def get_all_cards() -> list[Card]:
    """
    Get all cards.
    """
    return CardRepository.get_all()


@app.patch("/cards/{id}")
def update_card(id: UUID, data: CardUpdateRequest) -> Card:
    """
    Update a card.
    """
    return CardRepository.update(
        id=id,
        data=data,
    )


@app.delete("/cards/{id}")
def delete_card(id: UUID) -> JSONResponse:
    """
    Delete a card.
    """
    CardRepository.delete(id=id)
    return JSONResponse(
        content={
            "success": True,
            "message": f"Card {id} deleted successfully"
        },
        status_code=200,
    )
