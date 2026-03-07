How to build the Zynq boot image BOOT.BIN
=========================================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/user_guide/build_boot_bin.html\


| The boot image BOOT.BIN is built using the bootgen tool which requires several input files.
| Instructions on how to build the Xilinx Shell Archive (XSA) handover file can be found here:

-  `Building HDL <https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html>`_ projects

All further steps are lengthy explained on the `Xilinx Wiki Page <http://www.wiki.xilinx.com>`_

-  `Build u-boot <http://www.wiki.xilinx.com/Build+U-Boot>`_
-  `Build FSBL <http://www.wiki.xilinx.com/Build+FSBL>`_
-  `Build BOOT image <http://www.wiki.xilinx.com/Prepare+Boot+Image>`_

Use script to build BOOT.BIN
----------------------------

For ease of use, we provide a bash shell script which allows building BOOT.BIN from system_top.xsa and u-boot.elf

Download
~~~~~~~~

The script can be downloaded from here:

-  `build_boot_bin.sh <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/zynq_boot_bin/build_boot_bin.sh>`_

|

.. tip::

   \ **NOTE: After downloading the script you need to make it executable**

   | ``$ chmod +x build_boot_bin.sh``


Usage
~~~~~

::

   usage: build_boot_bin.sh system_top.xsa u-boot.elf [output-archive]

-  Path to ``system_top.xsa`` and ``u-boot.elf`` are required parameters
-  An optionally 3rd ``name`` parameter can be given to tar.gz the output directory (``name``.tar.gz)
-  Build output is located in a local directory named: output_boot_bin
-  This script requires Xilinx Vitis and bootgen in the PATH

   -  A simple way is to source vivado settings[32|64].sh:

::

   $ source /opt/Xilinx/Vivado/202x.x/settings64.sh

-  When using **cygwin**, you can add the following in the ~/.bashrc configuration file:

::

   export PATH=$PATH:/cygdrive/c/Xilinx/Vivado/202x.x/bin
   export PATH=$PATH:/cygdrive/c/Xilinx/Vitis/202x.x/bin

There is also a version of script that works in Windows Powershell: `build_boot_bin.ps1 <https://wiki.analog.com/https/raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/zynq_boot_bin/build_boot_bin.ps1>`_

|

.. tip::

   \ **NOTE: u-boot.elf**

   | For those who don't want to build u-boot themselves.
   | The **u-boot.elf** can be extracted from the project folder on the :doc:`SD Card image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`, **bootgen_sysfiles.tgz**
   

