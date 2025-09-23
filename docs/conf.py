# -- Import setup -------------------------------------------------------------

from os import path

# -- Project information -----------------------------------------------------

repository = 'documentation'
project = 'System Level Documentation'
copyright = '2025, Analog Devices, Inc.'
author = 'Analog Devices, Inc.'

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.todo",
    "adi_doctools"
]

needs_extensions = {
    'adi_doctools': '0.3.50'
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'

# -- External docs configuration ----------------------------------------------

interref_repos = [
    'doctools',
    'hdl',
    'pyadi-iio',
    'adi-kuiper-gen',
    'scopy',
    'no-OS',
    'precision-converters-firmware',
]

# -- Options for HTML output --------------------------------------------------

html_theme = 'cosmic'
html_favicon = path.join("sources", "icon.svg")
numfig = True
numfig_per_doc = True

numfig_format = {'figure': 'Figure %s',
                 'table': 'Table %s',
                 'code-block': 'Listing %s',
                 'section': 'Section %s'}

# -- Show TODOs ---------------------------------------------------------------

todo_include_todos = True
