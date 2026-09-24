from agent.action import Action
from agent.evaluation import Evaluation
from agent.experience import Experience
from agent.observation import Observation
from agent.simple_reflector import SimpleReflector
from agent.task import Task


def test_simple_reflector_creates_success_reflection():
    experience = Experience(
        Task("Calculate 2 + 2"),
        Action("answer", "4"),
        Observation("4"),
        Evaluation(True, "The agent produced an observable result."),
    )

    reflection = SimpleReflector().reflect(experience)

    assert reflection.insight == (
        "For the task 'Calculate 2 + 2', "
        "the approach produced a successful outcome: "
        "The agent produced an observable result."
    )


def test_simple_reflector_creates_failure_reflection():
    experience = Experience(
        Task("Calculate 2 + 2"),
        Action("answer", ""),
        Observation(""),
        Evaluation(False, "The agent produced an empty result."),
    )

    reflection = SimpleReflector().reflect(experience)

    assert reflection.insight == (
        "For the task 'Calculate 2 + 2', "
        "the approach should be improved: "
        "The agent produced an empty result."
    )