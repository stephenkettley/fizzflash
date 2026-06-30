from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.subdomain_service import SubdomainService
from pydantic import BaseModel
from app.core.cache import get_cache, set_cache, delete_cache


router = APIRouter()


class SubdomainCreate(BaseModel):
    skill_id: int
    name: str


@router.post("/subdomains")
def create_subdomain(payload: SubdomainCreate, db: Session = Depends(get_db)):
    service = SubdomainService(db)
    result = service.create_subdomain(skill_id=payload.skill_id, name=payload.name)

    delete_cache(f"subdomains:skill:{payload.skill_id}")

    return result


@router.get("/skills/{skill_id}/subdomains")
def get_subdomains(skill_id: int, db: Session = Depends(get_db)):
    CACHE_KEY = f"subdomains:skill:{skill_id}"
    cached = get_cache(CACHE_KEY)

    if cached:
        return cached

    service = SubdomainService(db)
    subdomains = service.list_subdomains(skill_id)

    set_cache(CACHE_KEY, subdomains, ttl=300)

    return subdomains
