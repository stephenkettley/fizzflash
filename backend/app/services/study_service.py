from app.services.flashcard_service import FlashcardService


class StudyService:
    def __init__(self, db):
        self.db = db
        self.flashcard_service = FlashcardService(db)
        self.sessions = {}
        self.session_counter = 1

    def start_subdomain_session(self, subdomain_id: int):
        cards = self.flashcard_service.get_subdomain_cards(subdomain_id)

        session = {
            "id": self.session_counter,
            "subdomain_id": subdomain_id,
            "cards": cards,
            "index": 0,
            "results": [],
        }

        self.sessions[self.session_counter] = session
        self.session_counter += 1

        return session

    def mark_answer(self, session_id: int, card_id: int, is_correct: bool):

        card = self.flashcard_service.mark_answer(card_id, is_correct)

        session = self.sessions.get(session_id)

        if session:
            session["results"].append({"card_id": card_id, "is_correct": is_correct})

        return card
