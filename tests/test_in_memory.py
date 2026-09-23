from agent.memory.in_memory import InMemoryStore
from agent.memory.memory import Memory
from agent.memory.embeddings import EmbeddingModel

class FakeEmbeddingModel(EmbeddingModel):
    def embed(self, text: str) -> list[float]:
        if "concise" in text.lower() or "short" in text.lower():
            return [1.0, 0.0]

        return [0.0, 1.0]


def test_in_memory_store_adds_and_returns_memories():
    store = InMemoryStore()
    memory = Memory("The user prefers concise explanations.")

    store.add(memory)

    memories = store.get_all()

    assert len(memories) == 1
    assert memories[0] is memory


def test_in_memory_store_searches_memories():
    store = InMemoryStore()

    relevant = Memory("The user prefers concise explanations.")
    unrelated = Memory("The user enjoys playing cricket.")

    store.add(relevant)
    store.add(unrelated)

    memories = store.search("concise explanations")

    assert memories == [relevant]

def test_in_memory_store_searches_semantically():
    embedding_model = FakeEmbeddingModel()
    store = InMemoryStore(embedding_model)

    relevant = Memory("The user prefers concise explanations.")
    unrelated = Memory("The user enjoys playing cricket.")

    store.add(relevant)
    store.add(unrelated)

    memories = store.search("Keep the answer short.")

    assert memories[0] is relevant