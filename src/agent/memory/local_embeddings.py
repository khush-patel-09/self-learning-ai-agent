from sentence_transformers import SentenceTransformer

from agent.memory.embeddings import EmbeddingModel


class LocalEmbeddingModel(EmbeddingModel):
    """Embedding model running locally with Sentence Transformers."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, text: str) -> list[float]:
        """Convert text into an embedding vector."""
        vector = self.model.encode(text)

        return vector.tolist()