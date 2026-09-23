from agent.experience_store import ExperienceStore


def test_experience_store_is_abstract():
    assert ExperienceStore.__abstractmethods__ == {
        "add",
        "get_all",
    }