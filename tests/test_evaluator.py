from agent.evaluator import Evaluator


def test_evaluator_is_abstract():
    assert Evaluator.__abstractmethods__ == {"evaluate"}