from agent.agent import Agent
from agent.config import Config
from agent.context.builder import ContextBuilder
from agent.llm.ollama import OllamaLLM
from agent.memory.in_memory import InMemoryStore


def create_agent(config: Config) -> Agent:
    """Create an agent using the configured LLM provider."""
    if config.llm_provider == "ollama":
        llm = OllamaLLM(config)
    else:
        raise ValueError(f"Unsupported LLM provider: {config.llm_provider}")

    return Agent(
        llm,
        ContextBuilder(),
        InMemoryStore(),
    )