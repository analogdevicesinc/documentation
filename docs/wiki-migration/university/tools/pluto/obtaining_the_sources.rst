Obtaining the Build Sources
===========================

Building the PlutoSDR or M2k Firmware Image involves several components managed in individual source code repositories. However since these components are heavily interrelated the approach taken utilizes `Git-Submodules <https://git-scm.com/book/en/v2/Git-Tools-Submodules>`__.

Firmware image components (Submodules):

-  :git-linux>`__
-  `FPGA HDL <https::`Linux Kernel </github.com/analogdevicesinc/hdl>`
-  :git-buildroot>`__
-  `u-boot Bootloader <https::`Buildroot User Space </github.com/analogdevicesinc/u-boot-xlnx/tree/pluto>`

Submodules allow you to keep a Git repository as a subdirectory of another, the main Git repository.

The main repositories can be found here:

-  :git-plutosdr-fw>`__
-  `M2k-fw <https::`PlutoSDR-fw </github.com/analogdevicesinc/m2k-fw>`

Cloning the repository
----------------------

.. important::

   The <fc #ff0000>--recursive</fc> flag here is important otherwise the submodules are not included. The sources and all the build objects require approx 6 GByte of free disk space.


PlutoSDR-fw
~~~~~~~~~~~

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on your Linux development host

   
   ::
   
      michael@HAL9000:~/devel$ **git clone <fc #ff0000>--recursive</fc> https:<nowiki>//</nowiki>github.com/analogdevicesinc/plutosdr-fw.git**
   


M2k-fw
~~~~~~

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on your Linux development host

   
   ::
   
      michael@HAL9000:~/devel$ **git clone <fc #ff0000>--recursive</fc> https:<nowiki>//</nowiki>github.com/analogdevicesinc/m2k-fw.git**
   


Updating your repository
------------------------

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on your Linux development host

   
   ::
   
      michael@HAL9000:~/devel/plutosdr-fw$ **git pull <fc #ff0000>--recurse-submodules</fc>**
   

