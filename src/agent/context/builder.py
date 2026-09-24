from agent.conversation import Conversation
from agent.experience_store import ExperienceStore
from agent.memory.store import MemoryStore
from agent.task import Task


class ContextBuilder:
    """Builds the context sent to the language model."""

    def build(
        self,
        task: Task,
        conversation: Conversation,
        memory_store: MemoryStore | None = None,
        experience_store: ExperienceStore | None = None,
    ) -> str:
        """Build an LLM prompt from conversation, memories, experiences, and task."""
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

                for experience in experiences:
                    messages.append(
                        f"- task: {experience.task.description}"
                    )
                    messages.append(
                        f"  outcome: {experience.evaluation.feedback}"
                    )

                    if experience.reflection is not None:
                        messages.append(
                            f"  learned insight: {experience.reflection.insight}"
                        )

        messages.append(f"user: {task.description}")

        return "\n".join(messages)