from app.repositories.flashcard_repository import FlashcardRepository


class FlashcardService:
    def __init__(self):
        self.repo = FlashcardRepository()

    def create_manual_card(self, subdomain_id: int, front: str, back: str):
        return self.repo.create(
            subdomain_id=subdomain_id, front=front, back=back, source="manual"
        )

    def create_ai_card(self, subdomain_id: int, front: str, back: str):
        return self.repo.create(
            subdomain_id=subdomain_id, front=front, back=back, source="ai"
        )

    def get_subdomain_cards(self, subdomain_id: int):
        return self.repo.list_by_subdomain(subdomain_id)

    def get_card(self, card_id: int):
        return self.repo.get(card_id)

    def delete_card(self, card_id: int):
        return self.repo.delete(card_id)

    def mark_answer(self, card_id: int, is_correct: bool):
        return self.repo.update_stats(card_id, is_correct)

    def get_skill_cards(self, skill_id: int, subdomain_service):
        subdomains = subdomain_service.list_subdomains(skill_id)

        all_cards = []

        for subdomain in subdomains:
            cards = self.repo.list_by_subdomain(subdomain["id"])
            all_cards.extend(cards)

        return all_cards
