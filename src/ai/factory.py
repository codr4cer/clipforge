from src.config.settings import AI_PROVIDER
from src.ai.mock_provider import MockAIProvider
from src.ai.openai_provider import OpenAIProvider


def get_ai_provider():
    if AI_PROVIDER == "mock":
        return MockAIProvider()

    if AI_PROVIDER == "openai":
        return OpenAIProvider()

    raise ValueError(f"Unknown AI provider: {AI_PROVIDER}")