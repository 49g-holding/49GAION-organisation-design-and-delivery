"""Case 10 of TEST-DESIGN-CHAIN v2: every part's mother blueprint, and every pinned contract,
reads back from its repository at the pinned commit with the pinned SHA-256.

Reads pins/PINS.json. For each entry with a sha256, it fetches the pinned commit of the public
repository into a cache folder and hashes the file at that commit.
Usage: python3 tools/check_pins.py [cache folder, default .deps/pins]   (exit 1 on any mismatch)
"""
import hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PINS = json.loads((ROOT / "pins" / "PINS.json").read_text(encoding="utf-8"))
CACHE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / ".deps" / "pins"


def git(*args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True).stdout


def read_at(repository, commit, path):
    folder = CACHE / repository.replace("/", "__")
    if not (folder / ".git").exists():
        folder.mkdir(parents=True, exist_ok=True)
        git("init", "-q", cwd=folder)
        git("remote", "add", "origin", f"https://github.com/{repository}.git", cwd=folder)
    git("fetch", "-q", "--depth", "1", "origin", commit, cwd=folder)
    return git("show", f"{commit}:{path}", cwd=folder)


def main():
    errors, checked = [], 0
    for entry in PINS["parts"] + PINS["contracts"]:
        name = entry.get("part") or entry.get("contract")
        if not entry.get("sha256"):
            print(f"skip   {name}: no single file pinned ({entry.get('note', '')[:60]})")
            continue
        try:
            got = hashlib.sha256(read_at(entry["repository"], entry["commit"], entry["path"])).hexdigest()
        except subprocess.CalledProcessError as e:
            errors.append(f"{name}: cannot read {entry['path']} at {entry['commit']}: {e.stderr.decode(errors='replace').strip()}")
            continue
        checked += 1
        if got != entry["sha256"]:
            errors.append(f"{name}: SHA-256 {got} at {entry['commit'][:7]}, pinned {entry['sha256']}")
        else:
            print(f"ok     {name}: {entry['path']} @ {entry['commit'][:7]} {got[:12]}")
    for e in errors:
        print(f"ERROR  {e}")
    print(f"{checked} pins read back; {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
