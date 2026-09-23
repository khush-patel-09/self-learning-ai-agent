from agent.action import Action
from agent.evaluation import Evaluation
from agent.evaluator import Evaluator
from agent.observation import Observation
from agent.task import Task


class SimpleEvaluator(Evaluator):
    """Evaluates agent outcomes using basic observation rules."""

    def evaluate(
        self,
        task: Task,
        action: Action,
        observation: Observation,
    ) -> Evaluation:
        success = bool(observation.content.strip())

        feedback = (
            "The agent produced an observable result."
            if success
            else "The agent produced an empty result."
        )

        return Evaluation(success, feedback)