from src.ai.base import AIProvider


class MockAIProvider(AIProvider):
    def generate(self, prompt: str) -> dict:
        return {
            "clips": [
                {
                    "id": 1,
                    "start": "00:01:00",
                    "end": "00:01:45",
                    "duration_seconds": 45,
                    "score": 82,
                    "hook": "Ce passage pourrait créer de la curiosité.",
                    "reason": "Réponse simulée pour tester le pipeline.",
                    "title": "Extrait automobile prometteur",
                    "hashtags": ["automobile", "voiture", "mecanique", "cartok"],
                }
            ]
        }