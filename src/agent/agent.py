from agent.conversation import Conversation
from agent.llm.base import LLM
from agent.task import Task


class Agent:
    """Core agent responsible for processing tasks."""

    def __init__(self, llm: LLM):
        self.llm = llm

    def run(self, task: Task, conversation: Conversation) -> str:
        """Process a task using the conversation context."""
        prompt = "\n".join(
            [f"{message.role}: {message.content}" for message in conversation.messages]
            + [f"user: {task.description}"]
        )

        response = self.llm.generate(prompt)

        conversation.add("assistant", response)

        return response