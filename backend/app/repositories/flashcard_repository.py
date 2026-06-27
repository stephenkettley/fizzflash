from typing import Dict, List, Optional
from datetime import datetime, timedelta


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
            "seen": 0,
            "correct": 0,
            "incorrect": 0,
            "ease_factor": 2.5,
            "interval": 1,
            "due_date": datetime.utcnow(),
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

    def update_stats(self, card_id: int, is_correct: bool):
        card = self._cards.get(card_id)

        if not card:
            return None

        card["seen"] += 1

        if is_correct:
            card["correct"] += 1
            # increase ease slightly
            card["ease_factor"] = min(card["ease_factor"] + 0.1, 3.0)
            # increase interval (spaced repetition growth)
            card["interval"] = max(1, int(card["interval"] * card["ease_factor"]))

        else:
            card["incorrect"] += 1
            # penalise
            card["ease_factor"] = max(card["ease_factor"] - 0.2, 1.3)
            # reset interval
            card["interval"] = 1

        # 🧠 SET NEXT DUE DATE
        card["due_date"] = datetime.utcnow() + timedelta(days=card["interval"])

        return card

    def get_study_queue(self, subdomain_id: int):
        cards = self.list_by_subdomain(subdomain_id)

        def score(card):
            # higher score = more likely to show
            return (
                (card["incorrect"] * 3)  # heavily prioritise weak cards
                + (1 / (card["interval"] + 1))
                + (3.0 - card["ease_factor"])  # harder cards appear more
            )

        return sorted(cards, key=score, reverse=True)

    def get_due_cards(self, subdomain_id: int):
        now = datetime.utcnow()

        cards = self.list_by_subdomain(subdomain_id)

        due_cards = [c for c in cards if c["due_date"] <= now]

        # fallback if nothing is due
        if not due_cards:
            return self.get_study_queue(subdomain_id)

        return due_cards
