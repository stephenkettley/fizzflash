from typing import Dict, List


class SkillRepository:
    def __init__(self):
        self._skills: Dict[int, dict] = {}
        self._id_counter = 1

    def create(self, name: str) -> dict:
        skill = {
            "id": self._id_counter,
            "name": name,
            "seen": 0,
            "correct": 0,
            "incorrect": 0,
            "accuracy": 0.0,
            "mastery": 0.0,
        }
        self._skills[self._id_counter] = skill
        self._id_counter += 1
        return skill

    def list(self) -> List[dict]:
        return list(self._skills.values())

    def get(self, skill_id: int):
        return self._skills.get(skill_id)

    def delete(self, skill_id: int):
        return self._skills.pop(skill_id, None)
