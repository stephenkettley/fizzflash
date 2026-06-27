from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.subdomain_service import SubdomainService
from pydantic import BaseModel


router = APIRouter()


# -------------------------
# SCHEMA
# -------------------------
class SubdomainCreate(BaseModel):
    skill_id: int
    name: str


# -------------------------
# CREATE SUBDOMAIN
# -------------------------
@router.post("/subdomains")
def create_subdomain(payload: SubdomainCreate, db: Session = Depends(get_db)):

    service = SubdomainService(db)

    return service.create_subdomain(skill_id=payload.skill_id, name=payload.name)


# -------------------------
# GET BY SKILL
# -------------------------
@router.get("/skills/{skill_id}/subdomains")
def get_subdomains(skill_id: int, db: Session = Depends(get_db)):

    service = SubdomainService(db)

    return service.list_subdomains(skill_id)
