from agent.agent import Agent
from agent.llm.fake import FakeLLM
from agent.task import Task


def test_agent_runs_task_using_llm():
    llm = FakeLLM("4")
    agent = Agent(llm)
    task = Task("Calculate 2 + 2")

    result = agent.run(task)

    assert result == "4"