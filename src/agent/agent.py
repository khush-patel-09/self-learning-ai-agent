from agent.action import Action
from agent.context.builder import ContextBuilder
from agent.conversation import Conversation
from agent.llm.base import LLM
from agent.memory.store import MemoryStore
from agent.observation import Observation
from agent.result import AgentResult
from agent.task import Task


class Agent:
    """Core agent responsible for processing tasks."""

    def __init__(
        self,
        llm: LLM,
        context_builder: ContextBuilder,
        memory_store: MemoryStore | None = None,
    ):
        self.llm = llm
        self.context_builder = context_builder
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

        return AgentResult(response, action, observation)