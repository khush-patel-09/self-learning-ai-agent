from abc import ABC, abstractmethod

from agent.experience import Experience
from agent.reflection import Reflection


class Reflector(ABC):
    """Interface for reflecting on agent experiences."""

    @abstractmethod
    def reflect(self, experience: Experience) -> Reflection:
        """Generate a reflection from an experience."""
        raise NotImplementedError