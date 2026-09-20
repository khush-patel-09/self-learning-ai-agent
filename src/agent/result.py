from agent.action import Action
from agent.observation import Observation


class AgentResult:
    """Represents the result of an agent run."""

    def __init__(
        self,
        response: str,
        action: Action,
        observation: Observation,
    ):
        self.response = response
        self.action = action
        self.observation = observation