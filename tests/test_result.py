from agent.action import Action
from agent.observation import Observation
from agent.result import AgentResult


def test_agent_result_stores_response_action_and_observation():
    action = Action("respond", "4")
    observation = Observation("4")

    result = AgentResult("4", action, observation)

    assert result.response == "4"
    assert result.action is action
    assert result.observation is observation