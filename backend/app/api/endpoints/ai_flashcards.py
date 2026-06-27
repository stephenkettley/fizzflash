from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.flashcard_service import FlashcardService
from pydantic import BaseModel


router = APIRouter()


class AIFlashcardRequest(BaseModel):
    subdomain_id: int
    topic: str


@router.post("/ai/flashcards")
def generate_ai_flashcards(payload: AIFlashcardRequest, db: Session = Depends(get_db)):

    flashcard_service = FlashcardService(db)

    # placeholder logic (you may already have AI logic here)
    return flashcard_service.repo.create(
        subdomain_id=payload.subdomain_id,
        front=f"AI: {payload.topic}",
        back="Generated answer",
    )
