from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.flashcard_service import FlashcardService
from pydantic import BaseModel


router = APIRouter()


class FlashcardCreate(BaseModel):
    subdomain_id: int
    front: str
    back: str


class FlashcardAnswer(BaseModel):
    is_correct: bool


@router.post("/flashcards")
def create_flashcard(payload: FlashcardCreate, db: Session = Depends(get_db)):

    service = FlashcardService(db)

    return service.create_manual_card(
        subdomain_id=payload.subdomain_id, front=payload.front, back=payload.back
    )


@router.get("/subdomains/{subdomain_id}/flashcards")
def get_flashcards(subdomain_id: int, db: Session = Depends(get_db)):

    service = FlashcardService(db)

    return service.get_subdomain_cards(subdomain_id)


@router.get("/flashcards/{card_id}")
def get_flashcard(card_id: int, db: Session = Depends(get_db)):

    service = FlashcardService(db)

    return service.get_card(card_id)


@router.delete("/flashcards/{card_id}")
def delete_flashcard(card_id: int, db: Session = Depends(get_db)):

    service = FlashcardService(db)

    return service.delete_card(card_id)


@router.post("/flashcards/{card_id}/answer")
def mark_answer(card_id: int, payload: FlashcardAnswer, db: Session = Depends(get_db)):

    service = FlashcardService(db)

    return service.mark_answer(card_id=card_id, is_correct=payload.is_correct)
