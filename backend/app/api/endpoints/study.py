from fastapi import APIRouter
from app.services.study_service import StudyService

router = APIRouter()

service = StudyService()


@router.post("/study/subdomain/{subdomain_id}")
def start_subdomain(subdomain_id: int):
    return service.start_subdomain_session(subdomain_id)


@router.post("/study/skill/{skill_id}")
def start_skill(skill_id: int):
    return service.start_skill_session(skill_id)


@router.get("/study/{session_id}/next")
def next_card(session_id: int):
    return service.get_next_card(session_id)
