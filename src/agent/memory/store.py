from abc import ABC, abstractmethod

from agent.memory.memory import Memory


class MemoryStore(ABC):
    """Interface for storing and retrieving memories."""

    @abstractmethod
    def add(self, memory: Memory) -> None:
        """Store a memory."""
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[Memory]:
        """Return all stored memories."""
        raise NotImplementedError