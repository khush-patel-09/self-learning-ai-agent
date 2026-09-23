from agent import result
from agent.agent import Agent
from agent.conversation import Conversation
from agent.llm.fake import FakeLLM
from agent.task import Task
from agent.context.builder import ContextBuilder
from agent.result import AgentResult
from agent.memory.in_memory import InMemoryStore
from agent.memory.memory import Memory
from agent.memory.local_embeddings import LocalEmbeddingModel
from agent.memory.similarity import cosine_similarity


def test_agent_runs_task_using_llm():
    llm = FakeLLM("4")
    agent = Agent(llm, ContextBuilder())
    task = Task("Calculate 2 + 2")
    conversation = Conversation()

    result = agent.run(task, conversation)

    assert isinstance(result, AgentResult)
    assert result.response == "4"
    assert result.action.name == "respond"
    assert result.action.input == "4"
    assert result.observation.content == "4"


def test_agent_passes_conversation_to_llm():
    llm = FakeLLM("response")
    agent = Agent(llm, ContextBuilder())

    conversation = Conversation()
    conversation.add("user", "My name is Khush.")

    task = Task("What is my name?")

    agent.run(task, conversation)

    assert llm.last_prompt == (
        "user: My name is Khush.\n"
        "user: What is my name?"
    )


def test_agent_adds_response_to_conversation():
    llm = FakeLLM("4")
    agent = Agent(llm, ContextBuilder())

    conversation = Conversation()
    task = Task("Calculate 2 + 2")

    agent.run(task, conversation)

    assert len(conversation.messages) == 1
    assert conversation.messages[0].role == "assistant"
    assert conversation.messages[0].content == "4"

def test_agent_uses_memory_store():
    llm = FakeLLM("4")
    context_builder = ContextBuilder()
    memory_store = InMemoryStore()

    memory_store.add(Memory("The user prefers concise explanations."))

    agent = Agent(llm, context_builder, memory_store)

    task = Task("Give a concise explanation.")
    conversation = Conversation()

    agent.run(task, conversation)

    assert "The user prefers concise explanations." in llm.last_prompt

def test_agent_can_store_memory():
    llm = FakeLLM("4")
    context_builder = ContextBuilder()
    memory_store = InMemoryStore()

    agent = Agent(llm, context_builder, memory_store)

    agent.remember("The user prefers concise explanations.")

    memories = memory_store.get_all()

    assert len(memories) == 1
    assert memories[0].content == "The user prefers concise explanations."

def test_agent_includes_semantically_relevant_memory():
    llm = FakeLLM("4")
    context_builder = ContextBuilder()
    embedding_model = LocalEmbeddingModel()

    memory_store = InMemoryStore(
        embedding_model,
        similarity_threshold=0.3,
    )

    memory_store.add(
        Memory("The user prefers concise explanations.")
    )

    agent = Agent(llm, context_builder, memory_store)

    task = Task("Please keep the explanation concise.")
    conversation = Conversation()

    agent.run(task, conversation)

    assert "The user prefers concise explanations." in llm.last_prompt