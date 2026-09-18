from agent.conversation import Conversation


def test_conversation_stores_messages():
    conversation = Conversation()

    conversation.add("user", "Hello")
    conversation.add("assistant", "Hi!")

    assert len(conversation.messages) == 2

    assert conversation.messages[0].role == "user"
    assert conversation.messages[0].content == "Hello"

    assert conversation.messages[1].role == "assistant"
    assert conversation.messages[1].content == "Hi!"