#!/bin/bash

declare -A repos

repos[hdl]="git@github.com:analogdevicesinc/hdl.git"
repos[doctools]="git@github.com:analogdevicesinc/doctools.git"

cli_info="./ci/monolithic [--extra]"
if [ ! -d ci ]; then
	echo "Wrong path, run from the top-level path: $cli_info"
	exit 1
fi

if [ $# -eq 0 ]; then
	echo "Extra features disabled, use --extra to enable."
	extra=0
else
	while [ "$1" != "" ]; do
		case $1 in
			--extra )
				extra=1
				;;
			* )
				echo "Usage: $0 [--extra]"
				exit 1
				;;
		esac
		shift
	done
fi

if [[ -d docs-mono ]]
then
	rm -r docs-mono
fi

mkdir docs-mono
cp -r docs/* docs-mono/

if [[ ! -d repos ]]
then
	mkdir repos
fi

for i in "${!repos[@]}"; do
	if [[ ! -d repos/$i ]]
	then
		echo Cloning $i repository...
		git clone ${repos[$i]} repos/$i
	else
		echo Pulling $i repository...
		(cd repos/$i ; git pull)
	fi

	mkdir docs-mono/$i
	pushd .
	cd repos/$i/docs
	for dir in */; do
		dir="${dir%/}"
		if [ "$dir" != "_build" ] && [ "$dir" != "extensions" ] && [ "$dir" != "sources" ]; then
			cp -r $dir ../../../docs-mono/$i
		fi
	done
	popd

	# Prefixes references with repo name, expect already external references :ref:`repo:str`
	# Patch :ref:`str` into :ref:`$i str`
	find docs-mono/$i -type f -exec sed -i -E "s/(:ref:\`)([^<>:]+)(\`)/\\1$i \\2\\3/g" {} \;
	# Patch:ref:`Title <str>` into :ref:`Title <$i str>`
	find docs-mono/$i -type f -exec sed -i -E "s/(:ref:\`)([^<]+)( <)([^:>]+)(>)/\\1\\2\\3$i \\4\\5/g" {} \;
	# Patch ^.. _str:$ into .. _$i str:
	find docs-mono/$i -type f -exec sed -i -E "s/^(.. _)([^:]+)(:)\$/\\1$i \\2\\3/g" {} \;
	# Patch ^.. _str: into .. _$i str: (FORBIDDEN, used for in page/local references)
	# Patch `str`_ into `$1 strl`_ (FORBIDDEN, used for in page/local references)
	#find docs-mono -type f -exec sed -i -E "s/(\`)([^<>]+)(\`_)/\1$i \2\3/g" {} \;
done

# Convert external references into local prefixed
for i in "${!repos[@]}";
do
	find docs-mono -type f -exec sed -i "s|ref:\`$i:|ref:\`$i |g" {} \;
done
find docs-mono -type f -exec sed -i "s|<|<|g" {} \;

# Patch repos index.rst into index.rst
for i in "${!repos[@]}"; do
	python3 ci/patch_index.py "$i" "docs-mono/index.rst"
done

# Repo specific tasks
if [ $extra -eq 1 ]; then
	(cd repos/hdl/library; make all -j4)
fi

(cd docs-mono ; make html)
