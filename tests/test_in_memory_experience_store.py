from agent.action import Action
from agent.evaluation import Evaluation
from agent.experience import Experience
from agent.in_memory_experience_store import InMemoryExperienceStore
from agent.observation import Observation
from agent.task import Task


def test_experience_store_adds_and_returns_experience():
    store = InMemoryExperienceStore()

    experience = Experience(
        Task("Calculate 2 + 2"),
        Action("answer", "4"),
        Observation("4"),
        Evaluation(True, "The answer was correct."),
    )

    store.add(experience)

    experiences = store.get_all()

    assert len(experiences) == 1
    assert experiences[0] is experience


def test_experience_store_returns_copy():
    store = InMemoryExperienceStore()

    experience = Experience(
        Task("Calculate 2 + 2"),
        Action("answer", "4"),
        Observation("4"),
        Evaluation(True, "The answer was correct."),
    )

    store.add(experience)

    experiences = store.get_all()
    experiences.clear()

    assert len(store.get_all()) == 1