.. warning::

   These pages are not updated anymore. Documentation has been moved to :git-lnxdsp-adi-meta:`wiki\`


Branching Policy
================

We use a branching policy similar to our internal branching policy. This allows us to easily export internal development to the public repositories that we provide.

-  All ADI development is based off a main control branch that ADI maintains. This branch is always in a stable state and will contain the latest release. For repositories that ADI owns (MCAPI, scripts, examples, repo manifest) this will be the **master** branch. For open source repositories maintained by other parties, we use an **adi-master** branch. This allows us to do our development without interfering with anything from upstream.
-  All development for a release will be performed on a **development** branch whose name is off the format develop/yocto-<version>. Development branches are created from the main control branch at the start of development. The release branch will be branched from the development branch close to release.
-  Release branches are created for a product release. They may be created before the actual release in order for release candidates to be created. When a formal release occurs the release branches will be merged back to the main control branch.
-  Release branches may be updated after release with any critical hotfixes. Hotfixes will be small bugfixes that do not change the functionality of the release. If a bug requires a major fix, the product will be re-released with a new version.
-  Examples, demos, new features may be released on feature branches. These will branch from a specific release, or development branch. They will be fully self-contained.
