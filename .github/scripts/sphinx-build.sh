#!/bin/bash

_sparse_patch_conf() {
	[[ "$GITHUB_EVENT_NAME" != "pull_request" ]] && return

	local files
	files=$(git diff --diff-filter=ACM --no-renames --name-only \
		"$base_sha..$head_sha" 2>/dev/null \
		| grep -E "^docs/" || true)
	[[ -z "$files" ]] && return

	mapfile -t file_arr <<< "$files"
	python3 - "./docs" "${file_arr[@]}" <<'EOF'
import sys
from adi_doctools.cli.serve import compute_sparse_config

confoverrides = compute_sparse_config(sys.argv[1], sys.argv[2:], verbose=False)
if not confoverrides:
    sys.exit(0)

lines = ["\n# sparse build overrides\n"]
for key, value in confoverrides.items():
    lines.append(f"{key} = {repr(value)}\n")
block = ''.join(lines)

with open(f"{sys.argv[1]}/conf.py", 'a') as f:
    f.write(block)

print(block, end='')
EOF
}

_file() {
	local f="$1"
	f="${f#$PWD/}"
	echo "$f"
}

sphinx_build() {
	local err=0
	local step_name="sphinx"
	local warnfile=$(mktemp -t sphinx.XXX)

	local patch
	patch=$(_sparse_patch_conf)
	if [[ -n "$patch" ]]; then
		echo "sphinx: sparse build overrides:"
		echo "$patch"
	fi

	pushd ./docs
	sphinx-build -b html $j_ -w "$warnfile" . _build/html --keep-going || err=$?
	rm -rf _build/html/_sources
	popd

	# Filter false positives due to https://github.com/sphinx-doc/sphinx/pull/14325
	if grep -q "toctree glob pattern.*didn't match any documents" "$warnfile"; then
		echo "::notice ::Sphinx's warning 'toctree glob pattern...' is a false positive, please ignore."
	fi
	sed -i "/toctree glob pattern.*didn't match any documents/d" "$warnfile"

	while IFS= read -r line; do
		if [[ "$line" =~ ^(.+):([0-9]+):\ (WARNING|CRITICAL|ERROR):\ (.*)$ ]]; then
			file="${BASH_REMATCH[1]}"
			lineno="${BASH_REMATCH[2]}"
			level="${BASH_REMATCH[3]}"
			msg="${BASH_REMATCH[4]}"
			[[ "$level" == "WARNING" ]] && type="warning" || type="error"
			echo "::$type file=$(_file "$file"),line=$lineno::$step_name: $msg"
		elif [[ "$line" =~ ^(.+)::\ (WARNING|CRITICAL|ERROR):\ (.*)$ ]]; then
			file="${BASH_REMATCH[1]}"
			level="${BASH_REMATCH[2]}"
			msg="${BASH_REMATCH[3]}"
			[[ "$level" == "WARNING" ]] && type="warning" || type="error"
			echo "::$type file=$(_file "$file"),line=0::$step_name: $msg"
		elif [[ "$line" =~ ^(.+):\ (WARNING|CRITICAL|ERROR):\ (.*)$ ]]; then
			file="${BASH_REMATCH[1]}"
			level="${BASH_REMATCH[2]}"
			msg="${BASH_REMATCH[3]}"
			[[ "$level" == "WARNING" ]] && type="warning" || type="error"
			echo "::$type file=$(_file "$file"),line=0::$step_name: $msg"
		fi
	done < "$warnfile"

	# Replicates -W
	if [[ $err -eq 0 ]]; then
		local warnings
		warnings=$(grep -cE '(WARNING|CRITICAL|ERROR):' "$warnfile" || true)
		[[ "$warnings" -gt 0 ]] && err=1
	fi

	rm $warnfile

	return $err
}
