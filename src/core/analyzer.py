import json
from pathlib import Path

from src.config.settings import PROJECT_DIR
from src.ai.factory import get_ai_provider
from src.models.validators import validate_clip_suggestions


PROMPT_PATH = PROJECT_DIR / "src" / "prompts" / "analyzer_prompt.txt"


def analyze_transcript(transcript_path: Path):
    transcript = transcript_path.read_text(encoding="utf-8")
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")

    final_prompt = f"""
{system_prompt}

Transcript to analyze:

{transcript}
"""

    provider = get_ai_provider()
    response = provider.generate(final_prompt)

    data = json.loads(response)

    validate_clip_suggestions(data)

    return data