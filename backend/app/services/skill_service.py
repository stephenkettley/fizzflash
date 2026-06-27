from fastapi import HTTPException
from app.repositories.skill_repository import SkillRepository
from app.utils.stats import compute_accuracy


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

    def update_stats(self, skill_id: int, is_correct: bool):
        skill = self.repo.get(skill_id)

        if not skill:
            return None

        skill["seen"] += 1

        if is_correct:
            skill["correct"] += 1
        else:
            skill["incorrect"] += 1

        # 📊 accuracy (shared util)
        skill["accuracy"] = compute_accuracy(skill["correct"], skill["seen"])

        # 🧠 mastery (long-term signal)
        skill["mastery"] = (
            skill["accuracy"] * 0.7 + min(skill["correct"] / 50, 1.0) * 0.3
        )

        return skill
