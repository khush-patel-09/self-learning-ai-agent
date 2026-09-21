from agent.context.builder import ContextBuilder
from agent.conversation import Conversation
from agent.task import Task
from agent.memory.in_memory import InMemoryStore
from agent.memory.memory import Memory


def test_context_builder_builds_prompt():
    conversation = Conversation()
    conversation.add("user", "My name is Khush.")
    conversation.add("assistant", "Nice to meet you, Khush.")

    task = Task("What is my name?")

    builder = ContextBuilder()

    result = builder.build(task, conversation)

    assert result == (
        "user: My name is Khush.\n"
        "assistant: Nice to meet you, Khush.\n"
        "user: What is my name?"
    )

def test_context_builder_includes_relevant_memories():
    builder = ContextBuilder()
    conversation = Conversation()
    memory_store = InMemoryStore()

    memory_store.add(
        Memory("The user prefers concise explanations.")
    )

    task = Task("Give a concise explanation of binary search.")

    context = builder.build(task, conversation, memory_store)

    assert "relevant memories:" in context
    assert "The user prefers concise explanations." in context