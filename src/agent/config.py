import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration loaded from environment variables."""

    def __init__(self):
        self.llm_provider = os.getenv("LLM_PROVIDER")
        self.llm_model = os.getenv("LLM_MODEL")
        self.llm_base_url = os.getenv("LLM_BASE_URL")