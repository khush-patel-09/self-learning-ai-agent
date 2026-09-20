from agent.result import AgentResult


def test_agent_result_stores_response():
    result = AgentResult("4")

    assert result.response == "4"