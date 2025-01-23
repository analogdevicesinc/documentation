.. _forking-publishing:

Forking and publishing
======================

The steps below are a walk-through to contribute to
:git-documentation:`this </>` repository,
It ensures that GitHub Actions and GitHub Pages are enabled, so you can run
continuous integration and see the pages live at *<your_user>.github.io/documentation*,
and `git-lfs <https://git-lfs.com/>`__ artifacts are properly synced.

.. note::

   Using the Python virtual environment (venv) is recommended, but if you wish
   to not use it, skip steps in :green:`green`.

Preparing your origin
---------------------

There is three options to contribute:

* :ref:`forking-publishing fork`: that want to use the GitHub flow (recommended).
* :ref:`forking-publishing copy`: that want to work privately first.
* :ref:`forking-publishing branch`: with write access to *analogdevicesinc* organization.

.. tip::

   If using Github Codespaces, just fork/create a branch/copy and follow
   :ref:`this section <forking-publishing github-codespaces>`.

.. _forking-publishing fork:

Fork
~~~~

Fork the *analogdevicesinc/documentation* repo on your account.

| **Enable the workflows** on the forked repo at *github.com/<your_user>/documentation/actions*
  by clicking the green button
| "I understand my workflows, go ahead and enable them".

Ensure git-lfs is installed with:

.. code:: bash

   sudo apt install git-lfs -y

Clone the repository:

.. shell::

   $git clone https://github.com/<your_user>/documentation \
   $    --depth=10 -- documentation
   $cd documentation

.. _forking-publishing copy:

Copy
~~~~

Ensure git-lfs is installed with:

.. code:: bash

   sudo apt install git-lfs -y

Clone mainland:

.. shell::

   $git clone https://github.com/analogdevicesinc/documentation \
   $    --depth=10 -- documentation
   $cd documentation

Setup both origins, for example, call *analogdevicesinc* ``public`` and your
copy ``private`` at the *.git/config*, similar to:

