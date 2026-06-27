from app.repositories.subdomain_repository import SubdomainRepository


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
