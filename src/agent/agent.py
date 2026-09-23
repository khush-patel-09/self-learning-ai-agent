from agent.action import Action
from agent.context.builder import ContextBuilder
from agent.conversation import Conversation
from agent.llm.base import LLM
from agent.memory.store import MemoryStore
from agent.observation import Observation
from agent.evaluator import Evaluator
from agent.result import AgentResult
from agent.task import Task
from agent.memory.memory import Memory


class Agent:
    """Core agent responsible for processing tasks."""

    def __init__(
        self,
        llm: LLM,
        context_builder: ContextBuilder,
        evaluator: Evaluator,
        memory_store: MemoryStore | None = None,
    ):
        self.llm = llm
        self.context_builder = context_builder
        self.evaluator = evaluator
        self.memory_store = memory_store

    def run(self, task: Task, conversation: Conversation) -> AgentResult:
        """Process a task using the conversation and memory context."""
        prompt = self.context_builder.build(
            task,
            conversation,
            self.memory_store,
        )

        response = self.llm.generate(prompt)

        conversation.add("assistant", response)

        action = Action("respond", response)
        observation = Observation(response)

        evaluation = self.evaluator.evaluate(
            task,
            action,
            observation,
        )

        return AgentResult(
            response,
            action,
            observation,
            evaluation,
        )

    def remember(self, content: str) -> None:
        """Store a memory when memory storage is configured."""
        if self.memory_store is not None:
            self.memory_store.add(Memory(content))