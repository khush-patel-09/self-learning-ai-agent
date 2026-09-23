from abc import ABC, abstractmethod


class EmbeddingModel(ABC):
    """Interface for converting text into embedding vectors."""

    @abstractmethod
    def embed(self, text: str) -> list[float]:
        """Convert text into an embedding vector."""
        raise NotImplementedError