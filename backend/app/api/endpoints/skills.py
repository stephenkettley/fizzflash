from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.skill_service import SkillService
from pydantic import BaseModel


router = APIRouter()


class SkillCreate(BaseModel):
    name: str


@router.post("/skills")
def create_skill(payload: SkillCreate, db: Session = Depends(get_db)):

    service = SkillService(db)

    return service.create_skill(payload.name)


@router.get("/skills")
def get_skills(db: Session = Depends(get_db)):

    service = SkillService(db)

    return service.list_skills()
