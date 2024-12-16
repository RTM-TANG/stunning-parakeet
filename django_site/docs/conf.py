# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

import django

# Note: You may need to change the path to match
# your project's structure
sys.path.insert(0, os.path.abspath(".."))  # For discovery of Python modules
sys.path.insert(0, os.path.abspath("."))  # For finding the django_settings.py file

# This tells Django where to find the settings file
os.environ["DJANGO_SETTINGS_MODULE"] = "django_settings"
# This activates Django and makes it possible for Sphinx to
# autodoc your project
django.setup()

project = 'django_site'
copyright = '2024, TANG'
author = 'TANG'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
