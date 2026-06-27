from app.repositories.skill_repository import SkillRepository


class SkillService:
    def __init__(self):
        self.repo = SkillRepository()

    def create_skill(self, name: str):
        return self.repo.create(name)

    def list_skills(self):
        return self.repo.list()

    def delete_skill(self, skill_id: int):
        return self.repo.delete(skill_id)
