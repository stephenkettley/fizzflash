from sqlalchemy.orm import Session
from app.db.models import Skill


class SkillRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str):
        skill = Skill(name=name)

        self.db.add(skill)
        self.db.commit()
        self.db.refresh(skill)

        return skill

    def get(self, skill_id: int):
        return self.db.query(Skill).filter(Skill.id == skill_id).first()

    def get_by_name(self, name: str):
        return self.db.query(Skill).filter(Skill.name == name).first()

    def get_all(self):
        return self.db.query(Skill).all()

    def update_stats(self, skill_id: int, is_correct: bool):
        skill = self.get(skill_id)

        if not skill:
            return None

        skill.seen += 1

        if is_correct:
            skill.correct += 1
        else:
            skill.incorrect += 1

        self.db.commit()
        self.db.refresh(skill)

        return skill
