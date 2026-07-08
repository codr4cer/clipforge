import json

from dotenv import load_dotenv
from openai import OpenAI

from src.ai.base import AIProvider

load_dotenv()


class OpenAIProvider(AIProvider):
    def __init__(self):
        self.client = OpenAI()

    def generate(self, prompt: str) -> dict:
        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.2,
            response_format={"type": "json_object"},
        )

        content = response.choices[0].message.content

        return json.loads(content)