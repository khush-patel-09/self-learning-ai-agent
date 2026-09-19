from agent.context.builder import ContextBuilder
from agent.conversation import Conversation
from agent.llm.base import LLM
from agent.task import Task


class Agent:
    """Core agent responsible for processing tasks."""

    def __init__(self, llm: LLM):
        self.llm = llm
        self.context_builder = ContextBuilder()

    def run(self, task: Task, conversation: Conversation) -> str:
        """Process a task using the conversation context."""
        prompt = self.context_builder.build(task, conversation)

        response = self.llm.generate(prompt)

        conversation.add("assistant", response)

        return response