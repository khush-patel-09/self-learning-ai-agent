from agent.config import Config


def test_config_reads_llm_configuration(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "ollama")
    monkeypatch.setenv("LLM_MODEL", "test-model")
    monkeypatch.setenv("LLM_BASE_URL", "http://localhost:11434")

    config = Config()

    assert config.llm_provider == "ollama"
    assert config.llm_model == "test-model"
    assert config.llm_base_url == "http://localhost:11434"