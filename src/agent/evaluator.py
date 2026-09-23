from abc import ABC, abstractmethod

from agent.action import Action
from agent.evaluation import Evaluation
from agent.observation import Observation
from agent.task import Task


class Evaluator(ABC):
    """Interface for evaluating agent outcomes."""

    @abstractmethod
    def evaluate(
        self,
        task: Task,
        action: Action,
        observation: Observation,
    ) -> Evaluation:
        """Evaluate an agent outcome."""
        raise NotImplementedError