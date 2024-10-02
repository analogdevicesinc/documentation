.. _docs_guidelines:

Documentation guidelines
================================================================================

This documentation is built with `Sphinx <https://www.sphinx-doc.org>`_ and
all source code is available at the path :git-documentation:`docs`.

To contribute to it, open a pull request with the changes to
:git-documentation:`this repository </>`, just make sure to read the general
:ref:`doctools:docs_guidelines` first **and** the additional guidelines
below specific to the System Level Documentation repository.

Templates
--------------------------------------------------------------------------------

Templates are available:

.. note::

   No template is available yet.

Remove the ``:orphan:`` in the first line, it is to hide the templates from the
`TOC tree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`_,
and make sure to remove any placeholder text and instructive comment.

.. note::

   The old wiki uses `dokuwiki <https://www.dokuwiki.org/dokuwiki>`_. When
   importing text from there, consider ``pandoc`` and the tips accross the
   :external+doctools:ref:`docs_guidelines` to convert it to reST.
