import ollama
from pathlib import Path
from config import MODEL

# i think 10 000 is a decent number for now, will test out larger files later.
MAX_CHARS = 10000

# called in main for each file, reads text up to the character limit, passes to ollama and returns a summary of the file in english.
def summarize_file(path):
    path = Path(path)
    try:
        code = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None

    code = code[:MAX_CHARS]

    prompt = f"""Summarize what this file does in 3 sentences or less.
    Mention its main functions/classes and its role in the project.
    Do not guess about things not visible in the code.

File: {path.name}

{code}"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]