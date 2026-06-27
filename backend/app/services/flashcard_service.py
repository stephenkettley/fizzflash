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
