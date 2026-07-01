from pathlib import Path


def analyze_transcript(transcript_path: Path):
    text = transcript_path.read_text(encoding="utf-8")

    print("\n🤖 Analyse de la transcription...")
    print(f"Nombre de caractères analysés : {len(text)}")

    return {
        "status": "pending",
        "message": "Analyse IA pas encore connectée.",
        "transcript_preview": text[:1000],
    }