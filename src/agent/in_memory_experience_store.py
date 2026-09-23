from agent.experience import Experience
from agent.experience_store import ExperienceStore


class InMemoryExperienceStore(ExperienceStore):
    """Stores agent experiences in memory."""

    def __init__(self):
        self.experiences: list[Experience] = []

    def add(self, experience: Experience) -> None:
        """Store an experience."""
        self.experiences.append(experience)

    def get_all(self) -> list[Experience]:
        """Return all stored experiences."""
        return self.experiences.copy()