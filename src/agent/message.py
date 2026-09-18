class Message:
    """Represents a single message in a conversation."""

    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content