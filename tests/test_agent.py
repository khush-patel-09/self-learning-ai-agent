from agent.agent import Agent
from agent.conversation import Conversation
from agent.llm.fake import FakeLLM
from agent.task import Task


def test_agent_runs_task_using_llm():
    llm = FakeLLM("4")
    agent = Agent(llm)
    task = Task("Calculate 2 + 2")
    conversation = Conversation()

    result = agent.run(task, conversation)

    assert result == "4"


def test_agent_passes_conversation_to_llm():
    llm = FakeLLM("response")
    agent = Agent(llm)

    conversation = Conversation()
    conversation.add("My name is Khush.")

    task = Task("What is my name?")

    agent.run(task, conversation)

    assert llm.last_prompt == "My name is Khush.\nWhat is my name?"