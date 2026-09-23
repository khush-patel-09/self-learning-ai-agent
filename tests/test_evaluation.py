from agent.evaluation import Evaluation


def test_evaluation_stores_success():
    evaluation = Evaluation(
        True,
        "The outcome was successful.",
    )

    assert evaluation.success is True
    assert evaluation.feedback == "The outcome was successful."