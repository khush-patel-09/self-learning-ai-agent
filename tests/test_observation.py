from agent.observation import Observation


def test_observation_stores_content():
    observation = Observation("Correct answer")

    assert observation.content == "Correct answer"