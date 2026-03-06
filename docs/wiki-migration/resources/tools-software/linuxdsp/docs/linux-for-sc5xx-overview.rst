.. warning::

   These pages are not updated anymore. Documentation has been moved to :git-lnxdsp-adi-meta:`wiki\`


Linux For ADSP-SC5xx: Overview
==============================

When we talk about Linux running on the ADSP-SC5xx we are generally talking about more than Linux. Linux itself refers to the Operating System. The software that is installed on to the processor consists of several components; a second-stage bootloader (U-Boot), a package file (uImage, or zImage if it is compressed) which contains the Linux kernel and a filesystem, and a .dtb file (device tree blob) which defines the system hardware.

Booting Linux On the SC5xx
--------------------------

There are several ways for Linux to boot on the ADSP-SC5xx development boards, but all of them follow the same overall sequence of operations:

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linuxdsp_boot_overview.jpg
   :alt: linuxdsp_boot_overview.jpg
   :align: center
   :width: 600px

Booting From Different Sources
------------------------------

The `U-Boot Bootloader <https://www.denx.de/wiki/U-Boot>`__ is a sophisticated second stage bootloader that comes with the ability to boot applications from a series of sources (flash, network, SD Card, USB). It even has it's own shell for debugging and development.

During the boot process U-Boot will be extracted from flash and executed where its purpose will be to:

-  Copy the uImage file in to RAM
-  Extract the kernel and filesystem from the uImage
-  Copy the DTB file in to RAM
-  Call the Linux kernel

The uImage file may be located on different types of storage. For the ADSP-SC5xx processor we support the following boot options where hardware permits:

-  Copied over the network
-  Stored in flash
-  Stored on SD Card/Micro SD Card
-  Stored on USB

It is recommended that for development purposes you begin with a system as described in the Getting Started Guide where you boot from a network image. This makes it easier to rebuild and deploy changes to the system. As you further develop your application you will need to consider where you image will be stored in your final product.

Kernel And Driver Configuration
-------------------------------

Analog Devices provides the Linux kernel and system boot pre-configured for the SC5xx hardware. If the system is configured to build the **full** image, all supported drivers will be built into the kernel and the corresponding software stacks will be initialized during system bring-up. Later you can configure your system to include only the features required for your system.

During boot the kernel will initialize, parse the DTB file to determine what hardware peripherals are available, then begin to initialize the system.
