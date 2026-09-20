import json
from urllib.request import Request, urlopen

from agent.config import Config
from agent.llm.base import LLM


class OllamaLLM(LLM):
    """LLM implementation that communicates with a local Ollama server."""

    def __init__(self, config: Config):
        self.base_url = config.llm_base_url.rstrip("/")
        self.model = config.llm_model

    def generate(self, prompt: str) -> str:
        """Generate a response using the configured Ollama model."""
        payload = json.dumps(
            {
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                "stream": False,
            }
        ).encode("utf-8")

        request = Request(
            f"{self.base_url}/api/chat",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with urlopen(request) as response:
            data = json.load(response)

        return data["message"]["content"]