from fastapi import APIRouter
from app.api.endpoints import health, skills, flashcards, subdomains, ai_flashcards

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(skills.router, tags=["skills"])
api_router.include_router(subdomains.router, tags=["subdomains"])
api_router.include_router(flashcards.router, tags=["flashcards"])
api_router.include_router(ai_flashcards.router, tags=["ai"])
