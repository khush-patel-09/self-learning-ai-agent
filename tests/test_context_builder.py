from agent.context.builder import ContextBuilder
from agent.conversation import Conversation
from agent.task import Task


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