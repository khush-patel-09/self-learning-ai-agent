from agent.memory.embeddings import EmbeddingModel
from agent.memory.memory import Memory
from agent.memory.similarity import cosine_similarity
from agent.memory.store import MemoryStore


class InMemoryStore(MemoryStore):
    """Stores memories in memory and supports semantic search."""

    def __init__(
        self,
        embedding_model: EmbeddingModel | None = None,
        similarity_threshold: float = 0.5,
    ):
        self.memories: list[Memory] = []
        self.embedding_model = embedding_model
        self.similarity_threshold = similarity_threshold
        self.embeddings: dict[int, list[float]] = {}

    def add(self, memory: Memory) -> None:
        """Store a memory and its embedding when available."""
        self.memories.append(memory)

        if self.embedding_model is not None:
            self.embeddings[id(memory)] = self.embedding_model.embed(
                memory.content
            )

    def get_all(self) -> list[Memory]:
        """Return all stored memories."""
        return self.memories.copy()

    def search(self, query: str) -> list[Memory]:
        """Return memories relevant to a query."""
        if self.embedding_model is None:
            query_terms = set(query.lower().split())

            return [
                memory
                for memory in self.memories
                if query_terms.intersection(
                    set(memory.content.lower().split())
                )
            ]

        query_embedding = self.embedding_model.embed(query)

        scored_memories = [
            (
                cosine_similarity(
                    query_embedding,
                    self.embeddings[id(memory)],
                ),
                memory,
            )
            for memory in self.memories
        ]

        scored_memories = [
            (score, memory)
            for score, memory in scored_memories
            if score >= self.similarity_threshold
        ]

        scored_memories.sort(key=lambda item: item[0], reverse=True)

        return [memory for _, memory in scored_memories]