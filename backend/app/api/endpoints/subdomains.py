from fastapi import APIRouter
from pydantic import BaseModel
from app.services.subdomain_service import SubdomainService

router = APIRouter()
service = SubdomainService()


class SubdomainCreate(BaseModel):
    skill_id: int
    name: str


@router.post("/subdomains")
def create_subdomain(payload: SubdomainCreate):
    return service.create_subdomain(skill_id=payload.skill_id, name=payload.name)


@router.get("/skills/{skill_id}/subdomains")
def get_subdomains(skill_id: int):
    return service.list_subdomains(skill_id)


@router.get("/subdomains/{subdomain_id}")
def get_subdomain(subdomain_id: int):
    return service.get_subdomain(subdomain_id)


@router.delete("/subdomains/{subdomain_id}")
def delete_subdomain(subdomain_id: int):
    return service.delete_subdomain(subdomain_id)
