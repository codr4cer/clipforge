REQUIRED_CLIP_FIELDS = [
    "id",
    "start",
    "end",
    "duration_seconds",
    "score",
    "hook",
    "reason",
    "title",
    "hashtags",
]


def validate_clip_suggestions(data: dict) -> None:
    if "clips" not in data:
        raise ValueError("La réponse ne contient pas la clé 'clips'.")

    if not isinstance(data["clips"], list):
        raise ValueError("'clips' doit être une liste.")

    for clip in data["clips"]:
        for field in REQUIRED_CLIP_FIELDS:
            if field not in clip:
                raise ValueError(f"Champ manquant dans un clip : {field}")

        if not isinstance(clip["score"], int):
            raise ValueError("Le score doit être un entier.")

        if not 0 <= clip["score"] <= 100:
            raise ValueError("Le score doit être compris entre 0 et 100.")

        if not isinstance(clip["hashtags"], list):
            raise ValueError("Les hashtags doivent être une liste.")