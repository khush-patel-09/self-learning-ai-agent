from agent.action import Action
from agent.context.builder import ContextBuilder
from agent.conversation import Conversation
from agent.llm.base import LLM
from agent.result import AgentResult
from agent.task import Task
from agent.observation import Observation


class Agent:
    """Core agent responsible for processing tasks."""

    def __init__(self, llm: LLM, context_builder: ContextBuilder):
        self.llm = llm
        self.context_builder = context_builder

    def run(self, task: Task, conversation: Conversation) -> AgentResult:
        """Process a task using the conversation context."""
        prompt = self.context_builder.build(task, conversation)

        response = self.llm.generate(prompt)

        conversation.add("assistant", response)

        action = Action("respond", response)
        observation = Observation(response)

        return AgentResult(response, action, observation)