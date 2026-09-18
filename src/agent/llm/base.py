from abc import ABC, abstractmethod


class LLM(ABC):
    """Interface for a language model."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from a prompt."""
        raise NotImplementedError