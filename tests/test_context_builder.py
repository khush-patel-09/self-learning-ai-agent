from agent.context.builder import ContextBuilder
from agent.conversation import Conversation
from agent.task import Task
from agent.memory.in_memory import InMemoryStore
from agent.memory.memory import Memory
from agent.evaluation import Evaluation
from agent.experience import Experience
from agent.in_memory_experience_store import InMemoryExperienceStore
from agent.memory.local_embeddings import LocalEmbeddingModel
from agent.action import Action
from agent.observation import Observation


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

def test_context_builder_includes_relevant_experiences():
    builder = ContextBuilder()
    conversation = Conversation()

    experience_store = InMemoryExperienceStore(
        LocalEmbeddingModel(),
        similarity_threshold=0.3,
    )

    experience = Experience(
        Task("Calculate 2 + 2"),
        Action("answer", "4"),
        Observation("4"),
        Evaluation(
            True,
            "The answer was correct.",
        ),
    )

    experience_store.add(experience)

    task = Task("Solve a simple arithmetic calculation.")

    context = builder.build(
        task,
        conversation,
        experience_store=experience_store,
    )

    assert "relevant experiences:" in context
    assert "Calculate 2 + 2" in context
    assert "The answer was correct." in context