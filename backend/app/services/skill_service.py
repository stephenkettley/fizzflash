from fastapi import HTTPException
from app.repositories.skill_repository import SkillRepository


class SkillService:
    def __init__(self):
        self.repo = SkillRepository()

    def create_skill(self, name: str):
        normalized_name = name.strip().lower()

        existing_skills = self.repo.list()

        for skill in existing_skills:
            if skill["name"] == normalized_name:
                raise HTTPException(status_code=409, detail="Skill already exists")

        return self.repo.create(normalized_name)

    def list_skills(self):
        return self.repo.list()

    def delete_skill(self, skill_id: int):
        return self.repo.delete(skill_id)
