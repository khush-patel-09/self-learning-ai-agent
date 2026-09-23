from agent.memory.embeddings import EmbeddingModel


def test_embedding_model_defines_embed_interface():
    assert hasattr(EmbeddingModel, "embed")