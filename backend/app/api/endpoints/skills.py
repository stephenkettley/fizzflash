from fastapi import APIRouter
from pydantic import BaseModel
from app.services.skill_service import SkillService

router = APIRouter()
service = SkillService()


class SkillCreate(BaseModel):
    name: str


@router.post("/skills")
def create_skill(payload: SkillCreate):
    return service.create_skill(payload.name)


@router.get("/skills")
def list_skills():
    return service.list_skills()


@router.delete("/skills/{skill_id}")
def delete_skill(skill_id: int):
    return service.delete_skill(skill_id)
