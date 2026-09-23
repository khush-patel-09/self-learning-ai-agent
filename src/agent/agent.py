from agent.action import Action
from agent.context.builder import ContextBuilder
from agent.conversation import Conversation
from agent.llm.base import LLM
from agent.memory.store import MemoryStore
from agent.observation import Observation
from agent.evaluator import Evaluator
from agent.result import AgentResult
from agent.experience import Experience
from agent.task import Task
from agent.memory.memory import Memory
from agent.reflector import Reflector
from agent.experience_store import ExperienceStore


class Agent:
    """Core agent responsible for processing tasks."""

    def __init__(
        self,
        llm: LLM,
        context_builder: ContextBuilder,
        evaluator: Evaluator,
        reflector: Reflector,
        memory_store: MemoryStore | None = None,
        experience_store: ExperienceStore | None = None,
    ):
        self.llm = llm
        self.context_builder = context_builder
        self.evaluator = evaluator
        self.reflector = reflector
        self.memory_store = memory_store
        self.experience_store = experience_store

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

        experience = Experience(
            task,
            action,
            observation,
            evaluation,
        )

        reflection = self.reflector.reflect(experience)
        
        if self.experience_store is not None:
            self.experience_store.add(experience)

        return AgentResult(
            response,
            action,
            observation,
            evaluation,
            reflection,
        )

    def remember(self, content: str) -> None:
        """Store a memory when memory storage is configured."""
        if self.memory_store is not None:
            self.memory_store.add(Memory(content))