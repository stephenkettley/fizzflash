from app.repositories.flashcard_repository import FlashcardRepository
from app.services.subdomain_service import SubdomainService
from app.services.skill_service import SkillService


class FlashcardService:

    def __init__(self, db):
        self.repo = FlashcardRepository(db)
        self.subdomain_service = SubdomainService(db)
        self.skill_service = SkillService(db)

    # -------------------------
    # CREATE MANUAL CARD
    # -------------------------
    def create_manual_card(self, subdomain_id: int, front: str, back: str):
        return self.repo.create(subdomain_id=subdomain_id, front=front, back=back)

    # -------------------------
    # GET CARD
    # -------------------------
    def get_card(self, card_id: int):
        return self.repo.get(card_id)

    # -------------------------
    # DELETE CARD
    # -------------------------
    def delete_card(self, card_id: int):
        return self.repo.delete(card_id)

    # -------------------------
    # GET BY SUBDOMAIN
    # -------------------------
    def get_subdomain_cards(self, subdomain_id: int):
        return self.repo.list_by_subdomain(subdomain_id)

    # -------------------------
    # MARK ANSWER (CORE LEARNING FLOW)
    # -------------------------
    def mark_answer(self, card_id: int, is_correct: bool):
        """
        This is the central learning pipeline:
        - updates flashcard stats
        - updates subdomain stats
        - updates skill stats
        """

        card = self.repo.update_stats(card_id, is_correct)

        if not card:
            return None

        subdomain = self.subdomain_service.get_subdomain(card.subdomain_id)
        skill_id = subdomain.skill_id

        self.subdomain_service.update_stats(card.subdomain_id, is_correct)
        self.skill_service.update_stats(skill_id, is_correct)

        return card
