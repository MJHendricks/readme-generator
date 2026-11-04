import sys
import json
from pathlib import Path
from scan import scan_repo
from summary import summarize_file
from readme import generate_readme

MAX_FILES = 30
CACHE_DIR = Path(__file__).parent / "cache"

def load_cache(cache_path):
    if cache_path.exists():
        return json.loads(cache_path.read_text(encoding="utf-8"))
    return {}

def main(repo_path):
    repo_path = Path(repo_path).resolve()
    CACHE_DIR.mkdir(exist_ok=True)
    cache_path = CACHE_DIR / f"{repo_path.name}.json"
    cache = load_cache(cache_path)

    config_files, code_files = scan_repo(repo_path)
    all_files = config_files + code_files

    # crude importance proxy: biggest files first, capped
    code_files = sorted(code_files, key=lambda f: f.stat().st_size, reverse=True)[:MAX_FILES]

    summaries = {}
    for f in code_files:
        key = str(f.relative_to(repo_path))
        mtime = f.stat().st_mtime

        if key in cache and cache[key]["mtime"] == mtime:
            print(f"Cached: {key}")
            summaries[key] = cache[key]["summary"]
            continue

        print(f"Summarizing {key}...")
        result = summarize_file(f)
        if result:
            summaries[key] = result
            cache[key] = {"mtime": mtime, "summary": result}
            cache_path.write_text(json.dumps(cache, indent=2), encoding="utf-8")

    print("\nGenerating README...")
    readme = generate_readme(repo_path.name, repo_path, config_files, all_files, summaries)

    out = repo_path / "README.generated.md"
    out.write_text(readme, encoding="utf-8")
    print(f"Saved to {out}")

if __name__ == "__main__":
    main(sys.argv[1])