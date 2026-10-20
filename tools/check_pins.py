"""Case 10 of TEST-DESIGN-CHAIN v2: every part's mother blueprint, and every pinned contract,
reads back from its repository at the pinned commit with the pinned SHA-256; and each part's
pin equals its row in the Library register (49GAION-protocol, library/README.md) at the commit
pinned for the shared test.

Reads pins/PINS.json. Every entry must carry a commit and a SHA-256; one without fails.
Usage: python3 tools/check_pins.py [cache folder, default .deps/pins]   (exit 1 on any error)
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
        if not entry.get("commit") or not entry.get("sha256"):
            errors.append(f"{name}: the pin has no commit or no SHA-256")
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

    # Each part's pin equals its row in the Library register.
    reg = PINS["shared_test"]
    try:
        register = read_at(reg["repository"], reg["commit"], reg["path"]).decode("utf-8")
    except subprocess.CalledProcessError as e:
        errors.append(f"the Library register: cannot read {reg['path']} at {reg['commit']}")
        register = ""
    rows = [line for line in register.splitlines() if line.startswith("| 49GAION ")]
    for part in PINS["parts"]:
        row = next((r for r in rows if r.startswith(f"| {part['part']} |")), None)
        if row is None:
            errors.append(f"{part['part']}: no row in the Library register at {reg['commit'][:7]}")
            continue
        missing = [k for k in ("repository", "path", "version", "commit", "sha256")
                   if (part[k].split("/", 1)[1] if k == "repository" else part[k]) not in row]
        if missing:
            errors.append(f"{part['part']}: the Library register row differs in {', '.join(missing)}")
        else:
            print(f"ok     {part['part']}: equals its Library register row @ {reg['commit'][:7]}")

    for e in errors:
        print(f"ERROR  {e}")
    print(f"{checked} pins read back; {len(PINS['parts'])} register rows compared; {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
