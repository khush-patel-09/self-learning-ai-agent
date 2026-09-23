from agent.reflection import Reflection


def test_reflection_stores_insight():
    reflection = Reflection(
        "The agent should provide more concise explanations."
    )

    assert reflection.insight == (
        "The agent should provide more concise explanations."
    )