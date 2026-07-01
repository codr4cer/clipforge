import json

from src.config.settings import METADATA_DIR


def export_results(results: dict):
    METADATA_DIR.mkdir(exist_ok=True)

    output_path = METADATA_DIR / "clips_suggestions.json"

    output_path.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"\n✅ Résultats exportés : {output_path}")

    return output_path