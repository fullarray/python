# -*- coding: utf-8 -*-
#
# Django documentation build configuration file, created by
# sphinx-quickstart on Thu Mar 27 09:06:53 2008.
# This file is execfile()d with the current directory set to its containing dir.
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from __future__ import unicode_literals

import sys
from os.path import abspath, dirname, join

# Make sure we get the version of this copy of Django
sys.path.insert(1, dirname(dirname(abspath(__file__))))

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(abspath(join(dirname(__file__), "_ext")))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "djangodocs",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "ticket_role",
]

# Spelling check needs an additional module that is not installed by default.
# Add it only if spelling check is requested so docs can be generated without it.
if 'spelling' in sys.argv:
    extensions.append("sphinxcontrib.spelling")

# Spelling language.
spelling_lang = 'en_US'

# Location of word list.
spelling_word_list_filename = 'spelling_wordlist'

# Add any paths that contain templates here, relative to this directory.
# templates_path = []

# The suffix of source filenames.
source_suffix = '.txt'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'contents'

# General substitutions.
project = 'Django'
copyright = 'Django Software Foundation and contributors'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.9'
# The full version, including alpha/beta/rc tags.
try:
    from django import VERSION, get_version
except ImportError:
    release = version
else:
    def django_release():
        pep386ver = get_version()
        if VERSION[3:5] == ('alpha', 0) and 'dev' not in pep386ver:
            return pep386ver + '.dev'
        return pep386ver

    release = django_release()

# The "development version" of Django
django_next_version = '1.9'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# Location for .po/.mo translation files used when language is set
locale_dirs = ['locale/']

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'trac'

# Links to Python's docs should reference the most recent version of the 3.x
# branch, which is located at this URL.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('http://sphinx-doc.org/', None),
    'six': ('http://pythonhosted.org/six/', None),
    'formtools': ('http://django-formtools.readthedocs.org/en/latest/', None),
    'psycopg2': ('http://initd.org/psycopg/docs/', None),
}

# Python's docs don't change every week.
intersphinx_cache_limit = 90  # days

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "djangodocs"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["_theme"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# HTML translator class for the builder
html_translator_class = "djangodocs.DjangoHTMLTranslator"

# Content template for the index page.
# html_index = ''

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Djangodoc'

modindex_common_prefix = ["django."]

# Appended to every page
rst_epilog = """
.. |django-users| replace:: :ref:`django-users <django-users-mailing-list>`
.. |django-core-mentorship| replace:: :ref:`django-core-mentorship <django-core-mentorship-mailing-list>`
.. |django-developers| replace:: :ref:`django-developers <django-developers-mailing-list>`
.. |django-announce| replace:: :ref:`django-announce <django-announce-mailing-list>`
.. |django-updates| replace:: :ref:`django-updates <django-updates-mailing-list>`
"""

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    'preamble': ('\\DeclareUnicodeCharacter{2264}{\\ensuremath{\\le}}'
                 '\\DeclareUnicodeCharacter{2265}{\\ensuremath{\\ge}}')
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
# latex_documents = []
latex_documents = [
    ('contents', 'django.tex', 'Django Documentation',
     'Django Software Foundation', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('ref/django-admin', 'django-admin', 'Utility script for the Django Web framework', ['Django Software Foundation'], 1),
]


# -- Options for Texinfo output ------------------------------------------------

# List of tuples (startdocname, targetname, title, author, dir_entry,
# description, category, toctree_only)
texinfo_documents = [(
    master_doc, "django", "", "", "Django",
    "Documentation of the Django framework", "Web development", False
)]


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = 'Django Software Foundation'
epub_publisher = 'Django Software Foundation'
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
# epub_basename = 'Django'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
epub_theme = 'djangodocs-epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be an ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
epub_cover = ('', 'epub-cover.html')

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
# epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
# epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
# epub_fix_images = False

# Scale large images.
# epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# epub_show_urls = 'inline'

# If false, no index is generated.
# epub_use_index = True

# -- ticket options ------------------------------------------------------------
ticket_url = 'https://code.djangoproject.com/ticket/%s'
