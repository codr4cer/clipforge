from pathlib import Path

from src.config.settings import PROJECT_DIR


PROMPT_PATH = PROJECT_DIR / "src" / "prompts" / "analyzer_prompt.txt"


def analyze_transcript(transcript_path: Path):
    transcript = transcript_path.read_text(encoding="utf-8")
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")

    final_prompt = f"""
{system_prompt}

Transcript to analyze:

{transcript}
"""

    print("\n🤖 Prompt Viral Engine généré.")
    print(f"Longueur du prompt : {len(final_prompt)} caractères")

    return {
        "status": "prompt_generated",
        "prompt_preview": final_prompt[:3000],
    }