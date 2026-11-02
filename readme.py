import ollama
from pathlib import Path

MODEL = "qwen2.5-coder:3b"

def read_config(config_files, max_chars=1500):
    parts = []
    for f in config_files:
        if f.name == "README.md":
            continue  # don't feed in the old README
        try:
            parts.append(f"--- {f.name} ---\n{f.read_text(encoding='utf-8')[:max_chars]}")
        except (UnicodeDecodeError, OSError):
            pass
    return "\n\n".join(parts)

def generate_readme(repo_name, config_files, summaries):
    config_text = read_config(config_files)
    summary_text = "\n\n".join(f"{name}:\n{s}" for name, s in summaries.items())

    prompt = f"""Write a README.md in markdown for a project called "{repo_name}".

Use exactly these sections:
# {repo_name}
## Overview
## Features
## Installation
## Usage
## Project Structure

Rules:
- Only use information from the material below. Do not invent features, commands, or dependencies.
- For Installation, use only commands and dependencies visible in the config files. If none are visible, say "See project files for setup details."
- For Usage, if you can't tell how it's run, say so rather than guessing.

CONFIG FILES:
{config_text}

FILE SUMMARIES:
{summary_text}"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]