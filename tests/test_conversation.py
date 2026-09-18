from agent.conversation import Conversation


def test_conversation_stores_messages():
    conversation = Conversation()

    conversation.add("Hello")
    conversation.add("How are you?")

    assert conversation.messages == [
        "Hello",
        "How are you?",
    ]