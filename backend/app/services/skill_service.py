from app.repositories.skill_repository import SkillRepository
from app.utils.stats import compute_accuracy


class SkillService:

    def __init__(self, db):
        self.repo = SkillRepository(db)

    def create_skill(self, name: str):
        return self.repo.create(name.lower())

    def get_skill(self, skill_id: int):
        return self.repo.get(skill_id)

    def list_skills(self):
        return self.repo.get_all()

    def update_stats(self, skill_id: int, is_correct: bool):
        skill = self.repo.update_stats(skill_id, is_correct)

        if not skill:
            return None

        # accuracy
        skill.accuracy = compute_accuracy(skill.correct, skill.seen)

        # mastery (simple weighted model)
        skill.mastery = skill.accuracy * 0.7 + min(skill.correct / 50, 1.0) * 0.3

        return skill
