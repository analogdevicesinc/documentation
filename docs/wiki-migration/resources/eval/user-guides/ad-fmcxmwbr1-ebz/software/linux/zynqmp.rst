AD-FMCXMWBR1-EBZ on ZynqMP ADRV9009-ZU11EG-ADRV2CRR-FMC
=======================================================

The image for the AD-FMCXMWBR1-EBZ FMC Card on the ADRV9009-ZU11EG-ADRV2CRR-FMC can be found, and created by following the directions :doc:`here </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.

Building the ZynqMP / MPSoC Linux kernel and devicetrees from source
====================================================================

The script method
-----------------

We provide `a script that does automates <https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/linux/build_zynqmp_kernel_image.sh>`__ the build for Zynq using the Linaro toolchain.

<fc #ff0000>\ **Note**\ </fc> that this script differs from the one for Zynq.

The script takes up to 3 parameters, but if left blank, it uses defaults:

-  **<local_kernel_dir>** - default is **linux-adi** if left blank ; use this, if you want to use an already cloned kernel repo
-  **<devicetree_file>** - which device tree should be exported/copied from the build ; default is ``zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb`` for Zynq
-  **<path_to_other_toolchain>** - in case you have your own preferred ARM64 toolchain [other than Linaro's or Xilinx's] you can use override it with this 3rd param

The script will:

-  clone the ADI kernel tree
-  download the Linaro GCC toolchain [if no other is specified]
-  build the ADI kernel tree
-  export/copy the Image file and device tree file out of the kernel build folder

Running the script in one line [with defaults]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   wget https://raw.githubusercontent.com/analogdevicesinc/wiki-scripts/master/linux/build_zynqmp_kernel_image.sh && chmod +x build_zynqmp_kernel_image.sh && ./build_zynqmp_kernel_image.sh zynqmp

Building using Petalinux
------------------------

Please see here: :doc:`Building with Petalinux </wiki-migration/resources/tools-software/linux-build/generic/petalinux>`

On the development host
-----------------------

::

   git clone https://github.com/analogdevicesinc/linux.git

or do a git pull in the existing repository.

Checkout the master development/master branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   dave@hal9000:~/github-linux-build/linux$ git checkout master
   Already on 'master'
   Your branch is up-to-date with 'origin/master'.

Add aarch64-linux-gnu-gcc to PATH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vivado 2016.2 SDK may be installed into a different directory

::

   dave@hal9000:~/github-linux-build/linux$ export PATH=$PATH:/opt/Xilinx/SDK/2017.2/gnu/aarch64/lin/aarch64-linux/bin

Setup cross compile environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   dave@hal9000:~/github-linux-build/linux$ export ARCH=arm64

   dave@hal9000:~/github-linux-build/linux$ export CROSS_COMPILE=aarch64-linux-gnu-

Configure the kernel
~~~~~~~~~~~~~~~~~~~~

::

   dave@hal9000:~/github-linux-build/linux$ make adi_zynqmp_defconfig 
   #
   # configuration written to .config
   #
   dave@hal9000:~/github-linux-build/linux$

Build the kernel
~~~~~~~~~~~~~~~~

::

   dave@hal9000:~/github-linux-build/linux$ make -j5 Image UIMAGE_LOADADDR=0x8000
     CHK     include/config/kernel.release
     CHK     include/generated/uapi/linux/version.h
     HOSTCC  scripts/basic/fixdep
     HOSTCC  scripts/basic/bin2c


   [ -- snip --]

     CC      init/version.o
     LD      init/built-in.o
     KSYM    .tmp_kallsyms1.o
     KSYM    .tmp_kallsyms2.o
     LD      vmlinux
     SORTEX  vmlinux
     SYSMAP  System.map
     OBJCOPY arch/arm64/boot/Image
   dave@hal9000:~/github-linux-build/linux$

Build the devicetree FCMOMMS2/3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build the one that fits your FPGA carrier and FMC card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dts | `ZCU102 <https://www.xilinx.com/ZCU102>`__ **Rev. 1.0** and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board |
+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynqmp-zcu102-rev10-ad9364-fmcomms4.dts   | `ZCU102 <https://www.xilinx.com/ZCU102>`__ **Rev. 1.0** and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` or :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board |
+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynqmp-zcu102-revB-ad9361-fmcomms2-3.dts  | `ZCU102 <https://www.xilinx.com/ZCU102>`__ Rev.B and the :doc:`AD-FMCOMMS2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`AD-FMCOMMS3-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>` board        |
+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zynqmp-zcu102-revB-ad9364-fmcomms4.dts    | `ZCU102 <https://www.xilinx.com/ZCU102>`__ Rev.B and the :doc:`AD-FMCOMMS4-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>` board                                                                                               |
+-------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

