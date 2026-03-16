Migrating Wiki Pages
====================

Steps
-----

0. Copy scripts folder outside of a git repository.

1. Edit ``moves.csv`` in the copied folder — add one line per page to move::

      source path, destination path

   Paths are relative to the current directory or absolute paths.
   Source must be under ``documentation/docs/wiki-migration/``.
   Destination can be in any repo (``hdl/``, ``no-OS/``,
   ``documentation/``, etc.). Lines starting with ``#`` are comments.

2. Run the script::

      migrate-pages moves.csv --branch <NAME-OF-PROJECT>
			(for example, the NAME-OF-PROJECT can be AD9009.... something related to the documentation content)

   Use ``--dry-run`` first to preview. Add ``--verbose`` to see every link
   update. The script finds the documentation repo from the CSV source paths.

3. Review the changes:

   The script creates two branches on the documentation repo:

	``wiki_migration/<NAME>_REMAINING-PAGES`` — checks out the reachable
  pages that are **not** being moved, generates an ``index.rst`` with a
  glob toctree, updates ``:doc:`` links to point to the moved pages' new
  locations, and commits.
	- ``wiki_migration/<NAME>_MOVING`` — checks out only the pages being moved.

   - ``wiki_migration/<NAME>_REMAINING-PAGES`` — already committed
   - ``wiki_migration/<NAME>_MOVING`` — staged, not committed

   Review the staged moves::

      cd documentation && git diff --cached

   For cross-repo moves, also review the target repo::

      cd hdl && git diff --cached

4. Commit the ``_MOVING`` branch when satisfied::

      cd documentation && git commit -m "move pages for X"
      cd ../hdl && git commit -m "add migrated pages for X"


What the Script Does
--------------------

The script runs five phases:

**Phase 1 — Parse & Validate.**
Reads the CSV, resolves all paths, detects which git repo each destination
belongs to, and looks up the Sphinx doc root from ``adi_doctools`` lut.py.
The documentation repo is identified from the first CSV source path.

**Phase 2 — BFS Crawl.**
Starting from the CSV source pages as seeds, follows ``:doc:`` links to
discover all reachable pages. These are split into two sets: pages being
moved (from the CSV) and remaining pages.

**Phase 3 — Branch Setup.**
Creates two branches from main (or ``--base``) on the documentation repo:

- ``wiki_migration/<NAME>_REMAINING-PAGES`` — checks out the reachable
  pages that are **not** being moved, generates an ``index.rst`` with a
  glob toctree, updates ``:doc:`` links to point to the moved pages' new
  locations, and commits.
- ``wiki_migration/<NAME>_MOVING`` — checks out only the pages being moved.

Target repos (hdl, no-OS, etc.) get a ``_MOVING`` branch.

**Phase 4 — Move & Update Links.**
Moves each file on the ``_MOVING`` branch and rewrites ``:doc:`` references:

- **Same-repo move** — ``git mv``
- **Cross-repo move** — copies to target repo, ``git rm`` from documentation,
  ``git add`` in target

Link updates in moved files:

- Inside a cross-repo moved file, references back to documentation become
  ``:doc:`documentation:wiki-migration/path```.
- References between pages that both moved to the same repo become local
  ``:doc:`` refs.

**Phase 5 — Stage.**
Stages all changes on the ``_MOVING`` branch. Does **not** commit.


Flags
-----

``--branch NAME``
   Required. Creates ``wiki_migration/<NAME>_MOVING`` and
   ``wiki_migration/<NAME>_REMAINING-PAGES``.

``--dry-run``
   Preview moves and link counts without touching git.

``--verbose``
   Print every individual link replacement.

``--base BRANCH``
   Base branch for the documentation repo (default: ``main``). Target repos
   always branch from their own ``main``.

``--claimed manifest.json [...]``
   Manifest files from prior runs. Pages listed in them are skipped during
   the BFS crawl.


Re-running
----------

The script is safe to re-run on existing branches:

- If the branches already exist, they are checked out instead of created.
- Files already at their destination are skipped (``[skip]``).
- Link updates are re-applied (idempotent).
- The ``_REMAINING-PAGES`` commit is updated if there are new changes.

This means you can add more entries to the CSV and re-run to move additional
pages onto the same branches.


The wiki-migration Branch
-------------------------

The ``wiki-migration`` branch is the source of truth for all 4,677 converted
RST pages. It is **never modified** by this script. The script switches to it
temporarily to read source files and check them out onto the new branches.
