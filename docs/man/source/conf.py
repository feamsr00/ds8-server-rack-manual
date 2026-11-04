# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DS-8 Server Rack'
copyright = '2026, feamsr00'
author = 'feamsr00'
release = '5.12.7'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pyramid'
# html_static_path = ['_static']

# PDF only: pdflatex has no glyph for the minus sign, and the chapters are numbered by hand
latex_elements = {'preamble': r'\DeclareUnicodeCharacter{2212}{\ensuremath{-}}\setcounter{secnumdepth}{-1}\setcounter{tocdepth}{1}'}


import re

def process_docstring(app, what, name, obj, options, lines):
    spaces_pat = re.compile(r"( {8})")
    ll = []
    for l in lines:
        ll.append(spaces_pat.sub("    ",l))
    lines[:] = ll

def setup(app):
    app.connect('autodoc-process-docstring', process_docstring)
