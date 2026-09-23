from agent.memory.local_embeddings import LocalEmbeddingModel


def test_local_embedding_model_returns_vector():
    model = LocalEmbeddingModel()

    vector = model.embed("The user prefers concise explanations.")

    assert isinstance(vector, list)
    assert len(vector) == 384
    assert all(isinstance(value, float) for value in vector)