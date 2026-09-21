from agent.memory.memory import Memory
from agent.memory.store import MemoryStore


def test_memory_store_defines_storage_interface():
    assert hasattr(MemoryStore, "add")
    assert hasattr(MemoryStore, "get_all")