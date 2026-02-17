# System Level Documentation

The System Level Documentation is the top documentation for Hardware, Projects, and some Linux documentation;
it also has the ability to aggregate every other documentation into a single monolithic output/website.

See the deployed docs output at the [System Level Documentation](https://analogdevicesinc.github.io/documentation/) index.

## Getting started

The repository uses Git LFS to host large files.
To not download all large files at the HEAD commit, we recommend `--skip-smudge` and letting [adoc serve](https://analogdevicesinc.github.io/doctools/cli.html#serve) to fetch them as you navigate the live server and touches files:

```
sudo apt install git-lfs -y
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/analogdevicesinc/documentation \
    --origin public \
    --depth 10 \
    -- documentation
cd documentation
git lfs install --local --force --skip-smudge
```

Install the documentation tools.
```
python3 -m venv ./venv
source ./venv/scripts/activate
python3 -m ensurepip
pip install pip --upgrade
(cd docs ; pip install -r requirements.txt --upgrade)
```
Launch the live server.
```
adoc serve
```
Or build the documentation with Sphinx.
```
(cd docs ; make html)
```
The generated documentation will be available at `docs/_build/html`.

## Build all documentations

It's possible to build all ADI's documentation at once in parallel.
To generate it, considering Doctools is installed, do:
```
adoc aggregate -d docs_output
```
See [Doctools](https://github.com/analogdevicesinc/doctools) for more information.
