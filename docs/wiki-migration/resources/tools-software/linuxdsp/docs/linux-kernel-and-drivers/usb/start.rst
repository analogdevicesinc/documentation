USB Interface
=============

Introduction
------------

This document introduces usage of USB interface for SC5XX Linux. There are two different kinds of USB controller on SC5XX silicon, one supports `OTG (On-The-Go) <https://en.wikipedia.org/wiki/USB_On-The-Go>`_ for USB2.0, which is able to work as Host or Device dynamically according to the standard USB HNP protocol. Another support Host or Device only, dedicated hardware and software configurations should be made in advance to identify it is for Host or Device mode.

\*\* Example Usage Description \*\*

In this page, we cover configuration and example on how to use USB interface in Host, Device, and OTG mode, and take ADSP-SC589 EZ-Kit ( with an OTG port and a HS port) as example to demonstrate the USB usage, which using the USB - OTG port to illustrate both **Host** (Host only mode) and **OTG** ( auto-detected Dual Role mode ) cases, and the USB1-HS port to illustrate **DEVICE** (Gadget only mode)example.

--------------

Supported Board
---------------

Below table shows numbers of the USB controller for SC589/584/573 chips [supported:<fc #6495ed>✔</fc>; unsupported:<fc #ff0000>✘</fc>]

+------------------+-------------------------+-------------------------+-----------------------------+------------------------+
| Board            | Hardware Port           |                         | USB 2.0 Supported Mode      |                        |
+==================+=========================+=========================+=============================+========================+
|                  |                         | ``HOST-Host only mode`` | ``DEVICE-Gadget only mode`` | ``OTG-Dual Role mode`` |
+------------------+-------------------------+-------------------------+-----------------------------+------------------------+
| adsp-sc573-ezkit | USB0 - OTG Port ( P23 ) | <fc #6495ed>✔</fc>      | <fc #6495ed>✔</fc>          | <fc #6495ed>✔</fc>     |
+------------------+-------------------------+-------------------------+-----------------------------+------------------------+
| adsp-sc584-ezkit | USB0 - OTG Port ( P23 ) | <fc #6495ed>✔</fc>      | <fc #6495ed>✔</fc>          | <fc #6495ed>✔</fc>     |
+------------------+-------------------------+-------------------------+-----------------------------+------------------------+
| adsp-sc589-ezkit | USB0 - OTG Port ( P10 ) | <fc #6495ed>✔</fc>      | <fc #6495ed>✔</fc>          | <fc #6495ed>✔</fc>     |
+------------------+-------------------------+-------------------------+-----------------------------+------------------------+
|                  | USB1 - HS  Port ( P11 ) | <fc #ff0000>✘</fc>      | <fc #6495ed>✔</fc>          | <fc #ff0000> ✘</fc>    |
+------------------+-------------------------+-------------------------+-----------------------------+------------------------+
| adsp-sc589-mini  | USB0 - OTG Port ( P10 ) | <fc #6495ed>✔</fc>      | <fc #6495ed>✔</fc>          | <fc #6495ed>✔</fc>     |
+------------------+-------------------------+-------------------------+-----------------------------+------------------------+
|                  | USB1 - HS Port  ( J7 )  | <fc #6495ed>✔</fc>      | <fc #ff0000>✘</fc>          | <fc #ff0000> ✘</fc>    |
+------------------+-------------------------+-------------------------+-----------------------------+------------------------+

--------------

HOST - host only mode
---------------------

With the USB Host mode, we can add a lot of USB dongle peripheral to the Ez-Kits and using the corresponding features.

\*\* Hardware Connection Software Configuration \*\*

**Step 1:** Linux kernel Configuration:

.. code:: c++

   $ bitbake linux-adi -c cleansstate
   $ bitbake linux-adi -c menuconfig

**Step 2:** Configure the USB drivers to host mode:

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
           <*>   Support for Host-side USB
                   [*]   Enable USB persist by default 
                   <*>   Inventra Highspeed Dual Role Controller
                           MUSB Mode Selection (Host only mode)  --->
                           *** Platform Glue Layer *** 
                   <*>     ADI
                           *** MUSB DMA mode ***
                   [N]     Disable DMA (always use PIO)  
                   [*]       Inventra 

**Step 3:** Configure the USB host mode supported devices:

.. code:: shell

   Device Drivers  --->
           SCSI device support  --->
           <*> SCSI device support
           <*> SCSI disk support
       [*] USB support  --->
                   <*>   USB Mass Storage support

**Step 4:** Build target images:

.. code:: shell

   $ bitbake adsp-sc5xx-full

**USB Host Mode Example Usage:**

-  :doc:`USB Mass Storage </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/host_mode/usb_mass_storage>`
-  :doc:`USB Camera </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/host_mode/usb_camera>`
-  :doc:`USB Bluetooth </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/host_mode/usb_bluetooth>`
-  :doc:`USB Wireless </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/host_mode/usb_wifi>`

--------------

DEVICE - gadget only mode
-------------------------

With the USB Device mode, we can connect the the Ez-Kits to a host PC other Hosts with the USB cable and make the Ez-Kits as an USB Devices: \*\* Hardware Connection Software Configuration \*\*

**Step 1:** Linux kernel Configuration:

.. code:: c++

   $ bitbake linux-adi -c cleansstate
   $ bitbake linux-adi -c menuconfig

**Step 2:** Configure the USB drivers to device mode(gadget only):

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <N>   Support for Host-side USB
                   <*>   Inventra Highspeed Dual Role Controller
                           MUSB Mode Selection (Gadget only mode)  --->
                           *** Platform Glue Layer *** 
                   <*>     ADI
                           *** MUSB DMA mode ***
                   [N]     Disable DMA (always use PIO)  
                   [*]       Inventra
                   <*>   USB Gadget Support  --->
                         USB Physical Layer drivers  --->
                   <*> NOP USB Transceiver Driver 

**Step 3:** Configure the USB device mode supported devices:

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <*>   USB Gadget Support  --->
                         <M>   USB Gadget precomposed configurations
                         <M>     Gadget Zero (DEVELOPMENT)
                         <M>     Audio Gadget
                         [*]       UAC 1.0
                         [*]         UAC 1.0 (Legacy)
                         <M>     Ethernet Gadget (with CDC Ethernet support)
                         [*]       RNDIS support
                         <M>     Gadget Filesystem   
                         <M>     Mass Storage Gadget      
                         <M>     Serial Gadget (with CDC ACM and CDC OBEX support)
                         <M>     HID Gadget 

**Step 4:** Build target images:

.. code:: shell

   $ bitbake adsp-sc5xx-full

**USB Device Mode Example Usage:**

-  :doc:`Gadget Zero Support </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/device_mode/gdaget_zero>`
-  :doc:`Gadget Audio Support </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/device_mode/gdaget_audio>`
-  :doc:`Ethernet Gadget Support </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/device_mode/gdaget_eth>`
-  :doc:`Serial Gadget Support </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/device_mode/gdaget_serial>`
-  :doc:`Gadget Filesystem Support </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/device_mode/gadget_fs>`
-  :doc:`Mass Storage Gadget Support </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/device_mode/gadget_mass_storage>`

--------------

OTG - dual role mode
--------------------

The USB OTG port can work as either Host or Device, depends on the way we connect it, for Host or Device application, as illustrated previously.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/003_usb_otg_mode_hardware_connection.png
   :align: center

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
