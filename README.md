# System Level Documentation

The System Level Documentation is the top documentation for Hardware, Projects, and some Linux documentation;
it also has the ability to aggregate every other documentation into a single monolithic output/website.

## Building the documentation

Ensure pip is newer than version 23.
```
pip install pip --upgrade
```
Install the documentation tools.
```
(cd docs ; pip install -r requirements.txt)
```
Build the libraries (recommended).
```
(cd library ; make)
```
Build the documentation with Sphinx.
```
(cd docs ; make html)
```
The generated documentation will be available at `docs/_build/html`.

## Building the monolithic documentation

The monolithic version aggregates all ADI's documentation into a single output/webpage.
To generate it, install the tools at the last topic, then do:
```
./ci/monolithic.sh
```
The output will be written to `docs-mono/_build/html`.
