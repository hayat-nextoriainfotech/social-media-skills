#!/usr/bin/env python3
"""Repository checks: copy rules, skill frontmatter, links and secrets.

Run from anywhere: python scripts/check.py
Exits 1 and prints every problem found. Standard library only.

Patterns that would match their own source text are built from pieces,
so this file passes its own checks.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}
TEXT_EXT = {".md", ".json", ".yml", ".yaml", ".py", ".sh", ".txt", ""}

LONG_DASHES = "".join(chr(c) for c in (0x2014, 0x2013, 0x2015))  # em dash, en dash, horizontal bar
NUM_WORDS = "two|three|four|five|six|seven|eight|nine|ten|eleven|twelve"
NETWORK_COUNT = re.compile(
    r"\b(\d+|" + NUM_WORDS + r")\+?\s+(social(\s+media)?\s+)?(networks?|platforms?|channels?)\b",
    re.I,
)
LI = "linked" + "in"
AR = r"auto[\s-]?" + "repl"
LI_AR_NEAR = re.compile(LI + r".{0,40}?" + AR + "|" + AR + r".{0,40}?" + LI, re.I | re.S)
PRICE = [
    re.compile(r"[$€£]\s?\d"),
    re.compile(r"\b(USD|AED|EUR|GBP|SAR|INR)\s?\d", re.I),
    re.compile(r"\d\s?(USD|AED|EUR|GBP|SAR|INR)\b", re.I),
    re.compile(r"\d\s?(/\s?mo(nth)?|per\s+month)\b", re.I),
]
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+" + "@" + r"[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
SECRETS = {
    "private key": re.compile("-----BEGIN " + r"[A-Z ]*" + "PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\b(AKIA|ASIA)[0-9A-Z]{16}\b"),
    "Anthropic key": re.compile("sk-" + r"ant-[A-Za-z0-9_-]{20,}"),
    "OpenAI-style key": re.compile(r"\bsk-(proj-)?[A-Za-z0-9]{32,}"),
    "GitHub token": re.compile(r"\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}"),
    "Slack token": re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "JWT": re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
    "bearer token": re.compile(r"Bearer\s+[A-Za-z0-9._~+/-]{20,}"),
    "assigned secret": re.compile(
        r"(pass" + r"word|secret|api[_-]?key|client[_-]?secret|access[_-]?token)\s*[:=]\s*['\"][^'\"\s]{6,}['\"]",
        re.I,
    ),
    "Azure connection string": re.compile(r"AccountKey=[A-Za-z0-9+/=]{20,}"),
}
INTERNAL_HOSTS = re.compile(
    r"\b(" + "local" + r"host|127\.0\.0\.1|0\.0\.0\.0|[\w-]+\.azurewebsites\.net|[\w-]+\.scm\.[\w.]+|"
    r"[\w-]+\.internal\b|[\w-]+\.local\b|[\w-]+\.cloudapp\.[\w.]+|10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+)",
    re.I,
)
SITE_LINK = re.compile(r"https://(www\.)?personaxpand\.com[^\s)\"'>`]*")
ALLOWED_FRONTMATTER = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
AFFILIATE = "affiliate." + "nextoria.ae"


def text_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() in TEXT_EXT or path.name in {"LICENSE"}:
            yield path


def line_of(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def check_text(path: Path, text: str, problems: list[str]) -> None:
    rel = path.relative_to(ROOT).as_posix()

    def add(index: int, what: str, snippet: str) -> None:
        problems.append(f"{rel}:{line_of(text, index)}: {what}: {snippet.strip()[:80]!r}")

    for i, ch in enumerate(text):
        if ch in LONG_DASHES:
            add(i, "long dash (use a comma, colon or full stop)", text[max(0, i - 20): i + 20])
    for m in NETWORK_COUNT.finditer(text):
        add(m.start(), "network count (name the networks instead)", m.group(0))
    for m in LI_AR_NEAR.finditer(text):
        add(m.start(), LI.capitalize() + " near auto-reply wording (unsupported claim risk)", m.group(0))
    for rx in PRICE:
        for m in rx.finditer(text):
            add(m.start(), "price", m.group(0))
    for m in EMAIL.finditer(text):
        add(m.start(), "email address", m.group(0))
    for name, rx in SECRETS.items():
        for m in rx.finditer(text):
            add(m.start(), f"possible secret ({name})", m.group(0)[:12] + "...")
    for m in INTERNAL_HOSTS.finditer(text):
        add(m.start(), "internal host or address", m.group(0))
    if path.suffix == ".md":
        for m in SITE_LINK.finditer(text):
            url = m.group(0)
            if url.rstrip("/").endswith("/mcp"):
                continue  # connector endpoint, not a web page
            if "utm_source=github" not in url or "utm_medium=skills" not in url or "utm_campaign=" not in url:
                add(m.start(), "personaxpand.com link without UTM", url)
    if AFFILIATE in text and rel != "README.md":
        add(text.index(AFFILIATE), "affiliate link outside README", AFFILIATE)


def check_affiliate_placement(problems: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    lines = [ln for ln in readme.splitlines() if ln.strip()]
    hits = [ln for ln in lines if AFFILIATE in ln]
    if len(hits) != 1:
        problems.append(f"README.md: affiliate link must appear exactly once (found {len(hits)})")
    elif lines[-1] != hits[0]:
        problems.append("README.md: affiliate line must be the last line")


def parse_frontmatter(text: str):
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.startswith((" ", "\t")):
            continue
        key, sep, value = raw.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return fields


def check_skills(problems: list[str]) -> None:
    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    if not skills:
        problems.append("skills/: no skills found")
    for folder in skills:
        rel = f"skills/{folder.name}/SKILL.md"
        skill = folder / "SKILL.md"
        if not skill.exists():
            problems.append(f"{rel}: missing")
            continue
        text = skill.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            problems.append(f"{rel}: frontmatter must start on line 1 with ---")
            continue
        extra = set(fm) - ALLOWED_FRONTMATTER
        if extra:
            problems.append(f"{rel}: frontmatter keys not allowed on claude.ai: {sorted(extra)}")
        name = fm.get("name", "")
        if name != folder.name:
            problems.append(f"{rel}: name {name!r} must equal folder name {folder.name!r}")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            problems.append(f"{rel}: name must be lowercase letters, digits and hyphens, max 64")
        if re.search(r"anthropic|claude", name):
            problems.append(f"{rel}: name must not contain reserved words")
        desc = fm.get("description", "")
        if not desc:
            problems.append(f"{rel}: description missing")
        elif len(desc) > 1024:
            problems.append(f"{rel}: description is {len(desc)} chars (max 1024)")
        if "<" in desc or ">" in desc:
            problems.append(f"{rel}: description must not contain < or >")
        lines = text.count("\n") + 1
        if lines > 500:
            problems.append(f"{rel}: {lines} lines (keep under 500)")
        for link in re.findall(r"\]\(([^)#\s]+)\)", text):
            if link.startswith(("http://", "https://")):
                continue
            target = (folder / link).resolve()
            if not target.exists():
                problems.append(f"{rel}: broken link {link}")
            elif folder.resolve() not in target.parents:
                problems.append(f"{rel}: link {link} leaves the skill folder (breaks single-skill ZIP uploads)")


def check_json(problems: list[str]) -> None:
    for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", ".mcp.json"):
        try:
            json.loads((ROOT / rel).read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{rel}: invalid JSON ({exc})")
    try:
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        names = [p.get("name") for p in market.get("plugins", [])]
        if plugin.get("name") not in names:
            problems.append("marketplace.json: entry name must equal plugin.json name")
        mcp = json.loads((ROOT / ".mcp.json").read_text(encoding="utf-8"))
        for key, server in mcp.get("mcpServers", {}).items():
            if server.get("headers") or server.get("env"):
                problems.append(f".mcp.json: server {key} must not carry headers or env (OAuth only)")
            if not str(server.get("url", "")).startswith("https://"):
                problems.append(f".mcp.json: server {key} url must be https")
    except Exception:  # noqa: BLE001
        pass


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    problems: list[str] = []
    for path in text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            problems.append(f"{path.relative_to(ROOT).as_posix()}: not UTF-8 text")
            continue
        check_text(path, text, problems)
    check_affiliate_placement(problems)
    check_skills(problems)
    check_json(problems)
    if problems:
        print(f"check.py: {len(problems)} problem(s)")
        for p in problems:
            print("  " + p)
        return 1
    print("check.py: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
