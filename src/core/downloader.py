import subprocess

from src.config.settings import DOWNLOADS_DIR, VIDEO_BASENAME


def download_video(url: str):
    DOWNLOADS_DIR.mkdir(exist_ok=True)

    output_path = DOWNLOADS_DIR / f"{VIDEO_BASENAME}.%(ext)s"

    command = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        url,
        "-o", str(output_path),
    ]

    print("\n📥 Téléchargement de la vidéo...")
    subprocess.run(command, check=True)

    video_files = list(DOWNLOADS_DIR.glob(f"{VIDEO_BASENAME}.*"))

    if not video_files:
        raise FileNotFoundError("Aucune vidéo téléchargée.")

    return video_files[0]