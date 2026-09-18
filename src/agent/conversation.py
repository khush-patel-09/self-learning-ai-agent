class Conversation:
    """Stores the messages exchanged during a conversation."""

    def __init__(self):
        self.messages: list[str] = []

    def add(self, message: str) -> None:
        """Add a message to the conversation."""
        self.messages.append(message)