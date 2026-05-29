# Configuration file for the Sphinx documentation builder.
import sys
import os
from datetime import datetime
from pathlib import Path

from sphinx.environment import BuildEnvironment

# Add the source directory to Python path for custom modules (e.g., screenshot_helpers)
sys.path.insert(0, str(Path(__file__).parent.absolute()))

# Compatibility shim for extensions that still use the removed private
# BuildEnvironment._app attribute on newer Sphinx versions.
# Test and try to remove with later >= 9.0 sphinx versions

if not hasattr(BuildEnvironment, "_app"):
    BuildEnvironment._app = property(lambda self: self.app)

# import custom screenshot helper functions
from _scripts.screenshots import make_screenshots

# get the screenshot directives
from screenshots import screenshots
import sphinx_autosummary_accessors
import orc_api

current_time = datetime.now()
current_year = current_time.year
project = 'OpenRiverCam Operating System'
copyright = f'{current_year}, Rainbow Sensing'
author = 'Hessel C. Winsemius'
release = orc_api.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "sphinxcontrib.screenshot",
    "matplotlib.sphinxext.plot_directive",
    "sphinxcontrib.programoutput",
    "sphinxcontrib.youtube",
    "sphinx_autosummary_accessors",
    "sphinx_design"
]
templates_path = ['_templates', sphinx_autosummary_accessors.templates_path]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = ".rst"
master_doc = "index"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ["theme-localdevices.css", "docs.css"]
html_logo = "_static/orc_logo_color.svg"
html_favicon = "_static/orc_favicon.svg"


html_theme_options = {
    "show_nav_level": 2,
    "navbar_align": "content",
    # "use_edit_page_button": True,
    "icon_links": [
        {
            "name": "Local Devices",
            "url": "https://openrivercam.org",
            "icon": "_static/orc_logo_color.svg",
            "type": "local",
        },
    ],
    "logo": {
        "text": f"ORC-OS {release}"
    }
}

html_context = {
    "github_url": "https://github.com",  # or your GitHub Enterprise interprise
    "github_user": "localdevices",
    "github_repo": "ORC-OS",
    "github_version": "docs",
    "doc_path": "docs",
}


remove_from_toctrees = ["_generated/*", "_build/doctrees/*"]

# create screenshots

make_screenshots(screenshots, overwrite=False)
