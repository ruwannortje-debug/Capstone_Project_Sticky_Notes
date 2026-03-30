"""Sphinx configuration for the Sticky Notes project."""

import os
import sys

import django

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'sticky_notes.settings'
django.setup()

project = 'Sticky Notes'
copyright = '2026, Ruwan Nortje'
author = 'Ruwan Nortje'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'alabaster'
html_static_path = ['_static']
