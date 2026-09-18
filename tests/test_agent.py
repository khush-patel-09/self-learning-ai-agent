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
    conversation.add("user", "My name is Khush.")

    task = Task("What is my name?")

    agent.run(task, conversation)

    assert llm.last_prompt == "My name is Khush.\nWhat is my name?"


def test_agent_adds_response_to_conversation():
    llm = FakeLLM("4")
    agent = Agent(llm)

    conversation = Conversation()
    task = Task("Calculate 2 + 2")

    agent.run(task, conversation)

    assert len(conversation.messages) == 1
    assert conversation.messages[0].role == "assistant"
    assert conversation.messages[0].content == "4"