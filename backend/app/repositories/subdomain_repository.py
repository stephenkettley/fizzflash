from sqlalchemy.orm import Session
from app.db.models import Subdomain


class SubdomainRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, skill_id: int, name: str):
        subdomain = Subdomain(skill_id=skill_id, name=name)

        self.db.add(subdomain)
        self.db.commit()
        self.db.refresh(subdomain)

        return subdomain

    def get(self, subdomain_id: int):
        return self.db.query(Subdomain).filter(Subdomain.id == subdomain_id).first()

    def get_by_skill(self, skill_id: int):
        return self.db.query(Subdomain).filter(Subdomain.skill_id == skill_id).all()

    def update_stats(self, subdomain_id: int, is_correct: bool):
        subdomain = self.get(subdomain_id)

        if not subdomain:
            return None

        subdomain.seen += 1

        if is_correct:
            subdomain.correct += 1
        else:
            subdomain.incorrect += 1

        self.db.commit()
        self.db.refresh(subdomain)

        return subdomain
