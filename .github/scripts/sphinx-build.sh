#!/bin/bash

_sparse_args() {
	local files
	files=$(git diff --diff-filter=ACM --no-renames --name-only \
		"$base_sha..$head_sha" 2>/dev/null \
		| grep -E "^docs/" || true)
	[[ -z "$files" ]] && return

	mapfile -t file_arr <<< "$files"

	python3 - "./docs" "${file_arr[@]}" <<'EOF'
import sys
from adi_doctools.cli.serve import compute_sparse_config

directory = sys.argv[1]
sparse    = sys.argv[2:]

confoverrides = compute_sparse_config(directory, sparse, verbose=False)
for key, value in confoverrides.items():
    if isinstance(value, list):
        print(f"-D {key}={','.join(value)}")
    else:
        print(f"-D {key}={value}")
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

	local sparse_args=()
	if [[ "$GITHUB_EVENT_NAME" == "pull_request" ]]; then
		while IFS=' ' read -r flag value; do
			[[ -n "$flag" ]] && sparse_args+=("$flag" "$value")
		done < <(_sparse_args)
		echo "got sparse args: ${sparse_args[*]}"
	fi

	pushd ./docs
	sphinx-build -b html $j_ -w "$warnfile" . _build/html --keep-going \
		"${sparse_args[@]}" || err=$?
        rm -rf _build/html/_sources
	popd

	# Filter false positives due to https://github.com/sphinx-doc/sphinx/pull/14325
	if grep -q "toctree glob pattern.*didn't match any documents" "$warnfile"; then
		echo "::notice ::Warning 'toctree glob pattern...' is a false positive, please ignore."
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
