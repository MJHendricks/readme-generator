import sys
from pathlib import Path
from scan import scan_repo
from summary import summarize_file
from readme import generate_readme

def main(repo_path):
    repo_path = Path(repo_path).resolve()
    config_files, code_files = scan_repo(repo_path)

    summaries = {}
    for f in code_files:
        print(f"Summarizing {f}...")
        result = summarize_file(f)
        if result:
            summaries[str(f.relative_to(repo_path))] = result

    print("\nGenerating README...")
    readme = generate_readme(repo_path.name, config_files, summaries)

    out = repo_path / "README.generated.md"
    out.write_text(readme, encoding="utf-8")
    print(f"Saved to {out}")

if __name__ == "__main__":
    main(sys.argv[1])