from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.session import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    seen = Column(Integer, default=0)
    correct = Column(Integer, default=0)
    incorrect = Column(Integer, default=0)

    accuracy = Column(Float, default=0.0)
    mastery = Column(Float, default=0.0)


class Subdomain(Base):
    __tablename__ = "subdomains"

    id = Column(Integer, primary_key=True, index=True)
    skill_id = Column(Integer, ForeignKey("skills.id"))

    name = Column(String)

    seen = Column(Integer, default=0)
    correct = Column(Integer, default=0)
    incorrect = Column(Integer, default=0)

    accuracy = Column(Float, default=0.0)
    mastery = Column(Float, default=0.0)


class Flashcard(Base):
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True, index=True)
    subdomain_id = Column(Integer, ForeignKey("subdomains.id"))

    front = Column(String)
    back = Column(String)
    source = Column(String, nullable=True)

    seen = Column(Integer, default=0)
    correct = Column(Integer, default=0)
    incorrect = Column(Integer, default=0)

    ease_factor = Column(Float, default=2.5)
    interval = Column(Integer, default=1)
