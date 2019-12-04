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
from docutils.parsers.rst import directives

# -- Project information -----------------------------------------------------

project = 'Workflows and Stacks'
copyright = '2019, team useblocks'
author = 'team useblocks'

# The full version, including alpha/beta/rc tags
release = '0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.needs'
]

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
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

##############################
# SPHINX-NEEDS CONFIGURATION #
##############################

needs_role_need_template = "{title}"

needs_types = [dict(directive="workflow", title="Workflow", prefix="WF_", color="#BFD8D2", style="node"),
               dict(directive="stack", title="Stack", prefix="S_", color="#DCB239", style="node"),
               dict(directive="tool", title="Tool", prefix="T_", color="#FEDCD2", style="node"),
               dict(directive="action", title="Action", prefix="A_", color="#DF744A", style="node"),
               ]

needs_extra_links = [
   {
      "option": "requires",
      "incoming": "is required by",
      "outgoing": "requires",
      "copy": False
   },
   {  # Action --> Tool
      "option": "tools",
      "incoming": "actions",
      "outgoing": "tools",
      "copy": False
   },
   {  # Workflow --> Action
      "option": "actions",
      "incoming": "workflows",
      "outgoing": "actions",
      "copy": False
   }
]

needs_extra_options = {
    "homepage": directives.unchanged,
    "license": directives.unchanged,
    "github": directives.unchanged,
    "wikipedia": directives.unchanged,
    "pypi": directives.unchanged,
    # Options filled automatically
    "category": directives.unchanged,  # used by actions
    "github_stars": directives.unchanged,
    "last_commit": directives.unchanged,
    "current_version": directives.unchanged,
}

needs_global_options = {
    'category': ('[[copy("section_name", lower=True)]]', 'type=="action"'),
    'actions': ('[[links_from_content(filter="type==\'action\'")]]', 'type=="workflow"'),
    'tools':  [('[[links_from_content(filter="type==\'tool\'")]]', 'type=="workflow"'),
               ('[[copy(\'id\', filter=\'current_need["sections"][-1]==sections[-1]\')]]', 'type=="action"')]
}
