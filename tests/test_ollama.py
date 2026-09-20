from unittest.mock import patch

from agent.config import Config
from agent.llm.ollama import OllamaLLM


def test_ollama_llm_generates_response(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "ollama")
    monkeypatch.setenv("LLM_MODEL", "qwen3:4b")
    monkeypatch.setenv("LLM_BASE_URL", "http://localhost:11434")

    config = Config()
    llm = OllamaLLM(config)

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def read(self):
            return b'{"message": {"role": "assistant", "content": "Hello from Qwen."}}'

    with patch("agent.llm.ollama.urlopen", return_value=FakeResponse()):
        response = llm.generate("Say hello.")

    assert response == "Hello from Qwen."