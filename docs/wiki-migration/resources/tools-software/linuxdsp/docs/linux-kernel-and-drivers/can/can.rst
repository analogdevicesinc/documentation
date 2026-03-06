CAN Bus Data Transaction
========================

Introduction
------------

This document describes how to do a data transaction test via CAN bus on SC5xx EZ-Board. Take ADSP SC589-EZKIT as an example.

Hardware Setup
--------------

Two ADSP-SC5xx EZ-Boards: 

-  ADSP-SC589 Ezkit v1.1 and above, or,
-  ADSP-SC584 Ezkit v1.0 and above, or,
-  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above

An RJ-11 crossover cable Connect the RJ-11 port labelled "CAN0/HU CONTROL" or "ACN1/ENGINE"on each board together with the crossover cable.

Connect a serial cable for each of the board to PC so we have a serial console for each of the boards.

Software Setup
--------------

Configure Linux Kernel
~~~~~~~~~~~~~~~~~~~~~~

Run **bitbkae linux-adi -c menuconfig** and configure the kernel as follows:

::

   Networking support  --->
       <*>   CAN bus subsystem support  --->
           <*>   Raw CAN Protocol (raw access with CAN-ID filtering)
           <*>   Broadcast Manager CAN Protocol (with content filtering)
           CAN Device Drivers  --->
               <*> Platform CAN drivers with Netlink support
               [*]   CAN bit-timing calculation
               <M>   Analog Devices SC5xx on-chip CAN
   Device Drivers  --->
       [*] SPI support  --->
           <*>   SPI controller v3 for ADI

For ADSP-SC573 Ezkit, Users should additionally disable the MMC support from Linux Kernel menuconfig due to pin conflict. Please refer to Mobile Storage Interface for MMC/SD.

::

   Device Drivers
       MMC/SD/SDIO card support  --->
           [*] Synopsys DesignWare Memory Card Interface
           [*]   Synopsys Designware MCI Support as platform device
           [N]   ADI specific extensions forSynopsys DW Memory Card Interface

Configure Device Tree
~~~~~~~~~~~~~~~~~~~~~

Need to disable the spidev from the device tree file due to SPI chip select line conflict. Please refer to SPI Driver;

For ADSP-SC573 Ezkit:

::

   $ bitbake linux-adi -c devshell
   $ vim arch/arm/boot/dts/sc573-ezkit.dts

   -   spidev {
   -          #address-cells = <1>;
   -           #size-cells = <1>;
   -           compatible = "rohm,dh2228fv";
   -           spi-max-frequency = <5000000>;
   -           reg = <38>;
   -   };

For other boards (sc589-ezkit.dts/sc589-mini.dts/sc584-ezkit.dts)

::

   $ bitbake linux-adi -c devshell
   $ vim arch/arm/boot/dts/sc589-ezkit.dts
   -   spidev {
   -          #address-cells = <1>;
   -           #size-cells = <1>;
   -           compatible = "rohm,dh2228fv";
   -           spi-max-frequency = <5000000>;
   -           reg = <44>;
   -   };

Then you must run "**bitbake linux-adi -C compile**" so that the changes can be effective.

Copy zImage and sc589-ezkit.dtb to /tftpboot directory

::

   cp ${YOCTO_DIR}/build/tmp/deploy/images/adsp-sc589-ezkit/zImage /tftpboot

   cp ${YOCTO_DIR}/build/tmp/deploy/images/adsp-sc589-ezkit/sc589-ezkit.dtb /tftpboot

As to filesystem, use the adsp-sc5xx-full image.

CAN0(HU CONTROL) Test Example
-----------------------------

Bring Up CAN0 Interface On Both Boards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command on both of the boards:

::

   root:/> modprobe sc5xx_can
   sc5xx_can 31000200.can: sc5xx_can device registered(&reg_base=0c450739, rx_irq=22, tx_irq=23, err_irq=24, sclk=112500000)

   sc5xx_can 31000a00.can: sc5xx_can device registered(&reg_base=de8b6d1d, rx_irq=25, tx_irq=26, err_irq=27, sclk=112500000)

   root:/> ip link set can0 type can bitrate 125000
   sc5xx_can 31000200.can can0: setting CLOCK=0x003b TIMING=0x001b
   root:/> ifconfig can0 up

Data Send & Receive Test
~~~~~~~~~~~~~~~~~~~~~~~~

Run the data receiving program on one of the boards:

::

   root:/> candump can0

Run the data sending program on the other board:

::

   root:/> cansend can0 123#AABBCCDD
   root:/> cansend can0 123#R 
   root:/> cansend can0 1F334455#1122334455667788
   root:/> cansend can0 1F334455#R

You should now see the transmitted data printing on the console of the receiving board:

::

   can0  123  [4] AA BB CC DD
   can0  123  [0] remote request
   can0  1F334455  [8] 11 22 33 44 55 66 77 88
   can0  1F334455  [0] remote request

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
