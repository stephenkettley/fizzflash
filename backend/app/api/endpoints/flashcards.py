from fastapi import APIRouter
from pydantic import BaseModel
from app.services.flashcard_service import FlashcardService

router = APIRouter()
service = FlashcardService()


class FlashcardCreate(BaseModel):
    subdomain_id: int
    front: str
    back: str


@router.post("/flashcards")
def create_flashcard(payload: FlashcardCreate):
    return service.create_manual_card(
        subdomain_id=payload.subdomain_id, front=payload.front, back=payload.back
    )


@router.get("/subdomains/{subdomain_id}/flashcards")
def get_flashcards(subdomain_id: int):
    return service.get_subdomain_cards(subdomain_id)


@router.get("/flashcards/{card_id}")
def get_flashcard(card_id: int):
    return service.get_card(card_id)


@router.delete("/flashcards/{card_id}")
def delete_flashcard(card_id: int):
    return service.delete_card(card_id)
