import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
DOWNLOADS_DIR = PROJECT_DIR / "downloads"
TRANSCRIPTS_DIR = PROJECT_DIR / "transcripts"


def run_command(command):
    print(f"\nCommande lancée : {' '.join(command)}\n")
    subprocess.run(command, check=True)


def download_video(url):
    output_path = DOWNLOADS_DIR / "video_test.%(ext)s"

    run_command([
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        url,
        "-o", str(output_path)
    ])


def transcribe_video():
    video_files = list(DOWNLOADS_DIR.glob("video_test.*"))

    if not video_files:
        raise FileNotFoundError("Aucune vidéo trouvée dans le dossier downloads.")

    video_path = video_files[0]

    run_command([
        "whisper",
        str(video_path),
        "--language", "French",
        "--model", "small",
        "--output_dir", str(TRANSCRIPTS_DIR),
        "--output_format", "all"
    ])


def main():
    url = input("Colle l'URL YouTube : ")

    DOWNLOADS_DIR.mkdir(exist_ok=True)
    TRANSCRIPTS_DIR.mkdir(exist_ok=True)

    download_video(url)
    transcribe_video()

    print("\n✅ Vidéo téléchargée et transcrite avec succès.")


if __name__ == "__main__":
    main()