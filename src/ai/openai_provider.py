from src.ai.base import AIProvider


class OpenAIProvider(AIProvider):
    def generate(self, prompt: str) -> str:
        raise NotImplementedError("OpenAI provider not connected yet.")