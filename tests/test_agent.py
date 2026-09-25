from agent.action import Action
from agent.agent import Agent
from agent.context.builder import ContextBuilder
from agent.conversation import Conversation
from agent.evaluation import Evaluation
from agent.evaluator import Evaluator
from agent.experience import Experience
from agent.llm.fake import FakeLLM
from agent.memory.in_memory import InMemoryStore
from agent.memory.local_embeddings import LocalEmbeddingModel
from agent.memory.memory import Memory
from agent.in_memory_experience_store import InMemoryExperienceStore
from agent.observation import Observation
from agent.reflection import Reflection
from agent.reflector import Reflector
from agent.result import AgentResult
from agent.simple_evaluator import SimpleEvaluator
from agent.simple_reflector import SimpleReflector
from agent.task import Task


def test_agent_runs_task_using_llm():
    llm = FakeLLM("4")
    agent = Agent(
        llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
    )
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
    agent = Agent(
        llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
    )

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
    agent = Agent(
        llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
    )

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

    memory_store.add(
        Memory("The user prefers concise explanations.")
    )

    agent = Agent(
        llm,
        context_builder,
        SimpleEvaluator(),
        SimpleReflector(),
        memory_store,
    )

    task = Task("Give a concise explanation.")
    conversation = Conversation()

    agent.run(task, conversation)

    assert "The user prefers concise explanations." in llm.last_prompt


def test_agent_can_store_memory():
    llm = FakeLLM("4")
    context_builder = ContextBuilder()
    memory_store = InMemoryStore()

    agent = Agent(
        llm,
        context_builder,
        SimpleEvaluator(),
        SimpleReflector(),
        memory_store,
    )

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

    agent = Agent(
        llm,
        context_builder,
        SimpleEvaluator(),
        SimpleReflector(),
        memory_store,
    )

    task = Task("Please keep the explanation concise.")
    conversation = Conversation()

    agent.run(task, conversation)

    assert "The user prefers concise explanations." in llm.last_prompt


def test_agent_uses_injected_evaluator():
    class TestEvaluator(Evaluator):
        def __init__(self):
            self.called = False

        def evaluate(self, task, action, observation):
            self.called = True
            return Evaluation(
                False,
                "Test evaluator feedback.",
            )

    llm = FakeLLM("4")
    evaluator = TestEvaluator()

    agent = Agent(
        llm,
        ContextBuilder(),
        evaluator,
        SimpleReflector(),
    )

    result = agent.run(
        Task("Calculate 2 + 2"),
        Conversation(),
    )

    assert evaluator.called is True
    assert result.evaluation.success is False
    assert result.evaluation.feedback == "Test evaluator feedback."

def test_agent_uses_injected_reflector():
    class TestReflector(Reflector):
        def __init__(self):
            self.called = False

        def reflect(self, experience):
            self.called = True
            return Reflection(
                "Test reflection insight.",
            )

    llm = FakeLLM("4")
    reflector = TestReflector()

    agent = Agent(
        llm,
        ContextBuilder(),
        SimpleEvaluator(),
        reflector,
    )

    result = agent.run(
        Task("Calculate 2 + 2"),
        Conversation(),
    )

    assert reflector.called is True
    assert result.reflection.insight == "Test reflection insight."

def test_agent_stores_experience():
    llm = FakeLLM("4")
    experience_store = InMemoryExperienceStore()

    agent = Agent(
        llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
        experience_store=experience_store,
    )

    agent.run(
        Task("Calculate 2 + 2"),
        Conversation(),
    )

    experiences = experience_store.get_all()

    assert len(experiences) == 1
    assert experiences[0].task.description == "Calculate 2 + 2"
    assert experiences[0].action.input == "4"
    assert experiences[0].evaluation.success is True

def test_agent_includes_relevant_experience_in_context():
    llm = FakeLLM("4")
    experience_store = InMemoryExperienceStore()

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

    agent = Agent(
        llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
        experience_store=experience_store,
    )

    agent.run(
        Task("Calculate 2+2"),
        Conversation(),
    )

    assert "relevant experiences:" in llm.last_prompt
    assert "Calculate 2 + 2" in llm.last_prompt
    assert "The answer was correct." in llm.last_prompt

