from agent.action import Action
from agent.evaluation import Evaluation
from agent.experience import Experience
from agent.observation import Observation
from agent.reflection import Reflection
from agent.task import Task


def test_experience_stores_components():
    task = Task("Calculate 2 + 2")
    action = Action("answer", "4")
    observation = Observation("Correct")
    evaluation = Evaluation(
        True,
        "The answer was correct.",
    )
    reflection = Reflection(
        "The approach worked successfully.",
    )

    experience = Experience(
        task,
        action,
        observation,
        evaluation,
        reflection,
    )

    assert experience.task is task
    assert experience.action is action
    assert experience.observation is observation
    assert experience.evaluation is evaluation
    assert experience.reflection is reflection