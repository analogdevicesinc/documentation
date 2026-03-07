How to build the ZynqMP boot image BOOT.BIN
===========================================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/user_guide/build_boot_bin.html\


| The boot image BOOT.BIN is build using the bootgen tool which requires several input files.
| Instructions on how to build the Xilinx Shell Archive (XSA) handover file can be found here:

-  `Building HDL <https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html>`_ projects

All further steps are lengthy explained on the `Xilinx Wiki Page <http://www.wiki.xilinx.com>`_

-  `Build u-boot <http://www.wiki.xilinx.com/Build+U-Boot>`_

   -  Make sure you checkout the proper git tag matching your Vivado Version (xilinx-v2022.2, xilinx-v2021.2, ...)

-  `Build FSBL <http://www.wiki.xilinx.com/Build+FSBL>`_
-  `Build PMU Firmware <http://www.wiki.xilinx.com/Build+PMU+Firmware>`_
-  `Build Arm Trusted Firmware (ATF) <http://www.wiki.xilinx.com/Build+Arm+Trusted+Firmware+%28ATF%29>`_
-  `Build BOOT image <http://www.wiki.xilinx.com/Prepare+Boot+Image>`_

Use script to build BOOT.BIN
----------------------------

For ease of use we provide a bash shell script which allows building BOOT.BIN from system_top.xsa, u-boot.elf and either bl31.elf or a path to the Arm Trusted Firmware repository

Download
~~~~~~~~

The script can be downloaded from here:

-  `build_zynqmp_boot_bin.sh <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/zynqmp_boot_bin/build_zynqmp_boot_bin.sh>`_

|

.. tip::

   \ **NOTE: After downloading the script you need to make it executable**

   | ``$ chmod +x build_zynqmp_boot_bin.sh``


Usage
~~~~~

::

   usage: build_zynqmp_boot_bin.sh system_top.xsa u-boot.elf (download | bl31.elf | <path-to-arm-trusted-firmware-source>) [output-archive]

-  Make sure that Vivado and Vitis is included in the path and a cross compiler for arm64 exists before running the script. For more information about cross compilers, see :doc:`Building the ZynqMP / MPSoC Linux kernel and devicetrees from source </wiki-migration/resources/tools-software/linux-build/generic/zynqmp>`.
-  Path to ``system_top.xsa`` and ``u-boot.elf`` are required parameters.

   -  To find ``system_top.xsa``, see `Building HDL <https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html>`_. After building a project in the HDL repository, it can be found inside a **<project>\_<board>.sdk** folder.
   -  See the note at the bottom of the page regarding ``u-boot.elf``.

-  The 3rd argument must either be ``download`` (which will git clone the ATF repository), ``bl31.elf`` or the file system ``path`` to the Arm Trusted Firmware source code repository

   -  See the note at the bottom of the page regarding ``bl31.elf``.

-  An optionally 4th ``name`` parameter can be given to tar.gz the output directory. (``name``.tar.gz)
-  **BOOT.BIN** and other build output files are located at the newly created local directory named: output_boot_bin.
-  This script requires Xilinx Vitis and bootgen in the PATH.
   \* A simple way is to source Vivado settings[32|64].sh for Linux:

::

   $ source /opt/Xilinx/Vivado/202x.x/settings64.sh

-  When using **cygwin**, you can add the following in the ~/.bashrc configuration file:

::

   export PATH=$PATH:/cygdrive/c/Xilinx/Vivado/202x.x/bin
   export PATH=$PATH:/cygdrive/c/Xilinx/Vitis/202x.x/bin
   export PATH=$PATH:/cygdrive/c/Xilinx/Vitis/202x.x/gnu/microblaze/nt/bin

|

.. tip::

   \ **NOTE: u-boot.elf and bl31.elf**

   | For those who don't want to build u-boot or bl31 themselves.
   | Both **u-boot.elf** and **bl31.elf** can be extracted from the project folder on the :doc:`SD Card image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`, **bootgen_sysfiles.tgz**.
   
   **u-boot.elf** may have a different name, rename that .elf file to u-boot.elf before using.
   

