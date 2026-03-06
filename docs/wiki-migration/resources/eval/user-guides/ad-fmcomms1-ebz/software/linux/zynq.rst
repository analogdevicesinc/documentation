Linux with HDMI video output on the ZED, ZC702 and ZC706 boards
===============================================================

Supported devices
-----------------

-  :adi:`ADV7511`
-  :adi:`FMCOMMS-1 <ad-fmcomms1-ebz>`
-  :adi:`FMCOMMS-2 <ad-fmcomms2-ebz>`
-  :adi:`FMCOMMS-3 <ad-fmcomms3-ebz>`
-  :adi:`FMCOMMS-4 <ad-fmcomms4-ebz>`
-  :adi:`FMCOMMS-5 <ad-fmcomms5-ebz>` (ZC702, ZC706 only)
-  :adi:`ad-fmcadc2-ebz` (ZC706 only)
-  :adi:`ad-fmcdaq2-ebz` (ZC706 only)
-  :adi:`EVAL-FMCDAQ3-EBZ` (ZC706 only)
-  :adi:`ad-fmcjesdadc1-ebz` (ZC706 only)

Supported carriers
------------------

-  `ZC702 <https://www.xilinx.com/ZC702>`__
-  `ZC706 <https://www.xilinx.com/ZC706>`__
-  `Zed Board <http://zedboard.org/content/overview>`__ (not for :adi:`FMCOMMS-5 <ad-fmcomms5-ebz>`)

Overview
--------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/adv7511.png
   :align: center
   :width: 400px

Preparing the SD-card
---------------------

To boot the system on the ZED, ZC702 or ZC706 board you'll need a SD memory card. The SD card should have at least 4 GB of storage and it is recommended to use a card with speed-grade 6 or higher to achieve optimal file transfer performance.

The SD card needs to be partitioned with two partitions. The first one should be about 40MB in size and the second one should take up the remaining space. For optimal performance make sure that the partitions are 4MB aligned. The first partition needs to be formatted with a FAT filesystem. It will hold the bootloader, devicetree and kernel images. The second partition needs to be formatted with a ext4 filesystem. It will store the systems root filesystem.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/linux-zynq-gparted-sdcard.png
   :align: center
   :width: 600px

Obtain the HDL reference design
-------------------------------

The ZYNQ does not have a on-chip graphics or audio core, instead the FPGA is used to generate the necessary signals to deliver the video and audio streams to the ADV7511. Analog Devices provides a reference HDL design which contain support for generating the necessary video and audio as well as support for interfacing with the AD-FMCOMMS1-EBZ.

The HDL reference designs can be downloaded from their respective wiki page:

-  :doc:`ADV7511 XILINX KC705, VC707, ZC702 AND ZED REFERENCE DESIGN </wiki-migration/resources/fpga/xilinx/kc705/adv7511>`
-  :doc:`AD-FMCOMMS1-EBZ REFERENCE DESIGN </wiki-migration/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz>`
-  :doc:`AD-FMCOMMS2-EBZ DESIGN </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>`

.. hint::

   The AD-FMCOMMS1-EBZ reference designs for the ZED, ZC702 and ZC706 include support for the ADV7511. So you only need one of the reference designs depending on whether you want support for the AD-FMCOMMS1-EBZ or not.


You can either use the provided reference designs to build your own system.bit or use a pre-build system.bit file. The system.bit will be required in the next step.

Build the boot image
--------------------

To complete this step you need to have a u-boot image for the Zynq platform. Please refer to the `Xilinx wiki <https://xilinx-wiki.atlassian.net/wiki/spaces/A/overview>`__ on how to build such an image.

The bootloader can be build with Xilinx SDK. In order to do so it is necessary to first export the HDL design from the Xilinx Platform Studio to the SDK, this is done by clicking the "Export to SDK" button in the Platform Studio GUI.

Export project to SDK:


|image1|

