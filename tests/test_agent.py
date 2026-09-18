import pytest

from agent.agent import Agent
from agent.task import Task


def test_agent_requires_implementation():
    agent = Agent()
    task = Task("Calculate 2 + 2")

    with pytest.raises(NotImplementedError):
        agent.run(task)