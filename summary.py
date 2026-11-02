import ollama
from pathlib import Path

MODEL = "qwen2.5-coder:3b"
MAX_CHARS = 6000  # truncate large files to fit context

def summarize_file(path):
    path = Path(path)
    try:
        code = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None

    code = code[:MAX_CHARS]

    prompt = f"""Summarize what this file does in 2-3 sentences.
Mention its main functions/classes and its role in the project.
Do not guess about things not visible in the code.

File: {path.name}

{code}"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]

if __name__ == "__main__":
    import sys
    print(summarize_file(sys.argv[1]))