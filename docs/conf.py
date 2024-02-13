# -- Project information -----------------------------------------------------

repository = 'documentation'
project = 'System Level, Analog Devices'
copyright = '2024, Analog Devices Inc'
author = 'Analog Devices Inc'

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "adi_doctools"
]

needs_extensions = {
    'adi_doctools': '0.3'
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'

# -- External docs configuration ----------------------------------------------

intersphinx_mapping = {
    'doctools': ('https://analogdevicesinc.github.io/doctools', None),
    'hdl': ('https://analogdevicesinc.github.io/hdl', None),
    'no-os': ('https://analogdevicesinc.github.io/no-os', None)
}

intersphinx_disabled_reftypes = ["*"]

# -- Custom extensions configuration ------------------------------------------

is_system_top = True
hide_collapsible_content = True
validate_links = False

# -- todo configuration -------------------------------------------------------

todo_include_todos = True
todo_emit_warnings = True

# -- Options for HTML output --------------------------------------------------

html_theme = 'cosmic'
html_static_path = ['sources']
html_css_files = ["custom.css"]
html_favicon = "sources/icon.svg"
