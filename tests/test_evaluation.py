from agent.evaluation import Evaluation


def test_evaluation_stores_success():
    evaluation = Evaluation(True)

    assert evaluation.success is True