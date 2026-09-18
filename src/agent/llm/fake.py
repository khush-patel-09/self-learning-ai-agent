from agent.llm.base import LLM


class FakeLLM(LLM):
    """Deterministic LLM implementation used for testing."""

    def __init__(self, response: str):
        self.response = response
        self.last_prompt: str | None = None

    def generate(self, prompt: str) -> str:
        self.last_prompt = prompt
        return self.response