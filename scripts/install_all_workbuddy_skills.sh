#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
zip_dir="$repo_root/dist/workbuddy-skill-zips"
dest_dir="${WORKBUDDY_SKILLS_DIR:-$HOME/.workbuddy/skills}"
force=0

for arg in "$@"; do
  case "$arg" in
    --force)
      force=1
      ;;
    -h|--help)
      echo "Usage: $0 [--force]"
      echo "Installs all zips from dist/workbuddy-skill-zips into ~/.workbuddy/skills."
      echo "Use --force to replace existing same-named skill folders."
      exit 0
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      exit 2
      ;;
  esac
done

if [ ! -d "$zip_dir" ]; then
  echo "Missing zip directory: $zip_dir" >&2
  echo "Run: python3 scripts/package_workbuddy_skills.py" >&2
  exit 1
fi

mkdir -p "$dest_dir"

installed=0
skipped=0
for zip_path in "$zip_dir"/*.zip; do
  [ -e "$zip_path" ] || continue
  skill_id="$(basename "$zip_path" .zip)"
  target="$dest_dir/$skill_id"
  if [ -d "$target" ]; then
    if [ "$force" -eq 1 ]; then
      rm -rf "$target"
    else
      echo "skip existing: $skill_id"
      skipped=$((skipped + 1))
      continue
    fi
  fi
  mkdir -p "$target"
  unzip -q "$zip_path" -d "$target"
  installed=$((installed + 1))
done

echo "Installed: $installed"
echo "Skipped: $skipped"
echo "Destination: $dest_dir"
echo "Restart WorkBuddy, then open a new task and click the skill selector."
