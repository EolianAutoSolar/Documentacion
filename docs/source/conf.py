# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
sys.setrecursionlimit(1500)

version = '1.0.0'  # Reemplaza con la versión actual

html_logo = 'logo_eolian_blanco (1).png'
html_theme_options = {
    'logo_only': False,  # Mostrar el logo y el texto del proyecto
    'display_version': True,  # Mostrar la versión del proyecto
}

html_favicon = 'mini.png'  # Icono de la pestaña del navegador

project = 'Documentacion'
copyright = '2024, Eolian'
author = ':D'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinxcontrib.drawio"]

templates_path = ['_templates']
exclude_patterns = []

pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
