#!/usr/bin/env python3
"""
Find and remove dangling files (not referenced in any .rst files) in docs folder.
"""

import os
import argparse
import subprocess
from pathlib import Path

GITHUB_ACTIONS = os.environ.get("GITHUB_ACTIONS", "false") == "true"

if GITHUB_ACTIONS:
    warning = "{file}\n::warning file={file}::{message}"
    error = "{file}\n::error file={file}::{message}"
    notice = "::notice ::{message}"
else:
    warning = "WARNING: {file} - {message}"
    error = "ERROR: {message}"
    notice = "INFO: {message}"

EXCLUDE_FILES = {
    'conf.py', 'Makefile', 'make.bat', '.gitignore', '.gitattributes',
    'requirements.txt',
    'custom.css', 'adi_logo.svg', 'icon.svg',
}

EXCLUDE_EXTENSIONS = {'.rst', '.md'}

SKIP_DIRS = {'_build', '__pycache__', '.git'}


def find_all_files(root_dir):
    """Find all files that could potentially be dangling."""
    files = []
    for root, dirs, filenames in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for name in filenames:
            path = Path(root) / name
            ext = path.suffix.lower()

            if ext in EXCLUDE_EXTENSIONS:
                continue
            if name in EXCLUDE_FILES:
                continue

            files.append(path)

    return files


def find_rst_files(root_dir):
    """Find all .rst files in the docs folder."""
    rst_files = []
    for root, dirs, filenames in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for name in filenames:
            if name.endswith('.rst'):
                rst_files.append(Path(root) / name)

    return rst_files


def load_rst_contents(rst_files):
    """Load contents of all .rst files into a single string for fast searching."""
    contents = {}
    for rst_file in rst_files:
        try:
            contents[rst_file] = rst_file.read_text(encoding='utf-8')
        except (UnicodeDecodeError, PermissionError):
            pass
    return contents


def is_file_referenced(file_path, rst_contents):
    """Check if a file is referenced in any .rst file."""
    filename = file_path.name

    for rst_file, content in rst_contents.items():
        rel_path = os.path.relpath(file_path, rst_file.parent)
        if rel_path in content:
            return True

    return False


def find_dangling_files(root_dir):
    """Find files that are not referenced in any .rst file."""
    all_files = find_all_files(root_dir)
    rst_files = find_rst_files(root_dir)
    rst_contents = load_rst_contents(rst_files)

    dangling = []
    for file_path in all_files:
        if not is_file_referenced(file_path, rst_contents):
            dangling.append(file_path)

    return dangling


def git_rm(file_path, dry_run=False):
    """Remove a file using git rm."""
    if dry_run:
        print(f"  Would run: git rm {file_path}")
        return True

    try:
        result = subprocess.run(
            ['git', 'rm', str(file_path)],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"  Removed: {file_path}")
            return True
        else:
            print(f"  Failed to remove {file_path}: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"  Error removing {file_path}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Find and remove dangling files in docs')
    parser.add_argument('--fix', action='store_true', help='Remove dangling files with git rm')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be removed')
    args = parser.parse_args()

    root_dir = 'docs'
    if not os.path.isdir(root_dir):
        print(error.format(file=root_dir, message="Directory does not exist"))
        return 1

    dangling = find_dangling_files(root_dir)

    if not dangling:
        print("No dangling files found")
        return 0

    for f in dangling:
        print(warning.format(file=str(f), message="Not referenced in any .rst file"))

    print(f"\nFound {len(dangling)} dangling files\n")

    if not args.fix and not args.dry_run:
        print(notice.format(message="Remove dangling files by running `python3 .github/scripts/dangling.py --fix`"))
        return 1

    removed = 0
    for f in dangling:
        if git_rm(f, dry_run=args.dry_run):
            removed += 1

    if args.dry_run:
        print(f"\nDry run complete, {removed} files would be removed")
    else:
        print(f"\nRemoved {removed} dangling files")

    return 0


if __name__ == '__main__':
    exit(main())
