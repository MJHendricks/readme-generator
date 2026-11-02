from pathlib import Path

SKIP_DIRS = {".git", "node_modules", "__pycache__", "venv", ".venv", "dist", "build"}
SKIP_FILES = {"package-lock.json", "yarn.lock", "poetry.lock"}
CODE_EXTS = {".py", ".js", ".ts", ".java", ".go", ".rs", ".c", ".cpp", ".cs", ".rb", ".php", ".html", ".css", ".sql"}
CONFIG_FILES = {"package.json", "requirements.txt", "pyproject.toml", "Dockerfile", "Makefile", "README.md"}

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

if __name__ == "__main__":
    import sys
    config, code = scan_repo(sys.argv[1])
    print("CONFIG FILES:")
    for f in config:
        print(" ", f)
    print(f"\nCODE FILES ({len(code)}):")
    for f in code:
        print(" ", f, f"({f.stat().st_size} bytes)")