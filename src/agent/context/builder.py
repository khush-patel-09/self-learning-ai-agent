from agent.conversation import Conversation
from agent.task import Task


class ContextBuilder:
    """Builds the context sent to the language model."""

    def build(self, task: Task, conversation: Conversation) -> str:
        """Build an LLM prompt from conversation history and the task."""
        messages = [
            f"{message.role}: {message.content}"
            for message in conversation.messages
        ]

        messages.append(f"user: {task.description}")

        return "\n".join(messages)