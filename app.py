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


# TODO: Implementar un sistema de autenticacion y autorizacion
# @app.get("/token")
# Implementar un modelo de usuario, username y password, tambien agregar roles
# Implementar logica para cifrar el password (Las contraseñas no se guardan en texto plano)
# Nota: La encriptacion es de dos sentidos, se encripta y se desencripta, el cifrado es de un solo sentido
# Implementar logica para verificar el usuario y el password
# Implementamos una funcion que te genere un JWT, y lo devuelva
# Lo guardamos en el local storage del navegador
# Luego hay que mandarlo en cada peticion al backend
# Authorization: Bearer <token>

# Implementar un middleware para verificar el token
# Un middleware es una funcion que se ejecuta antes de cada peticion
