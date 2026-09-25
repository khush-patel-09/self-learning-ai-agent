from agent.action import Action
from agent.evaluation import Evaluation
from agent.observation import Observation
from agent.reflection import Reflection
from agent.task import Task


class Experience:
    """Represents a complete experience from an agent run."""

    def __init__(
        self,
        task: Task,
        action: Action,
        observation: Observation,
        evaluation: Evaluation,
        reflection: Reflection | None = None,
    ):
        self.task = task
        self.action = action
        self.observation = observation
        self.evaluation = evaluation
        self.reflection = reflection

    def to_context(self) -> list[str]:
        """Return the experience formatted for LLM context."""
        lines = [
            f"- task: {self.task.description}",
            f"  outcome: "
            f"{'success' if self.evaluation.success else 'failure'} - "
            f"{self.evaluation.feedback}",
        ]

        if self.reflection is not None:
            lines.append(
                f"  learned insight: {self.reflection.insight}"
            )

        return lines