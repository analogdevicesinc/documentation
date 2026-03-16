Migrating Wiki Pages
====================

Steps
-----

1. Edit ``moves.csv`` — add one line per page to move::

      source path, destination path

   Paths are relative to the current directory or absolute paths.
   Source must be under ``documentation/docs/wiki-migration/``.
   Destination can be in any repo (``hdl/``, ``no-OS/``,
   ``documentation/``, etc.). Lines starting with ``#`` are comments.

2. Run the script ::

      migrate-pages moves.csv --branch <PROJECT-BRANCH-NAME>

   Use ``--dry-run`` first to preview. Add ``--verbose`` to see every link
   update.

3. Review the staged changes in each affected repo::

      cd doc-migration/documentation && git diff --cached
      cd ../hdl && git diff --cached

4. Commit when satisfied::

      cd doc-migration/documentation && git commit -m "migrate pages for X"
      cd ../hdl && git commit -m "add migrated pages for X"


What the Script Does
--------------------

The script runs five phases:

**Phase 1 — Parse & Validate.**
Reads the CSV, resolves all paths, detects which git repo each destination
belongs to, and looks up the Sphinx doc root from ``adi_doctools`` lut.py.

**Phase 2 — BFS Crawl.**
Starting from the CSV source pages as seeds, follows ``:doc:`` links to
discover all reachable pages. These are checked out onto the new branch so
cross-references resolve.

**Phase 3 — Branch Setup.**
Creates ``wiki_migration/<NAME>`` from main (or ``--base``) on the
documentation repo and on each target repo. Checks out the reachable
``.rst`` files from the ``wiki-migration`` branch. Generates an
``index.rst`` with a glob toctree.

**Phase 4 — Move & Update Links.**
Moves each file and rewrites ``:doc:`` references and toctree entries
across all checked-out pages:

- **Same-repo move** — ``git mv``
- **Cross-repo move** — copies to target repo, ``git rm`` from documentation,
  ``git add`` in target

Link updates:

- References to a moved page become ``:doc:`hdl:new/path``` (intersphinx)
  or ``:doc:`/new/path``` (same repo).
- Inside a cross-repo moved file, references back to documentation become
  ``:doc:`documentation:wiki-migration/path```.
- References between pages that both moved to the same repo become local
  ``:doc:`` refs.

**Phase 5 — Stage.**
Stages all changes. Does **not** commit.


Flags
-----

``--branch NAME``
   Required. Creates branch ``wiki_migration/<NAME>`` on all repos.

``--dry-run``
   Preview moves and link counts without touching git.

``--verbose``
   Print every individual link replacement.

``--base BRANCH``
   Base branch for the documentation repo (default: ``main``). Target repos
   always branch from their own ``main``.

``--claimed manifest.json [...]``
   Manifest files from prior ``start-migration`` runs. Pages listed in them
   are skipped during the BFS crawl.


Re-running
----------

The script is safe to re-run on an existing branch:

- If ``wiki_migration/<NAME>`` already exists, it checks it out instead of
  creating it.
- Files already at their destination are skipped (``[skip]``).
- Link updates are re-applied to the freshly checked-out wiki-migration
  files (idempotent — produces no net change if links were already correct).

This means you can add more entries to the CSV and re-run to move additional
pages onto the same branch.


The wiki-migration Branch
-------------------------

The ``wiki-migration`` branch is the source of truth for all 4,677 converted
RST pages. It is **never modified** by this script. The script switches to it
temporarily to read source files and check them out onto the new branch.
