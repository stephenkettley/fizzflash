from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.skill_service import SkillService
from app.schemas.skill import SkillCreate, SkillResponse
from app.core.cache import get_cache, set_cache, delete_cache


router = APIRouter()

CACHE_KEY = "skills:all"


@router.post("/skills")
def create_skill(payload: SkillCreate, db: Session = Depends(get_db)):

    service = SkillService(db)

    return service.create_skill(payload.name)


from app.core.cache import set_cache

CACHE_KEY = "skills_all"


@router.get("/skills", response_model=list[SkillResponse])
def get_skills(db: Session = Depends(get_db)):

    service = SkillService(db)
    skills = service.list_skills()

    response = [SkillResponse.model_validate(s) for s in skills]
    cache_data = [s.model_dump() for s in response]

    set_cache(CACHE_KEY, cache_data, ttl=300)

    return response
