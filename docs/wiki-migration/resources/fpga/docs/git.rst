HDL Git Repository
==================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated. Please check out our latest guide at https://analogdevicesinc.github.io/hdl/user_guide/git_repository.html\


All the HDL sources can be found in the following git repository:

https://github.com/analogdevicesinc/hdl

We assume that the user is familiar with `git <https://git-scm.com/>`_. Knows how to `clone <https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>`_ the repository, how to check its `status <https://git-scm.com/docs/git-status>`_ or how to `switch <https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>`_ between branches.

.. tip::

   A basic git knowledge is required in order to work with these source files, if you do not have any, don't worry! There are a lot of great resources and tutorials about git all over the `web <http://lmgtfy.com/?q=git+tutorial>`_.


If you want to pull down the sources as soon as possible, just do the following few steps:

-  Install Git from `here <https://git-scm.com/>`_
-  Open up Git bash, change your current directory to a place where you want to keep the hdl source
-  Clone the repository using `these <https://help.github.com/articles/cloning-a-repository/>`_ instructions

Folder structure
----------------

The root of the HDL repository has the following structure:

<block 60%>

::

   .
   ├─ .github
   ├─ docs
   ├─ projects
   ├─ library
   ├─ .gitattributes
   ├─ .gitignore
   ├─ LICENSE
   ├─ Makefile
   └─ README.md

</block>

The repository is divided into two separate sections:

-  **projects** with all the currently supported projects
-  **library** with all the Analog Devices Inc. proprietary IP cores and hdl modules, which are required to build the projects

The file **.gitattributes** is used to properly `handle different <https://help.github.com/articles/dealing-with-line-endings/>`_ line endings. And the **.gitignore** specifies intentionally untracked files that Git should ignore. The root **Makefile** can be used to build all the project of the repository. To learn more about hdl **Makefiles** visit the :doc:`Building & Generating programming files </wiki-migration/resources/fpga/docs/build>` section.

The projects are structured as following
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<block 60%>

::

   .
   ├─ projects
   │    ├ ad6676evb
   │    ├ ad9467_fmc
   │    ·
   │    ├ common
   │    ├ fmcomms2
   │    │   ├ ac701
   │    │   ├ common
   │    │   ├ kc705
   │    │   ·
   │    │   ├ zed
   │    │   └ Makefile
   │    ├ adrv9009
   │    ├ scripts
   │    ·
   │    └ Makefile
   └─ library
   ·
   └─ README.md

</block>

Besides the project folders, there are two special folders inside the **/hdl/projects**:

-  **common**: This folder contains all the base designs, for all currently supported FPGA development boards. Be aware if you see your board on this list, it does not necessarily mean that you can use it with your FMC board.
-  **scripts**: In all cases, we are interacting with the development tools (Vivado/Quartus) using Tcl scripts. In this folder are defined all the custom Tcl processes, which are used to create a project, define the system and generate programming files for the FPGA.

Inside a project folder, you can find folders with an FPGA carrier name (e.g. ZC706) which in general contains all the carrier board specific files, and a folder called **common** which contains the project specific files. If you can not find your FPGA board name in a project folder, that means your FPGA board with that particular FMC board is not supported.

The library are structured as following
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<block 60%>

::

   .
   ├─ projects
   ├─ library
   │   ├─ axi_ad6676
   │   ├─ axi_ad9122
   │   ├─ axi_ad9144
   │   ·
   │   ├─ common
   │   ├─ interfaces
   │   ├─ scripts
   │   ├─ util_pack
   │   ·
   │   └ Makefile
   ·
   └─ README.md

</block>

The library folder contains all the IP cores and common modules. An IP, in general, contains Verilog files, which describe the hardware logic, constraint files, to ease timing closure, and Tcl scripts, which generate all the other files required for IP integration (\*_ip.tcl for Vivado and \*_hw.tcl for Quartus) .

.. tip::

   Regarding Vivado, all the IPs must be 'packed' before being used in a design. To find more information about how to build the libraries please visit the :doc:`Building & Generating programming files </wiki-migration/resources/fpga/docs/build>` section.


Repository Releases and Branches
--------------------------------

The repository may contain multiple branches and tags. The :git-hdl:`tree/master` branch is the development branch (latest sources, but not stable). If you check out this branch, some builds may fail. If you are not into any kind of experimentation, you should only check out one of the release branch.

All our release branches have the following naming convention: **hdl\_**\ [year_of_release]\ **\_r**\ [1 or 2]. (e.g. :git-hdl:`tree/hdl_2014_r2`)

ADI does two releases each year when all the projects get an update to support the latest tools and get additional new features. \*\* The master branch is always synchronized with the latest release.*\* If you are in doubt, ask us on :ez:`FPGA Engineer Zone <community/fpga>`.

.. tip::

   You can find the release notes on the Github page of the repository:

   
   -  :git-hdl:`releases`
   


Need help?
----------

-  :ez:`FPGA Reference Designs support forum <community/fpga>`

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#intro
   :alt: Introduction#hdl|Main page#releases|Releases and supported tool versions
