from typing import Dict, List, Optional


class FlashcardRepository:
    def __init__(self):
        self._cards: Dict[int, dict] = {}
        self._id_counter = 1

    def create(
        self, subdomain_id: int, front: str, back: str, source: str = "manual"
    ) -> dict:
        card = {
            "id": self._id_counter,
            "subdomain_id": subdomain_id,
            "front": front,
            "back": back,
            "source": source,
        }

        self._cards[self._id_counter] = card
        self._id_counter += 1

        return card

    def list_by_subdomain(self, subdomain_id: int) -> List[dict]:
        return [
            card
            for card in self._cards.values()
            if card["subdomain_id"] == subdomain_id
        ]

    def get(self, card_id: int) -> Optional[dict]:
        return self._cards.get(card_id)

    def delete(self, card_id: int) -> Optional[dict]:
        return self._cards.pop(card_id, None)
