from app.repositories.subdomain_repository import SubdomainRepository
from app.utils.stats import compute_accuracy


class SubdomainService:
    def __init__(self):
        self.repo = SubdomainRepository()

    def create_subdomain(self, skill_id: int, name: str):
        normalized_name = name.strip().lower()
        return self.repo.create(skill_id, normalized_name)

    def list_subdomains(self, skill_id: int):
        return self.repo.list_by_skill(skill_id)

    def get_subdomain(self, subdomain_id: int):
        return self.repo.get(subdomain_id)

    def delete_subdomain(self, subdomain_id: int):
        return self.repo.delete(subdomain_id)

    def update_stats(self, subdomain_id: int, is_correct: bool):
        subdomain = self.repo.get(subdomain_id)

        if not subdomain:
            return None

        subdomain["seen"] += 1
        if is_correct:
            subdomain["correct"] += 1

        else:
            subdomain["incorrect"] += 1

        # 📊 accuracy
        subdomain["accuracy"] = compute_accuracy(
            subdomain["correct"], subdomain["seen"]
        )

        # 🧠 mastery (slightly more sensitive than skill)
        subdomain["mastery"] = (
            subdomain["accuracy"] * 0.8 + min(subdomain["correct"] / 20, 1.0) * 0.2
        )

        return subdomain
