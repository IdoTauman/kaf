import re

token_patterns = [
    ("keyword", r"\b(שלם | אם | החזר)\b"),
    ("identifier", r"\b[\u0590-\u05FF0-9_]+\b"),
    ("number_literal", r"\b[0-9]+(\.[0-9]+)?\b")
]

map: dict[str, tuple[str, str]] = {
    r"\bשלם\b": ("int", "keyword"),
}

def tokenize(code: str):
    tokens = []
