from agent.message import Message


class Conversation:
    """Stores the messages exchanged during a conversation."""

    def __init__(self):
        self.messages: list[Message] = []

    def add(self, role: str, content: str) -> None:
        """Add a message to the conversation."""
        self.messages.append(Message(role, content))