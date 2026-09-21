from agent.memory.in_memory import InMemoryStore
from agent.memory.memory import Memory


def test_in_memory_store_adds_and_returns_memories():
    store = InMemoryStore()
    memory = Memory("The user prefers concise explanations.")

    store.add(memory)

    memories = store.get_all()

    assert len(memories) == 1
    assert memories[0] is memory