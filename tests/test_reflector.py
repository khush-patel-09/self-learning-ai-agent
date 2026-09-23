from agent.reflector import Reflector


def test_reflector_is_abstract():
    assert Reflector.__abstractmethods__ == {"reflect"}