from agent.llm.fake import FakeLLM


def test_fake_llm_returns_configured_response():
    llm = FakeLLM("test response")

    result = llm.generate("test prompt")

    assert result == "test response"