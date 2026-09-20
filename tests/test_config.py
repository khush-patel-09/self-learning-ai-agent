from agent.config import Config


def test_config_reads_llm_configuration(monkeypatch):
    monkeypatch.setenv("LLM_API_KEY", "test-key")
    monkeypatch.setenv("LLM_MODEL", "test-model")

    config = Config()

    assert config.llm_api_key == "test-key"
    assert config.llm_model == "test-model"