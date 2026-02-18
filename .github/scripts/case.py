#!/usr/bin/env python3
"""
Find and fix uppercase characters in filenames in docs folder.
"""

import os
import argparse
from pathlib import Path
from collections import defaultdict

GITHUB_ACTIONS = os.environ.get("GITHUB_ACTIONS", "false") == "true"

if GITHUB_ACTIONS:
    warning = "{file}\n::warning file={file}::{message}"
    error = "{file}\n::error file={file}::{message}"
    notice = "::notice ::{message}"
else:
    warning = "WARNING: {message}"
    error = "ERROR: {message}"
    notice = "INFO: {message}"


def find_uppercase_files(root_dir):
    """Find files with uppercase letters, return (files_to_fix, conflicts)."""
    files = []
    seen = defaultdict(list)

    for root, _, filenames in os.walk(root_dir):
        if '_build' in root or '__pycache__' in root:
            continue
        for name in filenames:
            if name != name.lower() and name != "Makefile":
                path = Path(root) / name
                new_path = Path(root) / name.lower()
                seen[str(new_path)].append(str(path))
                files.append({'path': path, 'new_name': name.lower(), 'new_path': new_path})

    conflicts = {k: v for k, v in seen.items() if len(v) > 1}
    return files, conflicts


def find_references(root_dir, filename):
    """Find .rst/.md files referencing filename."""
    refs = []
    for root, _, filenames in os.walk(root_dir):
        if '_build' in root or '__pycache__' in root:
            continue
        for name in filenames:
            if name.endswith(('.rst', '.md')):
                path = Path(root) / name
                try:
                    content = path.read_text(encoding='utf-8')
                    if filename in content:
                        refs.append(path)
                except (UnicodeDecodeError, PermissionError):
                    pass
    return refs


def main():
    parser = argparse.ArgumentParser(description='Find and fix uppercase filenames in docs')
    parser.add_argument('--fix', action='store_true', help='Apply fixes')
    parser.add_argument('--dry-run', action='store_true', help='Show what would change')
    args = parser.parse_args()

    root_dir = 'docs'
    if not os.path.isdir(root_dir):
        print(error.format(file=root_dir, message="Directory does not exist"))
        return 1

    files, conflicts = find_uppercase_files(root_dir)

    if conflicts:
        for target, sources in conflicts.items():
            for src in sources:
                print(warning.format(file=src, message=f"Conflict: would become '{target}'"))
        print(error.format(file="", message=f"{len(conflicts)} naming conflicts found"))
        return 1

    if not files:
        print("No files with uppercase characters found")
        return 0

    for f in files:
        print(warning.format(file=str(f['path']), message=f"Should be: {f['new_name']}"))

    print(f"\nFound {len(files)} files with uppercase characters\n")

    if not args.fix and not args.dry_run:
        print(notice.format(message="Fix case issues by running `python3 .github/scripts/case.py --fix`"))
        return 0

    for f in files:
        old_path, new_path, new_name = f['path'], f['new_path'], f['new_name']
        old_name = old_path.name

        refs = find_references(root_dir, old_name)
        for ref in refs:
            if args.fix:
                content = ref.read_text(encoding='utf-8')
                ref.write_text(content.replace(old_name, new_name), encoding='utf-8')
                print(f"  Updated {ref}")
            else:
                print(f"  Would update {ref}")

        if args.fix:
            os.rename(old_path, new_path)
            print(f"Renamed: {old_name} -> {new_name}")
        else:
            print(f"Would rename: {old_name} -> {new_name}")

    if args.dry_run:
        print("\nDry run complete, no changes made")
    else:
        print(f"\nFixed {len(files)} files")

    return 0


if __name__ == '__main__':
    exit(main())
