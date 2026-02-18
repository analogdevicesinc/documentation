.. _pluto-m2k obtaining_the_sources:

Obtaining the Build Sources
===========================

Building the PlutoSDR or M2k Firmware Image involves several components managed
in individual source code repositories. However since these components are
heavily interrelated the approach taken utilizes
`Git-Submodules <https://git-scm.com/book/en/v2/Git-Tools-Submodules>`__.

Firmware image components (Submodules):

- :git-linux:`/`
- :git-hdl:`/`
- :git-buildroot:`buildroot <master:>`
- :git-u-boot-xlnx:`u-boot Bootloader <pluto:>`

Submodules allow you to keep a Git repository as a subdirectory of another, the
main Git repository.

The main repositories can be found here:

- :git-plutosdr-fw:`PlutoSDR-fw <master:>`
- :git-m2k-fw:`M2k-fw <master:>`

Cloning the repository
----------------------

.. important::

   The ``--recursive`` flag here is important otherwise the submodules are not
   included.
   The sources and all the build objects require approx 6 GByte of free disk space.

PlutoSDR-fw
~~~~~~~~~~~

.. shell::

   ~/devel
   $git clone --recursive https://github.com/analogdevicesinc/plutosdr-fw.git

M2k-fw
~~~~~~

.. shell::

   ~/devel
   $git clone --recursive https://github.com/analogdevicesinc/m2k-fw.git

Updating your repository
------------------------

.. shell::

   ~/devel/plutosdr-fw
   $git pull --recurse-submodules
