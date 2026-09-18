from agent.message import Message


def test_message_stores_role_and_content():
    message = Message("user", "Hello")

    assert message.role == "user"
    assert message.content == "Hello"