from agent.llm.base import LLM


class FakeLLM(LLM):
    """Deterministic LLM implementation used for testing."""

    def __init__(self, response: str):
        self.response = response

    def generate(self, prompt: str) -> str:
        return self.response