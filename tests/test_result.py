from agent.action import Action
from agent.result import AgentResult


def test_agent_result_stores_response_and_action():
    action = Action("respond", "4")
    result = AgentResult("4", action)

    assert result.response == "4"
    assert result.action is action