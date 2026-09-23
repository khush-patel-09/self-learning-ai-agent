import pytest

from agent.memory.similarity import cosine_similarity


def test_cosine_similarity_of_identical_vectors():
    assert cosine_similarity([1.0, 0.0], [1.0, 0.0]) == pytest.approx(1.0)


def test_cosine_similarity_of_orthogonal_vectors():
    assert cosine_similarity([1.0, 0.0], [0.0, 1.0]) == pytest.approx(0.0)


def test_cosine_similarity_rejects_different_dimensions():
    with pytest.raises(ValueError):
        cosine_similarity([1.0, 0.0], [1.0])