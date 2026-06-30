from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.flashcard_service import FlashcardService
from pydantic import BaseModel
from app.core.cache import get_cache, set_cache, delete_cache


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

    result = service.create_manual_card(
        subdomain_id=payload.subdomain_id, front=payload.front, back=payload.back
    )

    delete_cache(f"flashcards:subdomain:{payload.subdomain_id}")

    return result


@router.get("/subdomains/{subdomain_id}/flashcards")
def get_flashcards(subdomain_id: int, db: Session = Depends(get_db)):
    CACHE_KEY = f"flashcards:subdomain:{subdomain_id}"

    cached = get_cache(CACHE_KEY)
    if cached:
        return cached

    service = FlashcardService(db)
    flashcards = service.get_subdomain_cards(subdomain_id)

    set_cache(CACHE_KEY, flashcards, ttl=300)

    return flashcards


@router.get("/flashcards/{card_id}")
def get_flashcard(card_id: int, db: Session = Depends(get_db)):

    service = FlashcardService(db)

    return service.get_card(card_id)


@router.delete("/flashcards/{card_id}")
def delete_flashcard(card_id: int, db: Session = Depends(get_db)):

    service = FlashcardService(db)

    flashcard = service.get_card(card_id)

    result = service.delete_card(card_id)

    delete_cache(f"flashcards:subdomain:{flashcard.subdomain_id}")

    return result


@router.post("/flashcards/{card_id}/answer")
def mark_answer(card_id: int, payload: FlashcardAnswer, db: Session = Depends(get_db)):

    service = FlashcardService(db)

    return service.mark_answer(card_id=card_id, is_correct=payload.is_correct)


@router.get("/skills/{skill_id}/flashcards")
def get_flashcards_by_skill(skill_id: int, db: Session = Depends(get_db)):
    CACHE_KEY = f"flashcards:skill:{skill_id}"

    cached = get_cache(CACHE_KEY)
    if cached:
        return cached

    service = FlashcardService(db)

    subdomains = service.subdomain_service.repo.list_by_skill(skill_id)

    flashcards = []
    for subdomain in subdomains:
        flashcards.extend(service.get_subdomain_cards(subdomain.id))

    set_cache(CACHE_KEY, flashcards, ttl=300)

    return flashcards
