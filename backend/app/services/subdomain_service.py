from app.repositories.subdomain_repository import SubdomainRepository


class SubdomainService:

    def __init__(self, db):
        self.repo = SubdomainRepository(db)

    # -------------------------
    # CREATE SUBDOMAIN
    # -------------------------
    def create_subdomain(self, skill_id: int, name: str):
        return self.repo.create(skill_id, name)

    # -------------------------
    # GET SUBDOMAIN
    # -------------------------
    def get_subdomain(self, subdomain_id: int):
        return self.repo.get(subdomain_id)

    # -------------------------
    # LIST BY SKILL
    # -------------------------
    def list_subdomains(self, skill_id: int):
        return self.repo.get_by_skill(skill_id)

    # -------------------------
    # UPDATE STATS
    # -------------------------
    def update_stats(self, subdomain_id: int, is_correct: bool):
        return self.repo.update_stats(subdomain_id, is_correct)
