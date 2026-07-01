from src.core.downloader import download_video
from src.core.transcriber import transcribe_video
from src.core.analyzer import analyze_transcript
from src.core.exporter import export_results


def main():
    url = input("Colle l'URL YouTube : ")

    video_path = download_video(url)
    transcript_path = transcribe_video(video_path)
    results = analyze_transcript(transcript_path)
    export_results(results)

    print("\n🎉 Pipeline terminé.")


if __name__ == "__main__":
    main()