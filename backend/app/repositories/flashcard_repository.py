from sqlalchemy.orm import Session
from app.db.models import Flashcard


class FlashcardRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, subdomain_id: int, front: str, back: str, source: str = None):
        card = Flashcard(
            subdomain_id=subdomain_id, front=front, back=back, source=source
        )

        self.db.add(card)
        self.db.commit()
        self.db.refresh(card)

        return card

    def get(self, card_id: int):
        return self.db.query(Flashcard).filter(Flashcard.id == card_id).first()

    def list_by_subdomain(self, subdomain_id: int):
        return (
            self.db.query(Flashcard)
            .filter(Flashcard.subdomain_id == subdomain_id)
            .all()
        )

    def delete(self, card_id: int):
        card = self.get(card_id)

        if not card:
            return None

        self.db.delete(card)
        self.db.commit()

        return True

    def update_stats(self, card_id: int, is_correct: bool):
        card = self.get(card_id)

        if not card:
            return None

        card.seen += 1

        if is_correct:
            card.correct += 1
        else:
            card.incorrect += 1

        self.db.commit()
        self.db.refresh(card)

        return card
