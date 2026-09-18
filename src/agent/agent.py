from agent.llm.base import LLM
from agent.task import Task


class Agent:
    """Core agent responsible for processing tasks."""

    def __init__(self, llm: LLM):
        self.llm = llm

    def run(self, task: Task) -> str:
        """Process a task using the configured language model."""
        return self.llm.generate(task.description)