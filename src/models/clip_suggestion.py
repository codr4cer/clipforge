from dataclasses import dataclass
from typing import List


@dataclass
class ClipSuggestion:
    id: int
    start: str
    end: str
    duration_seconds: int
    score: int
    hook: str
    reason: str
    title: str
    hashtags: List[str]