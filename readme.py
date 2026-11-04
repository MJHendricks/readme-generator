import ollama
from config import MODEL

# read the config files, returns a single string that gets pasted into the prompt.
def read_config(config_files, max_chars=1500):
    parts = []
    for file in config_files:
        if file.name == "README.md":
            continue
        try:
            parts.append(f"--- {file.name} ---\n{file.read_text(encoding='utf-8')[:max_chars]}")
        except (UnicodeDecodeError, OSError):
            pass
    return "\n\n".join(parts)

# onverts each file to a path relative to the repo root. max 40 items, will consider more if necessary.
def build_structure(repo_path, files, max_items=40):
    paths = sorted(str(f.relative_to(repo_path)).replace("\\", "/") for f in files)
    text = "\n".join(paths[:max_items])
    if len(paths) > max_items:
        text += f"\n... and {len(paths) - max_items} more files"
    return f"```\n{text}\n```"

# collect file names, check if there are any files listing dependencies for easy install.
def build_install(config_files):
    names = {file.name for file in config_files}
    steps = []
    if "requirements.txt" in names:
        steps.append("pip install -r requirements.txt")
    if "package.json" in names:
        steps.append("npm install")
    if not steps:
        return "See project files for setup details."
    return "```\n" + "\n".join(steps) + "\n```"

# the main function
# joins all file summaries into a single text
# sets the headings for each section, still looking into these, i want to be thorough without going into too much detail.
# sends prompt through to the model 

def generate_readme(repo_name, repo_path, config_files, all_files, summaries):
    config_text = read_config(config_files)
    summary_text = "\n\n".join(f"{name}:\n{s}" for name, s in summaries.items())

    prompt = f"""Write part of a README.md for a project called "{repo_name}".

Write ONLY these three sections, using ## headers, in this order:
## Overview
## Features
## Usage

Rules:
- Do not write a title, installation steps, or a project structure section.
- Only use information from the material below. Do not invent features, commands, or dependencies.
- For Usage, if you can't tell how the project is run, say so rather than guessing.

CONFIG FILES:
{config_text}

FILE SUMMARIES:
{summary_text}"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    body = response["message"]["content"].strip()

    return (
        f"# {repo_name}\n\n{body}\n\n"
        f"## Installation\n\n{build_install(config_files)}\n\n"
        f"## Project Structure\n\n{build_structure(repo_path, all_files)}\n"
    )