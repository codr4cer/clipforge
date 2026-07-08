from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[2]

DOWNLOADS_DIR = PROJECT_DIR / "downloads"
TRANSCRIPTS_DIR = PROJECT_DIR / "transcripts"
METADATA_DIR = PROJECT_DIR / "metadata"

VIDEO_BASENAME = "video_test"
LANGUAGE = "French"
WHISPER_MODEL = "small"
AI_PROVIDER = "mock"