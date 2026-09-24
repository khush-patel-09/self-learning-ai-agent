from agent.conversation import Conversation
from agent.memory.store import MemoryStore
from agent.task import Task
from agent.experience_store import ExperienceStore


class ContextBuilder:
    """Builds the context sent to the language model."""

    def build(
        self,
        task: Task,
        conversation: Conversation,
        memory_store: MemoryStore | None = None,
        experience_store: ExperienceStore | None = None,
    ) -> str:
        """Build an LLM prompt from conversation history, memories, and task."""
        messages = [
            f"{message.role}: {message.content}"
            for message in conversation.messages
        ]

        if memory_store is not None:
            memories = memory_store.search(task.description)

            if memories:
                messages.append("relevant memories:")
                messages.extend(
                    f"- {memory.content}"
                    for memory in memories
                )

        if experience_store is not None:
            experiences = experience_store.search(task.description)

            if experiences:
                messages.append("relevant experiences:")
                messages.extend(
                    f"- {experience.task.description}: "
                    f"{experience.evaluation.feedback}"
                    for experience in experiences
                )

        messages.append(f"user: {task.description}")

        return "\n".join(messages)