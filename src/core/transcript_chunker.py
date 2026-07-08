def chunk_transcript(text: str, max_chars: int = 4000) -> list[str]:
    paragraphs = text.split("\n")
    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if not paragraph:
            continue

        if len(current_chunk) + len(paragraph) + 1 <= max_chars:
            current_chunk += paragraph + "\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = paragraph + "\n"

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks