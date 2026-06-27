from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.services.study_service import StudyService

router = APIRouter()


@router.post("/study/{subdomain_id}/start")
def start_session(subdomain_id: int, db: Session = Depends(get_db)):

    service = StudyService(db)

    return service.start_subdomain_session(subdomain_id)
