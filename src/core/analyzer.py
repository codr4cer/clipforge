import json
from pathlib import Path

from src.config.settings import PROJECT_DIR
from src.ai.factory import get_ai_provider
from src.models.validators import validate_clip_suggestions
from src.core.transcript_chunker import chunk_transcript


PROMPT_PATH = PROJECT_DIR / "src" / "prompts" / "analyzer_prompt.txt"


def analyze_transcript(transcript_path: Path):
    transcript = transcript_path.read_text(encoding="utf-8")
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")

chunks = chunk_transcript(transcript)

print(f"\n🧩 Nombre de chunks générés : {len(chunks)}")

provider = get_ai_provider()
all_clips = []

for index, chunk in enumerate(chunks, start=1):
    print(f"\n🤖 Analyse du chunk {index}/{len(chunks)}...")

    final_prompt = f"""
{system_prompt}

Transcript chunk number: {index}

Transcript chunk to analyze:

{chunk}
"""

    response = provider.generate(final_prompt)
    data = json.loads(response)

    validate_clip_suggestions(data)

    all_clips.extend(data["clips"])

all_clips = sorted(all_clips, key=lambda clip: clip["score"], reverse=True)

return {
    "clips": all_clips[:10]
}