Building the Manual
===================

Tool requirements:

- Python 3.12 or later
- Sphinx and the Furo theme, both pinned in ``docs/man/requirements.txt``
- Make, or ``make.bat`` on Windows

Misc

- Git
- latexmk and TeX Live, only if you want a local PDF

Get the project

.. code-block:: shell

	git clone https://github.com/feamsr00/ds8-server-rack-manual.git
	cd ds8-server-rack-manual
	pip install -r docs/man/requirements.txt

MAKE and Makefile
-----------------

`Make <https://www.gnu.org/software/make/>`_ is our build orchestration tool. You will use make to run any tool required for developing on this project. Build settings are configured in ``docs/man/Makefile``.

Build Targets
-------------

.. code-block:: text

	Sphinx v8.2.3
	Please use `make target' where target is one of
	html        to make standalone HTML files
	dirhtml     to make HTML files named index.html in directories
	singlehtml  to make a single large HTML file
	pickle      to make pickle files
	json        to make JSON files
	htmlhelp    to make HTML files and an HTML help project
	qthelp      to make HTML files and a qthelp project
	devhelp     to make HTML files and a Devhelp project
	epub        to make an epub
	latex       to make LaTeX files, you can set PAPER=a4 or PAPER=letter
	latexpdf    to make LaTeX and PDF files (default pdflatex)
	latexpdfja  to make LaTeX files and run them through platex/dvipdfmx
	text        to make text files
	man         to make manual pages
	texinfo     to make Texinfo files
	info        to make Texinfo files and run them through makeinfo
	gettext     to make PO message catalogs
	changes     to make an overview of all changed/added/deprecated items
	xml         to make Docutils-native XML files
	pseudoxml   to make pseudoxml-XML files for display purposes
	linkcheck   to check all external links for integrity
	doctest     to run all doctests embedded in the documentation (if enabled)
	coverage    to run coverage check of the documentation (if enabled)
	clean       to remove everything in the build directory

Reproducible builds
^^^^^^^^^^^^^^^^^^^

If you update a pip package to add a feature or fix a bug, please be sure to commit ``docs/man/requirements.txt`` as well. This ensures that local and published builds use the same tools.
