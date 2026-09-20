from agent.action import Action


def test_action_stores_name_and_input():
    action = Action("answer", "4")

    assert action.name == "answer"
    assert action.input == "4"