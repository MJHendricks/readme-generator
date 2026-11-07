import sys
import json
import ollama
from pathlib import Path
from scan import scan_repo
from summary import summarize_file
from readme import generate_readme

# max files 30 because i think this project is better suited for smaller repos, will test on larger directories later.
MAX_FILES = 30

# cache folder to speed things up
CACHE_DIR = Path(__file__).parent / "cache"

def load_cache(cache_path):
    if cache_path.exists():
        return json.loads(cache_path.read_text(encoding="utf-8"))
    return {}

def main(repo_path):
    # create cache folder if it doesnt exist
    repo_path = Path(repo_path).resolve()
    CACHE_DIR.mkdir(exist_ok=True)
    cache_path = CACHE_DIR / f"{repo_path.name}.json"
    cache = load_cache(cache_path)

    config_files, code_files = scan_repo(repo_path)
    all_files = config_files + code_files

    # biggest files first, in case the project goes over the max file cap, bigger usually means more important.
    # but not always. will maybe look into this later, and may add additional "skips".
    code_files = sorted(code_files, key=lambda f: f.stat().st_size, reverse=True)[:MAX_FILES]

    summaries = {}
    for f in code_files:
        # check if files have been updated since last run, if it hasnt been changed, just reuse the cached summary
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

    # for now im exporting to "README.generated", in case something goes wrong, i dont wanna overwrite the actual readme file.
    # This file can always be renamed to README.md, so i'll probably keep it this way.
    out = repo_path / "README.generated.md"
    out.write_text(readme, encoding="utf-8")
    print(f"Saved to {out}")

# remember to include directory when running main.py
if __name__ == "__main__": 
    try:
        main(sys.argv[1])
    except ConnectionError:
        print("Could not reach Ollama, is it running?")
    except ollama.ResponseError as e:
        print(f"Ollama returned an error: {e}")