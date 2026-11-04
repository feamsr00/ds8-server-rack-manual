# Configuration for the DS-8 Server Rack manual.
# See https://www.sphinx-doc.org/en/master/usage/configuration.html

project = 'DS-8 Server Rack'
copyright = '2026, feamsr00'
author = 'feamsr00'
version = release = '5.12.7'

extensions = []
exclude_patterns = []

html_theme = 'furo'
html_title = 'DS-8 Server Rack: unofficial manual'
html_theme_options = {
	'navigation_with_keys': True,
	'source_repository': 'https://github.com/feamsr00/ds8-server-rack-manual/',
	'source_branch': 'main',
	'source_directory': 'docs/man/source/',
}

# PDF only. pdflatex has no glyph for the minus sign, chapters, tables and figures
# are numbered by hand, figures should stay next to the text that introduces them, and a PDF
# read on screen is better without blank left-hand pages.
latex_documents = [('index', 'ds-8serverrack.tex', 'DS-8 Server Rack: User and Developer Manual', 'feamsr00', 'manual')]
latex_elements = {
	'preamble': r'\DeclareUnicodeCharacter{2212}{\ensuremath{-}}\setcounter{secnumdepth}{-1}\setcounter{tocdepth}{1}\usepackage{caption}\captionsetup{labelformat=empty}',
	'figure_align': 'H',
	'extraclassoptions': 'openany,oneside',
}

# The Index in the contents is an HTML page, so the other formats need not warn about it.
def _quiet_index_warning(app):
	if app.builder.format != 'html':
		app.config.suppress_warnings.append('toc.not_readable')

def setup(app):
	app.connect('builder-inited', _quiet_index_warning)
