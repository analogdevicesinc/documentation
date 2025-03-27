.. _forking-publishing:

Forking and publishing
======================

The steps below are a walk-through to contribute to
:git-documentation:`this </>` repository,
It ensures that GitHub Actions and GitHub Pages are enabled, so you can run
continuous integration and see the pages live at *<your_user>.github.io/documentation*,
and `git-lfs <https://git-lfs.com/>`__ artifacts are properly synced.
To learn about git lfs and use it as a pro, read :ref:`git-lfs`.

.. note::

   Using the Python virtual environment (venv) is recommended, but if you wish
   to not use it, skip steps in :green:`green`.

Preparing your origin
---------------------

There is three options to contribute:

* :ref:`forking-publishing branch`: with write access to *analogdevicesinc* organization (recommended).
* :ref:`forking-publishing fork`: that want to use the GitHub flow.
* :ref:`forking-publishing copy`: that want to work privately first.

.. tip::

   If using Github Codespaces, just fork/create a branch/copy and follow
   :ref:`this section <forking-publishing github-codespaces>`.

.. _forking-publishing branch:

Branch
~~~~~~

If you have write permission to the repository, you shall add your work to a
branch at mainland, then just:

Ensure git-lfs is installed with:

.. code:: bash

   sudo apt install git-lfs -y

Initialize it with skip-smudge during clone, so we can fetch on demand later:

.. code:: shell

   git lfs install --skip-smudge

Clone the repository

.. shell::

   $git clone https://github.com/analogdevicesinc/documentation \
   $    --origin public \
   $    --depth 10 \
   $    -- documentation
   $cd documentation

Create and checkout a branch

.. shell::

   ~/documentation
   $git checkout -b <your_branch>

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

Initialize it with skip-smudge during clone, so we can fetch on demand later:

.. code:: shell

   git lfs install --skip-smudge

Clone the repository:

.. shell::

   $git clone https://github.com/<your_user>/documentation \
   $    --origin public \
   $    --depth 10 -- documentation
   $cd documentation


Fetch the large files from *analogdevicesinc* that your are working on and push
to your copy the large files binaries (and vice-versa):

.. shell::

   ~/documentation
   $git lfs pull public -I file_basename
   $git lfs push private --all

If you don't have write permission to *analogdevicesinc*, you won't be able
to push to it, but a reviewer can do in your behalf during review.

.. _forking-publishing copy:

Copy
~~~~

Ensure git-lfs is installed with:

.. code:: bash

   sudo apt install git-lfs -y

Initialize it with skip-smudge during clone, so we can fetch on demand later:

.. code:: shell

   git lfs install --skip-smudge

Clone mainland:

.. shell::

   $git clone https://github.com/analogdevicesinc/documentation \
   $    --origin public \
   $    --depth 10 -- documentation
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

Fetch the large files from *analogdevicesinc* that your are working on and push
to your copy the large files binaries (and vice-versa):

.. shell::

   ~/documentation
   $git lfs pull public -I file_basename
   $git lfs push private --all

If you don't have write permission to *analogdevicesinc*, you won't be able
to push to it, but a reviewer can do in your behalf during review.

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

Launch the doc editing server using :external+doctools:ref:`serve`:

.. shell::

   ~/documentation
   $(cd docs ; adoc serve)

The server will fetch on demand the git lfs resource (smudge step) from the
pages you visit on the local server, and watched files you touch.

Alternatively, you can build it once calling Sphinx directly, but if the git lfs
smudge step was skipped, the images and other binary files will be missing.

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
documentation, including the live preview daemon :external+doctools:ref:`serve`,
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

.. _git-lfs:

Conquer git lfs
---------------

Since git lfs is not that common in the wild, it may be tricky to get the hang
of it.

First of all, the basics:
lfs replaces binaries files with pointers, and stores the binaries outside the
git repository, in an external server.

When you do ``git clone/pull``, by default lfs will also download the binaries
at the "smudge" step.
But we **highly** recommend to change this behaviour to fetch the artifacts on
demand by setting globally ``git lfs install --skip-smudge`` or temporally with
``GIT_LFS_SKIP_SMUDGE=1`` environment variable.
It is recommended because it saves a lot of bandwidth and (your precious) time.

In this configuration, you can fetch the artifact:

.. shell::

   ~/documentation
   $git lfs pull -I path/to/my_file.png
   # Checking size
   $ls -l path/to/my_file.png
    -rw-r--r-- 1 me me 34162787 Mar 25 11:09 path/to/my_file.png


And revert to it's pointer state:

.. shell::

   ~/documentation
   $rm path/to/my_file.png ; git restore -- $_
   # Checking pointer
   $cat path/to/my_file.png
    version https://git-lfs.github.com/spec/v1
    oid sha256:837ad06a63c0b1c10a02615601f73b7b7596746a62064fe35bb8a4d1543f04a2
    size 34162787

For documentation, you don't need to do it manually, :external+doctools:ref:`serve`
will automatically fetch lfs artifacts of watched touched files and visited pages
on the live server.

In the following subsections are common issues and on what to do in each situation.

.. _files-pointers:

Files that should have been pointers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Git lfs simply follows the rules on the :git-documentation:`.gitattributes` file.
And some times you may encounter during clone and pull:

.. shell::
   :no-path:

   $git pull
    Encountered <n> file(s) that should have been pointers

That simply means that someone pushed files to remote that should have been
pointers (defined in the *.gitattributes* file).
And to fix is simple:

.. shell::

   $git add --renormalize .
   $git commit -m "lfs: convert binary files to pointers" --signoff
   $git push

Then, advise the committer to ensure he has git lfs enabled with
``git lfs install`` and to read this page.

Checking out branches and commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Git lfs simply follows the rules on the :git-documentation:`.gitattributes` file.
And some times you may encounter during checkout:

.. shell::
   :no-path:

   $git checkout other_branch -f
    error: Your local changes to the following files would be overwritten by checkout:
            path/to/file/that_should_be_a_pointer.pptx
    Please commit your changes or stash them before you switch branches.
    Aborting

It is the same cause as :ref:`previously <files-pointers>`.
If you don't care about this file at the moment, just ``--force`` your way out.

.. shell::
   :no-path:

   $git checkout other_branch -f

Pull request permission
~~~~~~~~~~~~~~~~~~~~~~~

When a user opens a pull request, he temporally grants you write permission for their
remove branch for commits, but not for git lfs storage, so pushing lfs artifacts to
their remote will cause:

.. shell::
   :no-path:

   $git push contributor
    error: Authentication error: Authentication required: You must have push access to verify locks
    error: failed to push some refs to 'https://github.com/<contributor>/documentation.git'

   $git push contributor --no-verify
    Writing objects: 100% (8/8), 1.08 KiB | 1.08 MiB/s, done.
    Total 8 (delta 6), reused 0 (delta 0), pack-reused 0 (from 0)
    remote: Resolving deltas: 100% (6/6), completed with 6 local objects.
    remote: error: GH008: Your push referenced at least 1 unknown Git LFS object:
    remote:     9b439f0ad3b1e8e965955487b72e84045e85fb844392890c7d34ba45b3430c1e
    remote: Try to push them with 'git lfs push --all'.
    To https://github.com/<contributor>/documentation.git

As a reviewer, this may get on the way and there is no particular fix for that beyond not pushing
commits with new lfs artifacts, or awkwardly asking contributor permissions to their repository.

If you want to add new lfs artifacts, as a reviewer, just merge the PR, and commit to main.
If it is a complex PR, you can push to a new branch, and work from there and once you and the
contributor are ratified, close the original PR without merging, merging the branch on the main
remote instead.

