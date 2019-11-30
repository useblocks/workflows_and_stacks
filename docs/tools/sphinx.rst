Sphinx
======

.. tool:: [[copy('section_name')]]
   :id: SPHINX

   Sphinx is a documentation build system.

.. needtable::
   :filter: 'SPHINX' in id
   :columns: id, title, category

Installation
------------

.. action:: Install Sphinx via pip
   :id: SPHINX_INSTALL
   :tools: SPHINX
   :tags: Installation, Sphinx
   :category: installation

   Execute::

      pip install sphinx

Configuration
-------------

.. action:: Load extensions
   :id: SPHINX_EXTENSION
   :tools: SPHINX
   :tags: Configuration, Sphinx
   :category: configuration

   1. Open ``conf.py`` file with an editor.
   1. Add the extension package name to the parameters ``extensions``.

   Example::

      extensions = ['sphinxcontrib.needs']


Usage
-----

.. action:: Build html
   :id: SPHINX_BUILD_HTML
   :tags: test, Usage, Sphinx, html
   :category: usage

   Blub