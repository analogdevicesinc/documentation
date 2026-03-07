Mobile Storage Interface (MSI)
==============================

Overview
--------

Some of the ADSP-SC5xx processors provide a mobile storage interface(MSI). MSI is a fast, synchronous controller that uses various protocols to communicate with MMC, SD, and SDIO cards to address the growing storage need in embedded systems, handheld and consumer electronics applications requiring low power. The MSI is compatible with the following protocols.

-  MMC (Multimedia Card) bus protocol
-  SD (Secure Digital) bus protocol
-  SDIO (Secure Digital Input Output) bus protocol

All of these storage solutions use similar interface protocols. The main difference between MMC and SD support is the initialization sequence. The main difference between SD and SDIO support is the use of interrupt and read wait signals for SDIO.

Hardware Setup
--------------

-  An ADSP-SC5xx EZ-Board:

   -  ADSP-SC589 Ezkit v1.1 and above, or,

      -  ADSP-SC584 Ezkit v1.0 and above, (the SC584 processor does not include the MSI interface), or,
      -  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above

-  SD card

The SD/MMC card slot is **J18** on the SC589-EZKIT and SC573-EZKIT board. This slot accepts full-size SD and MMC cards, or microSD cards with an adapter.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/das-u-boot/dasu-mobile_sorage-hw_setup.jpg
   :width: 600px

Software Configuration
----------------------

To enable the MSI driver add the following MSI-related config macros in **include/configs/sc589-ezkit.h** or **include/configs/sc573-ezkit.h**

::

   #define CONFIG_GENERIC_MMC
   #define CONFIG_MMC
   #define CONFIG_SC5XX_DWMMC
   #define CONFIG_DWMMC
   #define CONFIG_BOUNCE_BUFFER

Build and Load Uboot
--------------------

A UBoot image can now be built and loaded onto the target board.  See :doc:`Building The Linux Components </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/building>` and :doc:`Installing Linux On The Hardware </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/installing>`\ for details.

Usage of MSI Driver
-------------------

Initialize MSI(MMC/SDIO) Sub-System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   # mmc info
   Device: SC5XX SDH
   Manufacturer ID: 3
   OEM: 5344
   Name: SD01G
   Tran Speed: 25000000
   Rd Block Len: 512
   SD version 1.10
   High Capacity: No
   Capacity: 968.8 MiB
   Bus Width: 4-bit 

Get More MMC Command Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   # mmc help
   or
   # help mmc

 

| 
| ----

.. container:: group

   
   .. container:: half column

      \**Pre: :doc:`Loading file from USB storage in u-boot </wiki-migration/resources/tools-software/linuxdsp/docs/das-u-boot/loading_file_from_usb_storage_in_uboot>`\ **\

   
   .. container:: half column

      **\ Back To: \*\*\ :doc:`Das U-boot </wiki-migration/resources/tools-software/linuxdsp/docs/das-u-boot>`

   

