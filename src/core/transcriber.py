import subprocess
from pathlib import Path

from src.config.settings import TRANSCRIPTS_DIR, LANGUAGE, WHISPER_MODEL


def transcribe_video(video_path: Path):
    TRANSCRIPTS_DIR.mkdir(exist_ok=True)

    command = [
        "whisper",
        str(video_path),
        "--language", LANGUAGE,
        "--model", WHISPER_MODEL,
        "--output_dir", str(TRANSCRIPTS_DIR),
        "--output_format", "all",
    ]

    print("\n📝 Transcription de la vidéo...")
    subprocess.run(command, check=True)

    transcript_path = TRANSCRIPTS_DIR / f"{video_path.stem}.txt"

    if not transcript_path.exists():
        raise FileNotFoundError("La transcription .txt n'a pas été trouvée.")

    return transcript_path