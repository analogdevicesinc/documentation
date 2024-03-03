# -- Project information -----------------------------------------------------

repository = 'documentation'
project = 'System Level Documentation'
copyright = '2024, Analog Devices, Inc.'
author = 'Analog Devices, Inc.'

# -- General configuration ---------------------------------------------------

extensions = [
    "adi_doctools"
]

needs_extensions = {
    'adi_doctools': '0.3.17'
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'

# -- External docs configuration ----------------------------------------------

interref_repos = ['doctools']

# -- Custom extensions configuration ------------------------------------------

hide_collapsible_content = True
validate_links = False

pseudo_subdomains = {
    'eval': 'Evaluation Boards',
    'university': 'University Program',
}

# -- Options for HTML output --------------------------------------------------

html_theme = 'cosmic'
html_static_path = ['sources']
html_css_files = ["custom.css"]
html_favicon = "sources/icon.svg"