::

   [core]
   	repositoryformatversion = 0
   	filemode = true
   	bare = false
   	logallrefupdates = true
   [remote "public"]
   	url = https://github.com/analogdevicesinc/documentation.git
   	fetch = +refs/heads/*:refs/remotes/public/*
   [remote "private"]
   	url = https://github.com/<your_user>/documentation.git
   	fetch = +refs/heads/*:refs/remotes/private/*
   [branch "main"]
        # Set your private copy as upstream
   	remote = private
   	merge = refs/heads/main


Push the working branch to your copy.

.. shell::

   ~/documentation
   $git push private main:main

Fetch from *analogdevicesinc* and push to your copy the large files binaries:

.. shell::

   ~/documentation
   $git lfs fetch --all public
   $git lfs push --all private

.. _forking-publishing branch:

Branch
~~~~~~

If you have write permission to the repository, you shall add your work to a
branch at mainland, then just:

Ensure git-lfs is installed with:

.. code:: bash

   sudo apt install git-lfs -y


Clone the repository

.. shell::

   $git clone https://github.com/analogdevicesinc/documentation \
   $    --depth=10 \
   $    -- documentation
   $cd documentation

Create and checkout a branch

.. shell::

   ~/documentation
   $git checkout -b <your_branch>

Preparing your environment
--------------------------

It is possible to contribute:

* :ref:`forking-publishing local` (most freedom); or with
* A :ref:`forking-publishing github-codespaces`.

Follow either tutorial to bring up the environment.

.. _forking-publishing local:

Using your local host
~~~~~~~~~~~~~~~~~~~~~

To prepare your environment to work **locally**,
clone and build the doc for the first time (working directory: repo root):

Ensure pip is up-to-date:

.. code:: bash

   pip install pip --upgrade

:green:`Setup the virtual env at the repo root path:`

.. shell::

   ~/documentation
   $python -m venv ./venv

:green:`Activate the virtual env`:

.. shell::

   ~/documentation
   $source ./venv/scripts/activate

Install the requirements:

.. shell::

   ~/documentation
   $(cd docs ; pip install -r requirements.txt --upgrade)

Build the doc (output at docs/_build/html):

.. shell::

   ~/documentation
   $(cd docs ; make html)

.. _forking-publishing github-codespaces:

GitHub Codespace
~~~~~~~~~~~~~~~~

Instead of working locally, you can use a cloud virtual machine with
GitHub Codespaces.

GitHub Codespaces uses the :git-documentation:`.devcontainer.json` file to
initialize a container in the cloud.
This container is pre-configured with all the tools required to build the
documentation, including the live preview daemon  :external+doctools:ref:`serve`,
which is automatically started.
This setup provides a user experience comparable to platforms like Google Docs
or Overleaf.

.. caution::

   | GitHub Codespaces usage is billed to the user (you)!
   | Be sure to understand GitHub's billing policies and your account free quota.

To use GitHub Codespaces, navigate to the
:git-documentation:`GitHub GUI for this repository <+>` and click
*Code > Codespaces > Create codespace on main*.

This will open a new tab and set up the virtual environment.
The setup is complete  when the live preview panel appears on the right.

To manage all your GitHub Codespaces and shut them down, visit
`github.com/codespaces <https://github.com/codespaces>`__.

Adding content
--------------

Add a new topic and pages (working directory: docs).

On *index.rst*, add a new topic:

::

   .. toctree::
      :caption: My new topic
      :maxdepth: 2

       my_topic/index

Or add to an existing, for example, in *eval/index.rst*.

.. tip::

   Don't overthink the location at this point, it can be easily moved later.

Create a new folder and file matching the entry from last step:

.. shell::

   ~/documentation/docs
   $mkdir my_topic; touch my_topic/index.rst

Edit *my_topic/index.rst*, adding a title and some content.

Build the doc and see the changes.

Commit the changes.

For a extensive guide on adding content see :ref:`creating-new-pages`.

Pushing and triggering the CI
-----------------------------

The CI (.github/workflows/top-level.yml) builds the doc and pushes to the
``gihub-pages`` branch and is triggered on push to main and on pull request
(every time):

* On pull request, the build doc target is run, which builds the doc and stores it as an artifact.
* On push to main, the build doc and deploy targets are run, the latter commits the doc artifact to the gh-pages branch.

.. tip::

   You can see the runs at github.com/<your_user>/documentation/actions.

Enable GitHub Pages to have the public website
configure GitHub Pages at *github.com/<your_user>/documentation/settings/pages*:

* Set Source as "deploy from branch"
* Set the branch as "gh-pages"

Resuming work at a later time
-----------------------------

:green:`Reactivate the virtual environment with:`

.. shell::

   ~/documentation
   $source ./venv/scripts/activate

Ensure the tools are up to data from time to time with:

.. shell::

   ~/documentation
   $(cd docs ; pip install -r requirements.txt --upgrade)

Edit, build, commit, push as usual.

Understanding git lfs
---------------------

Since git lfs is not that common in the wild, it may be tricky to get the hang
of it.

First of all, the basics:
lfs replaces binaries files with pointers, and stores the binaries outside the
git repository, in an external server.

When you do ``git clone/pull``, by default lfs will also download the binaries
at the "smudge" step.
You can change this behaviour by setting globally
``git lfs install --skip-smudge`` or temporally with ``GIT_LFS_SKIP_SMUDGE=1``
environment variable.

If during a clone or pull you obtain the error:

::

   Encountered n file(s) that should have been pointers

That simply means that someone pushed files to remote that should have been
pointers (defined in the *.gitattributes* file).
And to fix is simple:

.. shell::

   $git add --renormalize .
   $git commit -m "Convert binary files to pointers"
   $git push

And advise the committer to ensure he has git lfs enabled with
``git lfs install``.

