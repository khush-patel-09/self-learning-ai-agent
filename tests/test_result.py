from agent.action import Action
from agent.evaluation import Evaluation
from agent.observation import Observation
from agent.result import AgentResult
from agent.reflection import Reflection


def test_agent_result_stores_response_action_observation_and_evaluation():
    action = Action("respond", "4")
    observation = Observation("4")
    evaluation = Evaluation(
        True,
        "The response was successful.",
    )
    reflection = Reflection(
        "The approach worked successfully.",
    )

    result = AgentResult(
        "4",
        action,
        observation,
        evaluation,
        reflection,
    )

    assert result.response == "4"
    assert result.action is action
    assert result.observation is observation
    assert result.evaluation is evaluation
    assert result.reflection is reflection