::

   dave@hal9000:~/github-linux-build/linux$  make xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb
     DTC     arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms2-3.dtb
   dave@hal9000:~/github-linux-build/linux$

Copy the generated files to your SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   dave@hal9000:~/github-linux-build/linux$ cp arch/arm64/boot/Image /media/michael/BOOT/
   dave@hal9000:~/github-linux-build/linux$ cp arch/arm64/boot/dts/xilinx/zynqmp-zcu102-revB-ad9361-fmcomms2-3.dtb /media/michael/BOOT/system.dtb

Building the ZynqMP boot image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| The boot image BOOT.BIN is build using the bootgen tool which requires several input files.
| Instructions on how to build the Hardware Description File (HDF) handover file can be found here:

-  :doc:`Building HDL </wiki-migration/resources/fpga/docs/build>`

All further steps are lengthy explained on the `Xilinx Wiki Page <http://www.wiki.xilinx.com>`__

-  `Build u-boot <http://www.wiki.xilinx.com/Build+U-Boot>`__

   -  Make sure you checkout the proper git tag matching your Vivado Version (xilinx-v2018.2, xilinx-v2017.4, ...)

-  `Build FSBL <http://www.wiki.xilinx.com/Build+FSBL>`__
-  `Build PMU Frimware <http://www.wiki.xilinx.com/Build+PMU+Firmware>`__
-  `Build Arm Trusted Firmware (ATF) <http://www.wiki.xilinx.com/Build+Arm+Trusted+Firmware+%28ATF%29>`__
-  `Build BOOT image <http://www.wiki.xilinx.com/Prepare+Boot+Image>`__

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

-  When using **cygwin**, you can add the following in the ~/.bashrc configuration file:

::

   export PATH=$PATH:/cygdrive/c/Xilinx/Vivado/202x.x/bin
   export PATH=$PATH:/cygdrive/c/Xilinx/Vitis/202x.x/bin
   export PATH=$PATH:/cygdrive/c/Xilinx/Vitis/202x.x/gnu/microblaze/nt/bin

|

.. tip::

   \ **NOTE: u-boot.elf**

   | For those who don't want to build u-boot themselves.
   | The **u-boot.elf** can be extracted from the project folder on the :doc:`SD Card image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`, **bootgen_sysfiles.tgz**
   


AD-FMCXMWBR1-EBZ devicetree example
===================================

An example of device tree for the AD-FMCXMWBR1-EBZ SPI/I2C/GPIO connections to different ADI devices:

-  :doc:`AD7291 </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7291>`
-  `AD5721 <https://github.com/torvalds/linux/blob/master/drivers/iio/dac/ad5761.c>`__

