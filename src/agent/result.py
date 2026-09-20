from agent.action import Action


class AgentResult:
    """Represents the result of an agent run."""

    def __init__(self, response: str, action: Action):
        self.response = response
        self.action = action