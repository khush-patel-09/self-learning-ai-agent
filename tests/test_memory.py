from agent.memory.memory import Memory


def test_memory_stores_content():
    memory = Memory("The user prefers concise explanations.")

    assert memory.content == "The user prefers concise explanations."