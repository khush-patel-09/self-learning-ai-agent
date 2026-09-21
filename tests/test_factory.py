from agent.config import Config
from agent.factory import create_agent
from agent.llm.ollama import OllamaLLM


def test_create_agent_uses_configured_ollama(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "ollama")
    monkeypatch.setenv("LLM_MODEL", "qwen3:4b")
    monkeypatch.setenv("LLM_BASE_URL", "http://localhost:11434")

    config = Config()
    agent = create_agent(config)

    assert isinstance(agent.llm, OllamaLLM)
    assert agent.llm.model == "qwen3:4b"
    assert agent.llm.base_url == "http://localhost:11434"