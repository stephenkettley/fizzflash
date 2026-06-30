from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.skill_service import SkillService
from pydantic import BaseModel
from app.core.cache import get_cache, set_cache, delete_cache


router = APIRouter()

CACHE_KEY = "skills:all"


class SkillCreate(BaseModel):
    name: str


@router.post("/skills")
def create_skill(payload: SkillCreate, db: Session = Depends(get_db)):

    service = SkillService(db)

    return service.create_skill(payload.name)


@router.get("/skills")
def get_skills(db: Session = Depends(get_db)):
    cached = get_cache(CACHE_KEY)  # using redis

    if cached:
        return cached

    service = SkillService(db)
    skills = service.list_skills()

    set_cache(CACHE_KEY, skills, ttl=300)

    return skills