Once the project has been exported create a new FSBL project in the SDK. To do this right-click on the newly exported hardware platform specification in left "Project Explorer" panel and select "New > Project" from the popup menu. Select "Xilinx - Application Project" on first dialog page. On the second dialog page choose a name for the project (zynq_fsbl for example) and on the third page select "Zynq FSBL" template.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/linux-zynq-xsdk-fsbl1.png
   :alt: linux-zynq-xsdk-fsbl1.png
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/linux-zynq-xsdk-fsbl2.png
   :alt: linux-zynq-xsdk-fsbl2.png
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/linux-zynq-xsdk-fsbl3.png
   :alt: linux-zynq-xsdk-fsbl3.png
   :align: center
   :width: 400px

The project should build automatically. If not a manual build can be started by right clicking the newly created project in the left "Project Explorer" panel and selecting "Build Project" from the popup menu. After the project has been build it is time to generate the boot image. This is done by right clicking on the project in the left "Project Explorer" pane and selecting "Create Boot Image". This will open up the bootgen wizard. The bootgen wizard needs three files:

-  The freshly build zynq_fsbl.elf binary
-  The system.bit bitstream
-  The u-boot.elf binary

Add these files to partitions list in the dialog, then select an output folder.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/linux-zynq-bootgen.png
   :align: center
   :width: 400px

Clicking "Create Image" will now generate in the chosen location a new boot image for the target platform. The output \*.bin file should be named "BOOT.BIN" and needs to be saved on the first partition of the SD-card.

Alternative method of building the Zynq boot image
--------------------------------------------------

