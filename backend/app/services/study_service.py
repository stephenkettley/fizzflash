import random
from app.services.flashcard_service import FlashcardService
from app.services.subdomain_service import SubdomainService


class StudyService:
    def __init__(self):
        self.flashcard_service = FlashcardService()
        self.subdomain_service = SubdomainService()

        self.sessions = {}
        self.session_counter = 1

    def start_subdomain_session(self, subdomain_id: int):

        cards = self.flashcard_service.repo.get_due_cards(subdomain_id)

        session = {
            "id": self.session_counter,
            "cards": cards,
            "index": 0,
            "results": [],
        }

        self.sessions[self.session_counter] = session

        self.session_counter += 1

        return session

    def start_skill_session(self, skill_id: int):
        subdomains = self.subdomain_service.list_subdomains(skill_id)

        cards = self.flashcard_service.get_skill_cards(skill_id, self.subdomain_service)
        random.shuffle(cards)

        session = {"id": self.session_counter, "cards": cards, "index": 0}

        self.sessions[self.session_counter] = session
        self.session_counter += 1

        return session

    def get_next_card(self, session_id: int):
        session = self.sessions.get(session_id)

        if not session:
            return None

        if session["index"] >= len(session["cards"]):
            return {"done": True}

        card = session["cards"][session["index"]]
        session["index"] += 1

        return {"done": False, "card": card}
