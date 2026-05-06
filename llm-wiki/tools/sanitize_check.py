#!/usr/bin/env python3
import re
import sys
from pathlib import Path

DEFAULT_PATTERNS = {
    "possible_secret_assignment": re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*[\"']?[^\s\"']{8,}"),
    "github_token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "google_api_key": re.compile(r"AIza[0-9A-Za-z\-_]{20,}"),
    "bearer_token": re.compile(r"(?i)bearer\s+[A-Za-z0-9\-\._~\+/=]{12,}"),
    "email_address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
}

IGNORE_DIRS = {".git", "__pycache__"}
TEXT_EXTS = {".md", ".txt", ".log", ".json", ".yaml", ".yml", ".csv", ".py"}


def load_denylist(root: Path):
    deny = []
    p = root / "_meta" / "redaction-denylist.local.txt"
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                deny.append(line)
    return deny


def should_scan(path: Path):
    return path.is_file() and path.suffix.lower() in TEXT_EXTS


def main():
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "llm-wiki").resolve()
    denylist = load_denylist(target)
    findings = []
    for path in target.rglob("*"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if not should_scan(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        for label, pattern in DEFAULT_PATTERNS.items():
            for i, line in enumerate(text.splitlines(), start=1):
                if pattern.search(line):
                    findings.append((str(path.relative_to(target.parent)), i, label, line.strip()))
        for term in denylist:
            for i, line in enumerate(text.splitlines(), start=1):
                if term.lower() in line.lower():
                    findings.append((str(path.relative_to(target.parent)), i, "denylist_term", line.strip()))
    if findings:
        print("SANITIZATION FINDINGS:")
        for file_path, line_no, label, snippet in findings:
            print(f"{file_path}:{line_no}: {label}: {snippet[:200]}")
        sys.exit(1)
    print("No obvious sanitization findings.")


if __name__ == "__main__":
    main()
