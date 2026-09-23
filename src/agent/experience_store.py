from abc import ABC, abstractmethod

from agent.experience import Experience


class ExperienceStore(ABC):
    """Interface for storing and retrieving agent experiences."""

    @abstractmethod
    def add(self, experience: Experience) -> None:
        """Store an experience."""
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[Experience]:
        """Return all stored experiences."""
        raise NotImplementedError

    @abstractmethod
    def search(self, query: str) -> list[Experience]:
        """Return experiences relevant to a query."""
        raise NotImplementedError