| {The boot image BOOT.BIN is build using the bootgen tool which requires several input files.
| Instructions on how to build the Hardware Description File (HDF) handover file can be found here:

-  `Building HDL <resources/fpga/docs/build>`__

All further steps are lengthy explained on the `Xilinx Wiki Page <http://www.wiki.xilinx.com>`__

-  `Build u-boot <http://www.wiki.xilinx.com/Build+U-Boot>`__

::

      * Make sure you checkout the proper git tag matching your Vivado Version (xilinx-v2018.2, xilinx-v2017.4, ...)
   * [[http://www.wiki.xilinx.com/Build+FSBL|Build FSBL]]
   * [[http://www.wiki.xilinx.com/Build+PMU+Firmware|Build PMU Frimware]]
   * [[http://www.wiki.xilinx.com/Build+Arm+Trusted+Firmware+%28ATF%29|Build Arm Trusted Firmware (ATF)]]
   * [[http://www.wiki.xilinx.com/Prepare+Boot+Image|Build BOOT image]]

Use script to build BOOT.BIN
----------------------------

For ease of use we provide a bash shell script which allows building BOOT.BIN from system_top.hdf, u-boot.elf and either bl31.elf or a path to the Arm Trusted Firmware repository

Download
~~~~~~~~

The script can be downloaded from here:

-  `build_zynqmp_boot_bin.sh <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/zynqmp_boot_bin/build_zynqmp_boot_bin.sh>`__

|

.. tip::

   \ **NOTE: After downloading the script you need to make it executable**

   | ``$ chmod +x build_zynqmp_boot_bin.sh``


Usage
~~~~~

::

   usage: build_zynqmp_boot_bin.sh system_top.xsa u-boot.elf (download | bl31.elf | <path-to-arm-trusted-firmware-source>) [output-archive]

-  Path to ``system_top.xsa`` and ``u-boot.elf`` are required parameters.
-  The 3rd argument must either be ``download`` (which will git clone the ATF repository), ``bl31.elf`` or the file system ``path`` to the Arm Trusted Firmware source code repository
-  An optionally 4th ``name`` parameter can be given to tar.gz the output directory. (``name``.tar.gz)
-  Build output is located in a local directory named: output_boot_bin.
-  This script requires Xilinx Vitis and bootgen in the PATH.
   \* A simple way is to source vivado settings[32|64].sh for Linux:

::

   $ source /opt/Xilinx/Vivado/202x.x/settings64.sh

::

     * When using **cygwin**, you can add the following in the ~/.bashrc configuration file:

::

   export PATH=$PATH:/cygdrive/c/Xilinx/Vivado/202x.x/bin
   export PATH=$PATH:/cygdrive/c/Xilinx/Vitis/202x.x/bin
   export PATH=$PATH:/cygdrive/c/Xilinx/Vitis/202x.x/gnu/microblaze/nt/bin

|

.. tip::

   \ **NOTE: u-boot.elf**

   | For those who don't want to build u-boot themselves.
   | The **u-boot.elf** can be extracted from the project folder on the :doc:`SD Card image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`, **bootgen_sysfiles.tgz**
   


Build and install the kernel image
----------------------------------

.. note::

   The prerequistes for following these instructions are to have:

   
   -  mkimage from your distribution (normally ``apt-get install u-boot-tools``)
   -  C compiler from the Xilinx SDK
   


.. admonition:: Download
   :class: download

   The most stable kernel source tree containing support for the ZED, ZC702 and ZC706 plus **AD-FMCOMMS1-EBZ** can be found at :git-linux:`tree/2016_R1`. For the **AD-FMCOMMS2-EBZ** use also the :git-linux:`tree/2016_R1` branch.


.. container:: box bggreen

   
   .. note::

      root Download and build the kernel image

   
   ::
   
      > **git clone https:%%//%%github.com/analogdevicesinc/linux.git**
      Cloning into 'linux'...
      remote: Counting objects: 2550298, done.
      remote: Compressing objects: 100% (466978/466978), done.
      remote: Total 2550298 (delta 2118600), reused 2483072 (delta 2058083)
      Receiving objects: 100% (2550298/2550298), 727.70 MiB | 353 KiB/s, done.
      Resolving deltas: 100% (2118600/2118600), done.
      Checking out files: 100% (38170/38170), done.
      > **cd linux**
      > # For AD-FMCOMMS2-EBZ use
      > # **git checkout master **
      > **export ARCH=arm**
      > **export CROSS_COMPILE=/path/to/your/arm/cross-compiler**
      > # e.g. export CROSS_COMPILE=/opt/CodeSourcery/Sourcery_G++_Lite/bin/arm-xilinxa9-linux-gnueabi-
      > **make zynq_xcomm_adv7511_defconfig**
      #
      # configuration written to .config
      #
      > **make uImage LOADADDR=0x00008000**
        ...
        OBJCOPY arch/arm/boot/uImage
        Kernel: arch/arm/boot/uImage is ready
   


.. note::

   The same kernel image is used for all HDL reference design.


The next step is to build the devicetree for your target platform. While the kernel is the same for all target boards the devicetree file differs as it describes the board specifics.

The following devicetree files are available:

+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc702-adv7511.dts                         | `ZC702 <https://www.xilinx.com/ZC702>`__ and the on-board :adi:`ADV7511`                                                                                                                                                                                                        |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc702-adv7511-ad9361-fmcomms2-3.dts       | `ZC702 <https://www.xilinx.com/ZC702>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board                  |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc702-adv7511-ad9361-fmcomms5.dts         | `ZC702 <https://www.xilinx.com/ZC702>`__, the on-board :adi:`ADV7511` and the AD-FMCOMMS5-EBZ                                                                                                                                                                                   |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc702-adv7511-ad9364-fmcomms4.dts         | `ZC702 <https://www.xilinx.com/ZC702>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` board                                                                                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc702-adv7511-fmcomms1.dts                | `ZC702 <https://www.xilinx.com/ZC702>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz>` board                                                                                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511.dts                         | `ZC706 <https://www.xilinx.com/ZC706>`__ and the on-board :adi:`ADV7511`                                                                                                                                                                                                        |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad6676-fmc.dts              | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the AD6676-FMC-EBZ board                                                                                                                                                                              |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9265-fmc-125ebz.dts       | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the :doc:`AD9265-FMC-125EBZ </wiki-migration/resources/fpga/xilinx/fmc/ad9265>` board                                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9361-fmcomms2-3.dts       | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board                  |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9361-fmcomms2-3-pr.dts    | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board                  |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9361-fmcomms5.dts         | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the AD-FMCOMMS5-EBZ board                                                                                                                                                                             |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9364-fmcomms4.dts         | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` board                                                                                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9434-fmc-500ebz.dts       | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the :doc:`AD9434-FMC-500EBZ </wiki-migration/resources/fpga/xilinx/fmc/ad9434>` board                                                                                                                 |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-ad9625-fmcadc2.dts          | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCADC2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcadc2-ebz>` board                                                                                                           |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-fmcadc4.dts                 | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the `AD-FMCADC4-EBZ <resources/eval/user-guides/ad-fmcadc4-ebz>`__ board                                                                                                                              |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-fmcdaq1.dts                 | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the AD-FMCDAQ1-EBZ board                                                                                                                                                                              |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-fmcdaq2.dts                 | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCDAQ2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz>` board                                                                                                           |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-fmcjesdadc1.dts             | `ZC706 <https://www.xilinx.com/ZC706>`__, the the on-board :adi:`ADV7511` and the :doc:`AD-FMCJESDADC1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcjesdadc1-ebz>` board                                                                                               |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-fmcomms1.dts                | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz>` board                                                                                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zc706-adv7511-fmcomms6.dts                | `ZC706 <https://www.xilinx.com/ZC706>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS6-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms6-ebz>` board                                                                                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511.dts                           | `Zed Board <http://zedboard.org/product/zedboard>`__ and the on-board :adi:`ADV7511`                                                                                                                                                                                            |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511-ad9361-fmcomms2-3.dts         | `Zed Board <http://zedboard.org/product/zedboard>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board      |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511-ad9364-fmcomms4.dts           | `Zed Board <http://zedboard.org/product/zedboard>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` board                                                                                             |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511-ad9467-fmc-250ebz.dts         | `Zed Board <http://zedboard.org/product/zedboard>`__, the on-board :adi:`ADV7511` and the `AD9467-FMC-250EBZ <resources/fpga/xilinx/fmc/ad9467>`__ board                                                                                                                        |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511-fmcmotcon1.dts                | `Zed Board <http://zedboard.org/product/zedboard>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCMOTCON1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz>` board                                                                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511-fmcmotcon2.dts                | `Zed Board <http://zedboard.org/product/zedboard>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCMOTCON2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcmotcon2-ebz>` board                                                                                         |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-zed-adv7511-fmcomms1.dts                  | `Zed Board <http://zedboard.org/product/zedboard>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz>` board                                                                                             |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-mini-itx-adv7511.dts                      | `Mini-ITX <http://zedboard.org/product/mini-itx-board>`__ and the on-board :adi:`ADV7511`                                                                                                                                                                                       |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-mini-itx-adv7511-ad9361-fmcomms2-3.dts    | `Mini-ITX <http://zedboard.org/product/mini-itx-board>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-mini-itx-adv7511-ad9361-fmcomms2-3-pr.dts | `Mini-ITX <http://zedboard.org/product/mini-itx-board>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynq-mini-itx-adv7511-ad9364-fmcomms4.dts      | `Mini-ITX <http://zedboard.org/product/mini-itx-board>`__, the on-board :adi:`ADV7511` and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` board                                                                                        |
+------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. important::

   The devicetree must match the HDL reference design that is used. It is not possible to use a adv7511 only devicetree for a AD-FMCOMMS1-EBZ reference HDL design, even if the AD-FMCOMMS1-EBZ is not connected to the FMC slot.


To build the devicetree from the devicetree file run \`make name-dts-replaced-by-dtb\`

.. container:: box bggreen

   
   .. note::

      Build the devicetree for ZED with HDMI video out and XCOMM

   
   ::
   
      > **make zynq-zed-adv7511-xcomm.dtb**
        DTC     arch/arm/boot/zynq-zed-adv7511-xcomm.dtb
      DTC: dts->dtb  on file "arch/arm/boot/dts/zynq-zed-adv7511-xcomm.dts"
   


The last step is to copy both the kernel and the devicetree files to the first partition of the SD card. It is important to rename the devicetree file to devicetree.dtb

.. container:: box bggreen

   
   .. note::

      Copy kernel and device tree to SD card

   
   ::
   
      > **cp arch/arm/boot/uImage /media/BOOT/uImage**
      > **cp arch/arm/boot/zynq-zed-adv7511-xcomm.dtb /media/BOOT/devicetree.dtb**
   


uEnv.txt
--------

The default environment that is used by the u-boot bootloader instructions the kernel to use a ramfs disk for its root filesystem. In order to boot from the SD card it is necessary to overwrite the default environment. This can be done by placing a file called uEnv.txt in the BOOT partition of the SD card. This file will be read by u-boot and is used to replace the default environment.

**uEnv.txt for using SD card rootfs**

::

   uenvcmd=run adi_sdboot
   adi_sdboot=echo Copying Linux from SD to RAM... && fatload mmc 0 0x3000000 ${kernel_image} && fatload mmc 0 0x2A00000 ${devicetree_image} && if fatload mmc 0 0x2000000 ${ramdisk_image}; then bootm 0x3000000 0x2000000 0x2A00000; else bootm 0x3000000 - 0x2A00000; fi
   bootargs=console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlyprintk rootfstype=ext4 rootwait

Install the root file system
----------------------------

In this example we will use a `Linaro Ubuntu ARM <http://linaro.org>`__ rootfs as it provides a good out of the box experience. The latest version can be found on the `Linaro Download page <http://www.linaro.org/downloads/>`__. In this example we will use the 12.11 release.

The first step is to download the `archive containing the root filesystem <https://releases.linaro.org/archive/12.12/ubuntu/vexpress/linaro-precise-ubuntu-desktop-20121124-560.tar.gz>`__.

.. container:: box bggreen

   
   .. note::

      Download Linaro Ubuntu ARM rootfs

   
   ::
   
      > **wget http:%%//%%releases.linaro.org/archive/12.12/ubuntu/vexpress/linaro-precise-ubuntu-desktop-20121124-560.tar.gz**
   


The next step is to extract the root filesystem from the archive to the SD card. It is important to preserve the file permission and owner settings, otherwise the system will be unable to boot. Since some of the files have root permissions it is necessary to run the extraction process as root.

.. container:: box bggreen

   
   .. note::

      Extract the root filesystem onto the SD card

   
   ::
   
      > **sudo tar --strip-components=3 -C /media/rootfs -xzpf linaro-precise-ubuntu-desktop-20121124-560.tar.gz binary/boot/filesystem.dir**
      > **ls /media/rootfs/**
      bin/  boot/  dev/  etc/  home/  lib/  lost+found/  media/  mnt/ opt/
      proc/  root/  run/  sbin/  selinux/  srv/  sys/  tmp/  usr/  var/
   


Testing the system
------------------

Once all of the previous tasks have been completed it is time to test the system. To do this insert the SD-card into the board and power-up the board. After a few seconds the blue "DONE" LED should light up. This means that the bitstream has been loaded and the system will now start to boot. It is also possible to connect to the serial console by using the on-board UART-to-USB bridge, this allows to monitor the boot process and view debug messages.

After another few seconds the monitor connected to the system will turn on and display the `Linux mascot <https://en.wikipedia.org/wiki/Tux>`__ in the top left corner, after that the Ubuntu Desktop system will appear on the screen. The system is now ready to be used.

Post-installation tweaks
------------------------

After the system has been installed it is time to do some post-installation tweaks to the system. None of them is required to get a basic working system, but they improve the overall video and audio experience quite a bit.

Enable xf86-video-modesetting Xorg driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The xf86-video-modesetting driver is a driver which has been written to take advantage of the new Kernel Mode Setting (KMS) API of the DRM layer. This allows to switch between different screen resolutions at runtime (using the Xservers xrandr interface) and adds plug-and-play support for monitors.

Unfortunately the current Linaro Ubuntu distribution does not contain a package for xf86-video-modesetting driver. So it becomes necessary to manually download and build it. Open up a terminal on the target system and run the following commands.

.. container:: box bggreen

   
   .. note::

      Download and install xf86-video-modesetting

   
   ::
   
      > **sudo apt-get install xserver-xorg-dev libdrm-dev xutils-dev**
      > **wget http:%%//%%xorg.freedesktop.org/archive/individual/driver/xf86-video-modesetting-0.9.0.tar.bz2**
      > **tar -xjf xf86-video-modesetting-0.9.0.tar.bz2**
      > **cd xf86-video-modesetting-0.9.0**
      > **./configure --prefix=/usr**
      > **make**
      > **sudo make install**
   


To enable the modesetting driver the create /etc/X11/xorg.conf and add following lines:

Enable the modesetting driver:

::

     Section "Device"
       Identifier "ADV7511 HDMI"
       Driver "modesetting"
     EndSection

Fixing issues with pulse audio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PulseAudio is the audio daemon used by default on the Linaro Ubuntu installation. Unfortunately PulseAudio's 'glitch-free' algorithm seems to cause audio glitches on this particular platform. To get seamless audio experience it is necessary to disable the glitch-free feature. To disable the 'glitch-free' feature of pulse audio open up a terminal on the target system an run the following commands.

.. container:: box bggreen

   
   .. note::

      Disable pulse audio 'glitch-free' feature

   
   ::
   
      > **sed -i 's,load-module module-udev-detect.*,load-module module-udev-detect tsched=0,' /etc/pulse/default.pa**
   


More information
----------------

-  `AD-FMCOMMS1-EBZ Reference Design <resources/fpga/xilinx/fmc/ad-fmcomms1-ebz>`__
-  :doc:`AD-FMCOMMS2-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>`
-  :doc:`AD-FMCOMMS3-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>`
-  :doc:`AD-FMCOMMS4-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>`
-  AD-FMCOMMS5-EBZ User Guide
-  :doc:`AD-FMCDAQ2-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz>`
-  :doc:`AD-FMCADC2-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcadc2-ebz>`
-  `ADI IIO Oscilloscope <..//../linux-software/iio_oscilloscope>`__
-  `AD7511 HDMI transmitter Linux Driver <..//drm/adv7511>`__
-  `AXI HDMI HDL Linux Driver <..//drm/hdl-axi-hdmi>`__
-  `HDL AXI SPIDF Linux Driver <..//sound/hdl-axi-spidf>`__
-  `HDL AXI I2S Linux Driver <..//sound/hdl-axi-i2s>`__
-  `AD9523-1: Low Jitter Clock Generator with 14 LVPECL/LVDS/HSTL/29 LVCMOS Outputs <..//iio-pll/ad9523>`__
-  `ADF4351: Wideband Synthesizer with Integrated VCO <..//iio-pll/adf4350>`__
-  `AD8366: DC to 600 MHz, Dual-Digital Variable Gain Amplifiers <..//iio-amplifiers/ad8366>`__
-  `AD9643: 14-Bit, 170/210/250 MSPS, 1.8 V Dual Analog-to-Digital Converter (ADC) <..//iio-adc/axi-adc-hdl>`__
-  `AD9122: Dual, 16-Bit, 1200 MSPS, TxDAC+® Digital-to-Analog Converter <..//iio-dds/axi-dac-dds-hdl>`__
-  :doc:`AD9361 high performance, highly integrated RF Agile Transceiver™ Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

.. image:: https://wiki.analog.com/_media/page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn
   :alt: page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linux-drivers/platforms/linux-zynq-export-xps.png
   :width: 600px

