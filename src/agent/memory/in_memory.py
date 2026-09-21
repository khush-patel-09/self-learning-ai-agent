from agent.memory.memory import Memory
from agent.memory.store import MemoryStore


class InMemoryStore(MemoryStore):
    """Stores memories in memory."""

    def __init__(self):
        self.memories: list[Memory] = []

    def add(self, memory: Memory) -> None:
        """Store a memory."""
        self.memories.append(memory)

    def get_all(self) -> list[Memory]:
        """Return all stored memories."""
        return self.memories.copy()

    def search(self, query: str) -> list[Memory]:
        """Return memories containing terms from the query."""
        query_terms = set(query.lower().split())

        return [
            memory
            for memory in self.memories
            if query_terms.intersection(set(memory.content.lower().split()))
        ]