Ethernet Driver in U-Boot on SC5xx-EZKIT
========================================

Overview
--------

Ethernet driver provides driver for the MAC controller present in ADI processors. The ethernet driver package also has code to interface with the PHYs on the ADI released boards.

There are 2 network interfaces on ADSP-SC5xx : EMAC0 and EMAC1

-  EMAC0 is configurable as 10/100 Mbps, interfacing via RMII, or 10/100/1000 Mbps, interfacing via RGMII. On the SC5xx-EZ-Board the RGMII interface is used, providing 10/100/1000 Mbps (gigabit) capability
-  EMAC1 is a fixed 10/100 Mbps EMAC, interfacing via RMII.

Hardware Setup
--------------

-  ADSP-SC589 Ezkit v1.1 and above, or,
-  ADSP-SC584 Ezkit v1.0 and above, or,
-  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above

Build U-Boot with emac0 or emac1
--------------------------------

U-Boot only supports one network port.  You have to select one emac port in include/configs/sc589-ezkit.h at build time.(For SC584/SC573 EZ-Board , we should do it in file sc584-ezkit.h or sc573-ezkit.h)

::

   #define CONFIG_DW_PORTS         1  // enable EMAC0
   or
   #define CONFIG_DW_PORTS         2  // enable EMAC1

Using EMAC Driver
-----------------

U-boot provides a set of basic net commands:

-  dhcp    - invoke a DHCP client request to obtain IP/boot params
-  ping    - send a ICMP ECHO_REQUEST to the network host
-  tftpboot - boot an image via network using the TFTP protocol

For example:

::

   CPU:   ADSP ADSP-SC589-0.0 (Detected Rev: 1.1) (spi flash boot)
   VCO: 450 MHz, Cclk0: 450 MHz, Sclk0: 112.500 MHz, Sclk1: 112.500 MHz, DCLK: 225 MHz
   OCLK: 150 MHz
   I2C:   ready
   DRAM:  112 MiB
   MMC:   SC5XX SDH: 0
   SF: Detected W25Q128BV with page size 256 Bytes, erase size 4 KiB, total 16 MiB
   In:    serial
   Out:   serial
   Err:   serial
   other init
   Net:   dwmac.3100c000
   Hit any key to stop autoboot:  0 
   sc #  
   sc # dhcp
   Speed: 100, full duplex
   BOOTP broadcast 1
   BOOTP broadcast 2
   DHCP client bound to address 10.99.24.200 (260 ms)
   sc # ping 10.99.24.94
   Speed: 100, full duplex
   Using dwmac.3100c000 device
   host 10.99.24.94 is alive
   sc # tftp ${loadaddr} ${ramfile}
   Speed: 100, full duplex
   Using dwmac.3100c000 device
   TFTP from server 10.99.24.94; our IP address is 10.99.24.200
   Filename 'uImage'.
   Load address: 0x89000000
   Loading: #################################################################
        #################################################################
   ......
    #####################################
        2 MiB/s
   done
   Bytes transferred = 10502080 (a03fc0 hex)

 

| 
| ----

.. container:: group

   
   .. container:: half column

      \**Pre: :doc:`Das U-boot </wiki-migration/resources/tools-software/linuxdsp/docs/das-u-boot>`\ **

   
   .. container:: half column

      **\ Next: \*\*\ :doc:`Loading file from USB storage in u-boot </wiki-migration/resources/tools-software/linuxdsp/docs/das-u-boot/loading_file_from_usb_storage_in_uboot>`

   