def test_agent_stores_reflection_with_experience():
    llm = FakeLLM("4")
    experience_store = InMemoryExperienceStore()

    agent = Agent(
        llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
        experience_store=experience_store,
    )

    agent.run(
        Task("Calculate 2 + 2"),
        Conversation(),
    )

    experiences = experience_store.get_all()

    assert len(experiences) == 1
    assert experiences[0].reflection is not None
    assert experiences[0].reflection.insight == (
        "For the task 'Calculate 2 + 2', "
        "the approach produced a successful outcome: "
        "The agent produced an observable result."
    )

def test_agent_reuses_learned_reflection_for_similar_task():
    experience_store = InMemoryExperienceStore()

    first_llm = FakeLLM("4")
    first_agent = Agent(
        first_llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
        experience_store=experience_store,
    )

    first_agent.run(
        Task("Calculate 2 + 2"),
        Conversation(),
    )

    second_llm = FakeLLM("5")
    second_agent = Agent(
        second_llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
        experience_store=experience_store,
    )

    second_agent.run(
        Task("Calculate 2 + 2"),
        Conversation(),
    )

    assert "relevant experiences:" in second_llm.last_prompt
    assert "For the task 'Calculate 2 + 2', " in second_llm.last_prompt

def test_agent_retrieves_semantically_similar_experience():
    embedding_model = LocalEmbeddingModel()
    experience_store = InMemoryExperienceStore(embedding_model)

    experience = Experience(
        Task("Calculate the sum of two numbers"),
        Action("answer", "4"),
        Observation("4"),
        Evaluation(
            True,
            "The calculation was correct.",
        ),
        Reflection(
            "Direct arithmetic produced the correct result.",
        ),
    )

    experience_store.add(experience)

    llm = FakeLLM("5")

    agent = Agent(
        llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
        experience_store=experience_store,
    )

    agent.run(
        Task("What is the result when adding two values?"),
        Conversation(),
    )

    assert "relevant experiences:" in llm.last_prompt
    assert "Direct arithmetic produced the correct result." in llm.last_prompt

def test_agent_includes_outcome_and_reflection_in_experience_context():
    experience_store = InMemoryExperienceStore()

    experience = Experience(
        Task("Calculate 2 + 2"),
        Action("answer", "4"),
        Observation("4"),
        Evaluation(
            True,
            "The answer was correct.",
        ),
        Reflection(
            "For the task 'Calculate 2 + 2', "
            "the approach produced the correct result.",
        ),
    )

    experience_store.add(experience)

    llm = FakeLLM("4")

    agent = Agent(
        llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
        experience_store=experience_store,
    )

    agent.run(
        Task("Calculate 2 + 2"),
        Conversation(),
    )

    assert (
        "outcome: success - The answer was correct."
        in llm.last_prompt
    )
    assert (
        "For the task 'Calculate 2 + 2', "
        "the approach produced the correct result."
    ) in llm.last_prompt

def test_agent_reuses_failed_experience_reflection():
    experience_store = InMemoryExperienceStore()

    experience = Experience(
        Task("Calculate 2 + 2"),
        Action("answer", ""),
        Observation(""),
        Evaluation(
            False,
            "The agent produced an empty result.",
        ),
        Reflection(
            "For the task 'Calculate 2 + 2', "
            "the approach should be improved: "
            "The agent produced an empty result.",
        ),
    )

    experience_store.add(experience)

    llm = FakeLLM("4")

    agent = Agent(
        llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
        experience_store=experience_store,
    )

    agent.run(
        Task("Calculate 2 + 2"),
        Conversation(),
    )

    assert "outcome: failure" in llm.last_prompt
    assert (
        "the approach should be improved: "
        "The agent produced an empty result."
    ) in llm.last_prompt