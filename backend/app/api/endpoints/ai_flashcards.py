from fastapi import APIRouter
from app.services.flashcard_service import FlashcardService
from app.services.subdomain_service import SubdomainService
from app.services.skill_service import SkillService

router = APIRouter()

flashcard_service = FlashcardService()
subdomain_service = SubdomainService()
skill_service = SkillService()


@router.post("/flashcards/ai")
def generate_ai_flashcards(subdomain_id: int, count: int = 5):
    subdomain = subdomain_service.get_subdomain(subdomain_id)
    skill = skill_service.repo.get(subdomain["skill_id"])

    return flashcard_service.generate_ai_flashcards(
        subdomain=subdomain, skill=skill, count=count
    )
