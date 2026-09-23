from agent.action import Action
from agent.observation import Observation
from agent.simple_evaluator import SimpleEvaluator
from agent.task import Task


def test_simple_evaluator_marks_non_empty_observation_successful():
    evaluator = SimpleEvaluator()

    evaluation = evaluator.evaluate(
        Task("Calculate 2 + 2"),
        Action("answer", "4"),
        Observation("4"),
    )

    assert evaluation.success is True
    assert evaluation.feedback == "The agent produced an observable result."


def test_simple_evaluator_marks_empty_observation_unsuccessful():
    evaluator = SimpleEvaluator()

    evaluation = evaluator.evaluate(
        Task("Calculate 2 + 2"),
        Action("answer", ""),
        Observation(""),
    )

    assert evaluation.success is False
    assert evaluation.feedback == "The agent produced an empty result."