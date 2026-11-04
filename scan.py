from pathlib import Path

# ignore the following files:
SKIP_DIRS = {".git", "node_modules", "__pycache__", "venv", ".venv", "dist", "build"}
SKIP_FILES = {"package-lock.json", "yarn.lock", "poetry.lock"}

# scan these, maybe add more later, will do research.
CODE_EXTS = {".py", ".js", ".ts", ".java", ".go", ".rs", ".c", ".cpp", ".cs", ".rb", ".php", ".html", ".css", ".sql"}
CONFIG_FILES = {"package.json", "requirements.txt", "pyproject.toml", "Dockerfile", "Makefile", "README.md","README.generated.md"}

# scan all the files in the given directory, this is called in main.
def scan_repo(root):
    root = Path(root)
    code_files, config_files = [], []

    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.is_file() or path.name in SKIP_FILES:
            continue
        if path.name in CONFIG_FILES:
            config_files.append(path)
        elif path.suffix in CODE_EXTS:
            code_files.append(path)
            
    return config_files, code_files