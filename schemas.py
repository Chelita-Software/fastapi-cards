from pydantic import BaseModel

class CardUpdateRequest(BaseModel):
    """Request model for updating a card."""
    title: str | None = None
    descripcion: str | None = None
    img: str | None = None
    tags: list[str] | None = None
