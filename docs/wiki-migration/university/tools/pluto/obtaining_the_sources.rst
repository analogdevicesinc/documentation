Obtaining the Build Sources
===========================

Building the PlutoSDR or M2k Firmware Image involves several components managed in individual source code repositories. However since these components are heavily interrelated the approach taken utilizes `Git-Submodules <https://git-scm.com/book/en/v2/Git-Tools-Submodules>`_.

Firmware image components (Submodules):

-  `Linux Kernel <https://github.com/analogdevicesinc/linux>`_
-  `FPGA HDL <https://github.com/analogdevicesinc/hdl>`_
-  `Buildroot User Space <https://github.com/analogdevicesinc/buildroot>`_
-  :git-u-boot-xlnx:`u-boot Bootloader <tree/pluto>`

Submodules allow you to keep a Git repository as a subdirectory of another, the main Git repository.

The main repositories can be found here:

-  `PlutoSDR-fw <https://github.com/analogdevicesinc/plutosdr-fw>`_
-  `M2k-fw <https://github.com/analogdevicesinc/m2k-fw>`_

Cloning the repository
----------------------

.. important::

   The --recursive flag here is important otherwise the submodules are not included. The sources and all the build objects require approx 6 GByte of free disk space.


PlutoSDR-fw
~~~~~~~~~~~

.. container:: box bggreen

   This specifies any shell prompt running on your Linux development host

   
   ::
   
      michael@HAL9000:~/devel$ git clone --recursive https:<nowiki>//</nowiki>github.com/analogdevicesinc/plutosdr-fw.git
   


M2k-fw
~~~~~~

.. container:: box bggreen

   This specifies any shell prompt running on your Linux development host

   
   ::
   
      michael@HAL9000:~/devel$ git clone --recursive https:<nowiki>//</nowiki>github.com/analogdevicesinc/m2k-fw.git
   


Updating your repository
------------------------

.. container:: box bggreen

   This specifies any shell prompt running on your Linux development host

   
   ::
   
      michael@HAL9000:~/devel/plutosdr-fw$ git pull --recurse-submodules
   

