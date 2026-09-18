import pytest

from agent.llm.base import LLM


def test_llm_cannot_be_instantiated():
    with pytest.raises(TypeError):
        LLM()