::

   #include "zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-jesd204-fsm.dts"

   &fpga_axi {
       axi_i2c_1: i2c@83000000 {
           #address-cells = <1>;
           #size-cells = <0>;
           clock-names = "s_axi_aclk";
           clocks = <&zynqmp_clk 71>;
           compatible = "xlnx,axi-iic-2.0", "xlnx,xps-iic-2.00.a";
           interrupt-names = "iic2intc_irpt";
           interrupt-parent = <&gic>;
           interrupts = <0 90 IRQ_TYPE_LEVEL_HIGH>;
           reg = <0x0 0x83000000 0x1000>;
       };

       axi_i2c_2: i2c@83100000 {
           #address-cells = <1>;
           #size-cells = <0>;
           clock-names = "s_axi_aclk";
           clocks = <&zynqmp_clk 71>;
           compatible = "xlnx,axi-iic-2.0", "xlnx,xps-iic-2.00.a";
           interrupt-names = "iic2intc_irpt";
           interrupt-parent = <&gic>;
           interrupts = <0 91 IRQ_TYPE_LEVEL_HIGH>;
           reg = <0x0 0x83100000 0x1000>;
       };

       axi_spi_1: spi@84000000 {
           #address-cells = <1>;
           #size-cells = <0>;
           bits-per-word = <8>;
           compatible = "xlnx,xps-spi-2.00.a";
           reg = <0x0 0x84000000 0x1000>;
           fifo-size = <16>;
           interrupts = <0 92 IRQ_TYPE_EDGE_RISING>;
           num-cs = <0x8>;
           xlnx,num-ss-bits = <0x8>;
           xlnx,spi-mode = <0>;
       };

       axi_spi_2: spi@84500000 {
           #address-cells = <1>;
           #size-cells = <0>;
           bits-per-word = <8>;
           compatible = "xlnx,xps-spi-2.00.a";
           reg = <0x0 0x84500000 0x1000>;
           fifo-size = <16>;
           interrupts = <0 93 IRQ_TYPE_EDGE_RISING>;
           num-cs = <0x8>;
           xlnx,num-ss-bits = <0x8>;
           xlnx,spi-mode = <0>;
       };

       axi_gpio: gpio@86000000 {
           #gpio-cells = <2>;
           #interrupt-cells = <2>;
           clock-names = "s_axi_aclk";
           clocks = <&zynqmp_clk 71>;
           compatible = "xlnx,axi-gpio-2.0", "xlnx,xps-gpio-1.00.a";
           gpio-controller;
           interrupt-controller;
           interrupt-names = "ip2intc_irpt";
           interrupt-parent = <&gic>;
           interrupts = <0 9 4>;
           reg = <0x0 0x86000000 0x1000>;
           xlnx,all-inputs = <0x0>;
           xlnx,all-inputs-2 = <0x0>;
           xlnx,all-outputs = <0x0>;
           xlnx,all-outputs-2 = <0x0>;
           xlnx,dout-default = <0x00000000>;
           xlnx,dout-default-2 = <0x00000000>;
           xlnx,gpio-width = <0x20>;
           xlnx,gpio2-width = <0x20>;
           xlnx,interrupt-present = <0x1>;
           xlnx,is-dual = <0x1>;
           xlnx,tri-default = <0xFFFFFFFF>;
           xlnx,tri-default-2 = <0xFFFFFFFF>;
       };
   };

   &axi_i2c_1 {
       ad7291_1@2f {
           label = "ADC_I2C_1";
           compatible = "adi,ad7291";
           reg = <0x2f>;
       };
   };

   &axi_i2c_2 {
       ad7291_2@2f {
           label = "ADC_I2C_2";
           compatible = "adi,ad7291";
           reg = <0x2f>;
       };
   };

   &axi_spi_1 {
       ad5721r_1@0 {
           label = "DAC_SPI_1";
           compatible = "adi,ad5721r";
           reg = <0>;
           spi-max-frequency = <500000>;
       };
   };

   &axi_spi_2 {
       ad5721r_2@0 {
           label = "DAC_SPI_2";
           compatible = "adi,ad5721r";
           reg = <0>;
           spi-max-frequency = <500000>;
       };
   };

   &i2c_fmc {
       eeprom@52 {
           compatible = "at24,24c02";
           reg = <0x52>;
       };
   };

Devicetree AD-FMCXMWBR1-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:git-linux:`arch/arm64/boot/dts/xilinx/zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb-jesd204-fsm-fmcbridge.dts`

SPI/I2C device access via AD-FMCXMWBR1-EBZ from linux userspace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   analog@analog:/sys/bus/iio/devices $ ls -l
   total 0
   lrwxrwxrwx 1 root root 0 Feb 14 14:48 iio:device1 -> ../../../devices/platform/fpga-axi@0/84000000.spi/spi_master/spi1/spi1.0/iio:device1
   lrwxrwxrwx 1 root root 0 Feb 14 14:48 iio:device2 -> ../../../devices/platform/fpga-axi@0/84500000.spi/spi_master/spi2/spi2.0/iio:device2
   lrwxrwxrwx 1 root root 0 Feb 14 14:48 iio:device5 -> ../../../devices/platform/fpga-axi@0/83000000.i2c/i2c-11/11-002f/iio:device5
   lrwxrwxrwx 1 root root 0 Feb 14 14:48 iio:device6 -> ../../../devices/platform/fpga-axi@0/83100000.i2c/i2c-12/12-002f/iio:device6

GPIO control via AD-FMCXMWBR1-EBZ from linux userspace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   analog@analog:/sys/class/gpio $ ls -l
   total 0
   -rwxrwx--- 1 root gpio 4096 Feb 14 14:48 export
   lrwxrwxrwx 1 root gpio    0 Feb 14 14:48 gpiochip448 -> ../../devices/platform/fpga-axi@0/86000000.gpio/gpio/gpiochip448
   -rwxrwx--- 1 root gpio 4096 Feb 14 14:48 unexport
