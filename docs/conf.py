# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'NSLS-II XAS Workshops'
copyright = '2023-2024, Denis Leshchev, Lu Ma, Bruce Ravel, Eli Stavitski, Akhil Tayal; 2025 Lu Ma, Jorge Moncada Vivas, Bruce Ravel, Eli Stavitski, Akhil Tayal'
author = 'the NSLS-II Hard X-Ray Spectroscopy Group'

# The full version, including alpha/beta/rc tags
release = 'v2025.03'

rst_prolog = open('prolog','r').read()

numfig = True

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_math_dollar', 'sphinx.ext.mathjax',
              'sphinx.ext.todo'
]
todo_include_todos = True

mathjax3_config = {
    'tex2jax': {
        'inlineMath': [ ["\\(","\\)"] ],
        'displayMath': [["\\[","\\]"] ],
    },
}
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_theme_options = {
    "repository_url": "https://github.com/NSLS-II-BMM/XAS_Workshops",
    "use_edit_page_button": False,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    #"extra_navbar": '<p><a href=https://blueskyproject.io><img src="https://blueskyproject.io/_assets/bluesky-logo-dark.svg" style="height: 1.5cm;" alt="Bluesky logo"><br>The Bluesky Project</a></p>',
}

#html_sidebars = {
#    "**": ["sidebar-logo.html", "search-field.html", "sbt-sidebar-nav.html", "sbt-sidebar-footer.html"]
#}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
