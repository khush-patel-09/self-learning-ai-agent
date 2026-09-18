from agent.task import Task


def test_task_stores_description():
    task = Task("Calculate 2 + 2")

    assert task.description == "Calculate 2 + 2"