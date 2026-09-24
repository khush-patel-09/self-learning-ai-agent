from agent.agent import Agent
from agent.config import Config
from agent.context.builder import ContextBuilder
from agent.llm.ollama import OllamaLLM
from agent.memory.in_memory import InMemoryStore
from agent.memory.local_embeddings import LocalEmbeddingModel
from agent.simple_evaluator import SimpleEvaluator
from agent.simple_reflector import SimpleReflector
from agent.in_memory_experience_store import InMemoryExperienceStore


def create_agent(config: Config) -> Agent:
    """Create an agent using the configured LLM provider."""
    if config.llm_provider == "ollama":
        llm = OllamaLLM(config)
    else:
        raise ValueError(f"Unsupported LLM provider: {config.llm_provider}")

    embedding_model = LocalEmbeddingModel()
    memory_store = InMemoryStore(embedding_model)
    experience_store = InMemoryExperienceStore(embedding_model)

    return Agent(
        llm,
        ContextBuilder(),
        SimpleEvaluator(),
        SimpleReflector(),
        memory_store,
        experience_store,
    )