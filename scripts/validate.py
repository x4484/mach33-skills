#!/usr/bin/env python3
"""Static pack validation; no network, package execution, or behavioral tests."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skills = sorted((root / "skills").glob("*/SKILL.md"))
assert len(skills) == 3
for path in skills:
    text = path.read_text()
    assert text.startswith("---\n")
    front = text.split("---", 2)[1]
    fields = dict(re.findall(r"^([a-z-]+): (.+)$", front, re.M))
    name = fields["name"]
    assert name == path.parent.name
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
    assert len(name) <= 64
    assert 0 < len(fields["description"]) <= 1024
    assert len(fields.get("compatibility", "")) <= 500
    assert fields["license"] == "Apache-2.0"
    assert len(text.splitlines()) < 500
    for ref in re.findall(r"references/[a-z-]+\.md", text):
        assert (path.parent / ref).is_file(), ref
    print("PASS skill:", name)
for path in root.rglob("*.md"):
    if ".git" in path.parts:
        continue
    text = path.read_text()
    assert "PASTE_PUBLIC_REPOSITORY_URL_HERE" not in text, path
    for link in re.findall(r"\]\(([^)]+)\)", text):
        if not link.startswith(("https:", "http:", "#")):
            assert (path.parent / link).exists(), (path, link)
assert not (root / "copy-paste").exists(), "Obsolete instruction artifact"
assert not (root / "scripts/build-copy-paste.py").exists(), "Obsolete generator"
grok = (root / "harnesses/grok-bot.md").read_text()
assert "reusable private Grok Bot skills" in grok
assert "including every referenced file" in grok
assert "do not claim installation succeeded" in grok
for path in root.rglob("*.md"):
    if ".git" not in path.parts:
        assert "copy-paste/" not in path.read_text(), path
cases = (root / "tests/acceptance-cases.yaml").read_text()
ids = re.findall(r"^  - id: (.+)$", cases, re.M)
assert len(ids) == 22 and len(set(ids)) == 22
assert "status: not-run" in cases
assert "TERMS AND CONDITIONS" in (root / "LICENSE").read_text()
for path in root.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    assert path.suffix not in (".zip", ".xlsx", ".csv", ".pdf"), path
    content = path.read_text()
    assert ("/rails/active_storage/" + "blobs/redirect/") not in content, path
    assert not re.search(r"(?:ghp_|gho_|sk-live-)[A-Za-z0-9]{20,}", content), path
print("PASS references, Grok setup, 22 case definitions, license, public-pack hygiene")
print("Behavioral acceptance and harness/Compute testing remain NOT RUN.")
