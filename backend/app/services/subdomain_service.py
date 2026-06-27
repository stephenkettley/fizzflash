from app.repositories.subdomain_repository import SubdomainRepository


class SubdomainService:
    def __init__(self, db):
        self.repo = SubdomainRepository(db)

    def create_subdomain(self, skill_id: int, name: str):
        return self.repo.create(skill_id, name)

    def get_subdomain(self, subdomain_id: int):
        return self.repo.get(subdomain_id)

    def list_subdomains(self, skill_id: int):
        return self.repo.get_by_skill(skill_id)

    def update_stats(self, subdomain_id: int, is_correct: bool):
        return self.repo.update_stats(subdomain_id, is_correct)
