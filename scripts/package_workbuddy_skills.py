#!/usr/bin/env python3
"""Build WorkBuddy direct-import skill zips.

WorkBuddy v4.22.11 expects SKILL.md at the top level of each uploaded zip.
This script also keeps UI-facing skill names in Chinese while preserving
stable English zip file names for paths and updates.
"""

from __future__ import annotations

import argparse
import re
import shutil
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = REPO_ROOT / "dist" / "workbuddy-skill-zips"
GLOBAL_CHINA_CONTEXT = REPO_ROOT / "references" / "china-legal-context.md"
MODULE_RE = re.compile(r"当前模块：\*\*(.*?)\*\*；当前技能：\*\*(.*?)\*\*")


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def discover_skill_files() -> list[Path]:
    return sorted(
        p
        for p in REPO_ROOT.rglob("SKILL.md")
        if ".git" not in p.parts and "dist" not in p.parts
    )


def skill_identity(skill_md: Path) -> tuple[Path, str, str, str, str]:
    text = skill_md.read_text(encoding="utf-8")
    match = MODULE_RE.search(text)
    if not match:
        raise ValueError(f"missing Chinese module/skill marker: {skill_md}")

    module_cn, skill_cn = match.group(1).strip(), match.group(2).strip()
    parts = skill_md.relative_to(REPO_ROOT).parts
    skills_idx = parts.index("skills")
    module_root = REPO_ROOT.joinpath(*parts[:skills_idx])
    module_slug = parts[skills_idx - 1]
    skill_slug = "--".join(parts[skills_idx + 1 : -1])
    package_slug = f"{module_slug}--{skill_slug}"
    display_name = f"{module_cn}-{skill_cn}"
    return module_root, package_slug, display_name, module_cn, skill_cn


def update_frontmatter(text: str, display_name: str, module_cn: str, skill_cn: str) -> str:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        raise ValueError("missing YAML frontmatter")

    front = match.group(1)
    body = text[match.end() :]
    front = re.sub(
        r"^name:.*$",
        f"name: {yaml_quote(display_name)}",
        front,
        count=1,
        flags=re.M,
    )

    chinese_intro = (
        f"  用于中国大陆{module_cn}场景下的{skill_cn}。"
        "输出默认简体中文；正式依赖前需法务负责人或执业律师核验。\n"
    )
    if chinese_intro.strip() not in front:
        front = re.sub(
            r"^(description:\s*>\n)",
            r"\1" + chinese_intro,
            front,
            count=1,
            flags=re.M,
        )

    return f"---\n{front}\n---\n{body}"


def rewrite_references_for_zip(text: str) -> str:
    return (
        text.replace("`../../references/china-context.md`", "`references/china-context.md`")
        .replace("`../../../references/china-legal-context.md`", "`references/china-legal-context.md`")
        .replace("`../../../../references/china-context.md`", "`references/china-context.md`")
        .replace("`../../../../../references/china-legal-context.md`", "`references/china-legal-context.md`")
    )


def update_source_names(skill_files: list[Path]) -> int:
    changed = 0
    for skill_md in skill_files:
        _, _, display_name, module_cn, skill_cn = skill_identity(skill_md)
        original = skill_md.read_text(encoding="utf-8")
        updated = update_frontmatter(original, display_name, module_cn, skill_cn)
        if updated != original:
            skill_md.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def add_file(zf: zipfile.ZipFile, source: Path, arcname: str) -> None:
    if source.name in {".DS_Store"}:
        return
    zf.write(source, arcname)


def build_zip(skill_md: Path, out_dir: Path) -> Path:
    module_root, package_slug, display_name, module_cn, skill_cn = skill_identity(skill_md)
    skill_dir = skill_md.parent
    out_path = out_dir / f"{package_slug}.zip"
    skill_text = skill_md.read_text(encoding="utf-8")
    skill_text = update_frontmatter(skill_text, display_name, module_cn, skill_cn)
    skill_text = rewrite_references_for_zip(skill_text)

    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("SKILL.md", skill_text)

        module_claude = module_root / "CLAUDE.md"
        if module_claude.exists():
            add_file(zf, module_claude, "CLAUDE.md")

        module_context = module_root / "references" / "china-context.md"
        if module_context.exists():
            add_file(zf, module_context, "references/china-context.md")

        if GLOBAL_CHINA_CONTEXT.exists():
            add_file(zf, GLOBAL_CHINA_CONTEXT, "references/china-legal-context.md")

        for bundled in sorted(skill_dir.rglob("*")):
            if not bundled.is_file() or bundled.name == "SKILL.md":
                continue
            if "__pycache__" in bundled.parts or bundled.name == ".DS_Store":
                continue
            add_file(zf, bundled, str(bundled.relative_to(skill_dir)))

    return out_path


def build_all(out_dir: Path) -> list[Path]:
    skill_files = discover_skill_files()
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    return [build_zip(skill_md, out_dir) for skill_md in skill_files]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--update-source-names",
        action="store_true",
        help="rewrite source SKILL.md frontmatter names/descriptions to Chinese",
    )
    args = parser.parse_args()

    skill_files = discover_skill_files()
    if args.update_source_names:
        changed = update_source_names(skill_files)
        print(f"Updated source SKILL.md files: {changed}")

    zips = build_all(args.out)
    print(f"Built WorkBuddy skill zips: {len(zips)}")
    print(args.out)


if __name__ == "__main__":
    main()
