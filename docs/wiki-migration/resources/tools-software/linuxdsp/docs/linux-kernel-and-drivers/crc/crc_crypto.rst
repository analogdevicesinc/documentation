CRC Crypto Driver Guide
=======================

Introduction
------------

The CRC peripheral in ADSP-SC5xx processors is a hardware block used to compute the CRC of a block of data. It is a CRC32 engine which computes the CRC value of 32-bit data words presented to it. For data words of < 32-bit in size, it is the responsibility of application to pack the data into 32-bit data units.

The main features of the CRC peripheral are:

-  Memory Scan mode
-  Memory Transfer mode
-  Data Verify mode
-  Data Fill mode
-  32b CRC polynomial (Programmable polynomials)
-  Bit/Byte Mirroring option
-  Fault/Error interrupt mechanisms

The Linux CRC driver is based on the Linux crypto driver framework. The Scatterlist Crypto API takes page vectors (scatterlists) as arguments, and works directly on memory pages. The CRC driver implements the asynchronous hash interface. The CRC results are calculated via array-descriptor-based DMA operation, which is generated at run time. If the input buffer length is not a multiple of 32 bits this driver appends zeroes automatically. The framework only supports Memory Scan mode. This driver can be found at linux-kernel/drivers/crypto/adi_crc.c . The SC5xx and the BF609 share the same Linux CRC driver because the same CRC peripheral IP is used in both processors, the only difference is that the driver platform data is defined in the board file for BF609 but in the device tree file for SC5xx.

Hardware Setup
--------------

An ADSP-SC5xx EZ-Board:

-  ADSP-SC589 Ezkit v1.1 and above, or,
-  ADSP-SC589 Ezkit v1.1 and above, or,
-  ADSP-SC584 Ezkit v1.0 and above, or,
-  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above 

Software Configuration
----------------------

Configure Linux Kernel
~~~~~~~~~~~~~~~~~~~~~~

Run **bitbake linux-adi -c menuconfig** and configure the kernel as follows:

::

   Cryptographic API  --->
       -*-   Cryptographic algorithm manager
       {*}   HMAC support 
       [*]   Hardware crypto devices  --->
           <*>   Support for ADI SC5XX CRC hareware

To include a CRC test suite module in the kernel:

::

   Cryptographic API  --->
       [N]   Disable run-time self tests
       <M>   Testing module

Example
-------

When the kernel is booting up on SC5xx, you can check if the Crypto CRC driver probes devices correctly by looking for the following two lines of output:

::

   ADI hardware CRC crypto driver
   adi-hmac-crc 31001200.crc: initialized
   adi-hmac-crc 31001300.crc: initialized

You can also run a full test with tcrypt kernel module. This test module always exits with the warning "can't load module tcrypt" no mater whether the test passes or fails. However, if any test error occurs, “tcrypt: one or more tests failed” is printed out.

::

   root:/> modprobe tcrypt mode=110
   modprobe: can't load module tcrypt (kernel/crypto/tcrypt.ko): Resource temporarily unavailable

Linux Kernel Crypto API
-----------------------

If you want to use this CRC driver via the Linux kernel crypto API, please refer to the generic `Linux Kernel Crypto API <http://www.chronox.de/crypto-API/>`_ document . 

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
