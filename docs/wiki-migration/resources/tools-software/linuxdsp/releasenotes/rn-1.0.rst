Yocto Linux for ADSP-SC5xx Processors - Release 1.0.0: Release Notes
====================================================================

Introduction
------------

The Yocto Linux for ADSP-SC5xx Processors product is a new software product that provides users with a Yocto based Linux solution for supported ADSP-SC5xx processors. This product will replace the Linux Add-In for CrossCore Embedded Studio as the active Linux product for ADSP-SC5xx processors. Note that there is no direct upgrade path for projects that use the Linux Add-In. Please see the **Notable Changes from the Linux Add-In Product** for more details.

Supported Linux Distributions
-----------------------------

The Yocto Linux for ADSP-SC5xx processors product is formally supported on **Ubuntu 18.04 LTS 64-bit**. While the product will likely build on other modern Linux distributions, ADI support for build issues will only be provided when using the supported Linux distribution.

Supported Processors and EZ-KITs
--------------------------------

The following processors and silicon revisions are supported by the Yocto Linux for ADSP-SC5xx product.

.. important::

   Note: The supported processor silicon revision list is different from the Linux Add-In product. Earlier revisions of some EZ-KITs contained different hardware. These are not supported by the Yocto Linux product.


+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| Development Board                                                                                                                                              | Supported Revision |
+================================================================================================================================================================+====================+
| :adi:`ADSP-SC589 EZ-KIT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADSP-SC589.html>`                                       | 2.0 or later       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| :adi:`ADSP-SC584 EZ-KIT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADSP-SC584.html>`                                       | 2.0 or later       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| :adi:`ADSP-SC573 EZ-KIT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/SC573EZKIT.html>`                                            | 2.0 or later       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| :doc:`ADSP-SC589-MINI </wiki-migration/resources/tools-software/sharc-audio-module>`                                                                           | 1.5 or later       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+

System Requirements
-------------------

The following system requirements are recommended:

-  Modern multi-core CPU
-  8GB RAM
-  At least 60GB of disk space

For installation on the development board your host PC will require:

-  Two open USB ports

Note: The Yocto Linux product is built from source. For improved performance we recommend at least 4 cores and a SSD disk.

Obtaining Technical Support
---------------------------

You can reach Analog Devices software and tools technical support in the following ways:

-  Post your questions in the software and development tools support community at [[/\|\ :ez:`dsp/software-and-development-tools/linux-for-adsp-sc5xx-processors/f/q-a%7CAnalog` Devices Engineer Zone]] ®
-  E-mail your questions about processors and processor applications to processor.support@analog.com
-  Submit your questions to technical support directly via http://www.analog.com/support
-  Contact your Analog Devices sales office or authorized distributor

New Features And Changes
------------------------

This is the first release of the Yocto Linux for ADSP-SC5xx Processors product.

Notable Changes from the Linux Add-In Product
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following major changes have occurred since the last release of the Linux Add-In for Cross-Core Embedded Studio:

-  Replaced Buildroot build system with Yocto (version Thud)
-  Upgraded Linux kernel from 4.04 to 4.19 LTS
-  Replaced corectrl utility with Linux kernel remoteproc feature
-  Improved stability for MCAPI multi-core message passing
-  Binary images are no longer provided by Analog Devices

Known Issues
------------

The following issues are known for this release:

-  Limited MCAPI support:  MCAPI supports communication using the message transaction type. Packet and Scalar types are not supported in this release. It was found that although the previous release supported these data types, the support was faulty. For more information on supported MCAPI functionality please refer to the MCAPI section :doc:`Multicore Support </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/mcapi/start>`
-  SHARC core control: An issue exists where by attempting to halt the SHARC cores from Linux, the SHARC core may end in a hung state and will not be  able to be restarted again from Linux.
-  ADSP-SC584 EZ-Kit does not support the Video Decoder and Encoder EI3 Extender Board. This is a limitation of the EZ-Kit. Driver support is provided and this extender board may be used with custom hardware which can support the board.
-  ADSP-SC573 does not support the WVGA/LCD EI3 Extender Board. This is a limitation of the EZ-Kit. Driver support is provided and the extender may be used with a compatible custom board.
-  ADSP-SC573 EZ-KIT is only supported for BOM versions >= 1.8. Due to issues with the SD Card support, the ADSP-SC573 port in this release will only be supported on versions of the ADSP-SC573 EZ-KIT whose BOM version is at least 1.8. The BOM version is recorded on the underside of the EZ-KIT on a square white sticker.
-  SD Card and Rotary can't work simultaneously on ADSP-SC573 EZ-KIT. This is a limitation of the multiplexing pin conflict of the EZ-Kit. Rotary is disabled by default out of box on ADSP-SC573 EZ-KIT.
-  QT, Mplayer and Bluetooth ALSA for all processors are not support in this release.

| 
| ---- \**HOME PAGE: \*\* :doc:`Linux for ADSP-SC5xx Processors </wiki-migration/resources/tools-software/linuxdsp>`
