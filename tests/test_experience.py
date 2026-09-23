from agent.action import Action
from agent.evaluation import Evaluation
from agent.experience import Experience
from agent.observation import Observation
from agent.task import Task


def test_experience_stores_components():
    task = Task("Calculate 2 + 2")
    action = Action("answer", "4")
    observation = Observation("Correct")
    evaluation = Evaluation(
        True,
        "The answer was correct.",
    )

    experience = Experience(
        task,
        action,
        observation,
        evaluation,
    )

    assert experience.task is task
    assert experience.action is action
    assert experience.observation is observation
    assert experience.evaluation is evaluation