import json
from pathlib import Path

from src.config.settings import PROJECT_DIR
from src.ai.mock_provider import MockAIProvider


PROMPT_PATH = PROJECT_DIR / "src" / "prompts" / "analyzer_prompt.txt"


def analyze_transcript(transcript_path: Path):
    transcript = transcript_path.read_text(encoding="utf-8")
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")

    final_prompt = f"""
{system_prompt}

Transcript to analyze:

{transcript}
"""

    provider = MockAIProvider()
    response = provider.generate(final_prompt)

    return json.loads(response)