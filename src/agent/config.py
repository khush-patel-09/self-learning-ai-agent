import os


class Config:
    """Application configuration loaded from environment variables."""

    def __init__(self):
        self.llm_api_key = os.getenv("LLM_API_KEY")
        self.llm_model = os.getenv("LLM_MODEL")