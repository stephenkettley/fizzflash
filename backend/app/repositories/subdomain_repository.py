from typing import Dict, List, Optional


class SubdomainRepository:
    def __init__(self):
        self._subdomains: Dict[int, dict] = {}
        self._id_counter = 1

    def create(self, skill_id: int, name: str) -> dict:
        subdomain = {
            "id": self._id_counter,
            "skill_id": skill_id,
            "name": name,
            "seen": 0,
            "correct": 0,
            "incorrect": 0,
            "accuracy": 0.0,
            "mastery": 0.0,
        }

        self._subdomains[self._id_counter] = subdomain
        self._id_counter += 1

        return subdomain

    def list_by_skill(self, skill_id: int) -> List[dict]:
        return [s for s in self._subdomains.values() if s["skill_id"] == skill_id]

    def get(self, subdomain_id: int) -> Optional[dict]:
        return self._subdomains.get(subdomain_id)

    def delete(self, subdomain_id: int) -> Optional[dict]:
        return self._subdomains.pop(subdomain_id, None)
