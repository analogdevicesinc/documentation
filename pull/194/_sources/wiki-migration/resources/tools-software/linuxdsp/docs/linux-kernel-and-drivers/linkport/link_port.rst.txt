Link Port driver
================

Introduction
------------

Link ports allow the processor to connect to other processors or peripheral link ports using a simple communication protocol for high-speed parallel data transfer. This peripheral allows a variety of I/O peripheral interconnection schemes to I/O peripheral devices as well as co-processing and multiprocessing schemes.This document describes how to do a data transaction test via link ports on SC5xx EZ-Board.  

Hardware Setup
--------------

-  An ADSP-SC5xx EZ-Board:

   -  ADSP-SC589 Ezkit v1.1 and above, or,

      -  ADSP-SC584 Ezkit v1.0 and above, or,
      -  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above

-  A linkport cable

 Connect the LINK PORT 0 and LINK PORT 1 with the matched cable in the target board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/linkport/lkad-link_port_driver-hw_setup.jpg
   :width: 400px

Software configuration
----------------------

The following configuration should be done on top of the SC589-ezkit/SC584-ezkit/SC573-ezkit default configuration. 

Configure Packages
~~~~~~~~~~~~~~~~~~

You should also enable the linkport-test program to assist with testing. Add the linkport-test program in the filesystem images, it's enabled in adsp-sc5xx-full image by default.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "linkport-test"

Linux kernel configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Enable Linkport driver**

::

   Device Drivers --->
       Character devices ---> 
       <*> ADI LINKPORT driver

**Note:** For **SC589-ezkit/SC584-ezkit/SC573-ezkit**:

-  Need to disable the **SPI** support, due to Linkport hardware pin conflicts with SPI.
-  Need to disable the **MTD** support, due to Linkport hardware pin conflicts with MTD.
-  Need to disable the **CAN** bus support, due to Linkport hardware pin conflicts with CAN bus.
-  Need to disable the **Network device** support, due to Linkport hardware pin conflicts with Netework device.

::

   [*] Networking support --->
       <N> CAN bus subsystem support ----
   Device Drivers --->
       <N> Memory Technology Device (MTD) support ---- 
       [N] SPI support ---- 
       [N] Network device support ---- 

Then run bitbake linux-adi -C compile to generate kernel image zImage and dtb file.

**Note: nfsboot can't work without the network support**

Test Example
------------

linkport_test will send data to linkport1, and receive data from linkport0, then verify the data.

::

   # linkport_test
   linkport test passed

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
