Yocto Linux for ADSP-SC5xx Processors - Release 2.1.0: Release Notes
====================================================================

Introduction
------------

This release contains an upgrade of all the key components to a recent LTS release.

Supported Linux Distributions
-----------------------------

The Yocto Linux for ADSP-SC5xx processors product is formally supported on **Ubuntu 20.04 LTS 64-bit**. While the product will likely build on other modern Linux distributions, ADI support for build issues will only be provided when using the supported Linux distribution.

Supported Processors and EZ-KITs
--------------------------------

The following processors and silicon revisions are supported by the Yocto Linux for ADSP-SC5xx product.

.. important::

   Note: The supported processor silicon revision list is different from the Linux Add-In product. Earlier revisions of some EZ-KITs contained different hardware. These are not supported by the Yocto Linux product.


+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| Development Board                                                                                                                             | Supported Revision |
+===============================================================================================================================================+====================+
| :adi:`ADSP-SC598 EZ-KIT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EV-SC598-EZKIT.html>`                       | 1.0 Rev A or later |
+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| :adi:`ADSP-SC594 EZ-KIT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EV-SC594-EZKIT.html>`                       | 1.0 Rev B or later |
+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| :adi:`ADSP-SC589 EZ-KIT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADSP-SC589.html>`                      | 2.0 or later       |
+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| :adi:`ADSP-SC589-MINI <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sharc-audio-module.html>`                     | 1.5 or later       |
+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| :adi:`ADSP-SC584 EZ-KIT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADSP-SC584.html>`                      | 2.0 or later       |
+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| :adi:`ADSP-SC573 EZ-KIT <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/SC573EZKIT.html>`                           | 2.0 or later       |
+-----------------------------------------------------------------------------------------------------------------------------------------------+--------------------+

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

-  Post your questions in the software and development tools support community at :ez:`Analog Devices Engineer Zone <dsp/software-and-development-tools/linux-for-adsp-sc5xx-processors/f/q-a>` ®
-  E-mail your questions about processors and processor applications to processor.support@analog.com
-  Submit your questions to technical support directly via http://www.analog.com/support
-  Contact your Analog Devices sales office or authorized distributor

New Features And Changes
------------------------

The following changes have been applied since the 1.0 release of Yocto Linux for ADSP-SC5xx Processors.

-  U-Boot forked from upstream upgraded to 2020.10 LTS release
-  Linux kernel upgraded to 5.4.183 LTS release
-  Yocto upgraded to 3.1 (Dunfell) LTS release
-  Recommended host OS upgraded from Ubuntu 18.04 to 20.04 (Although both should work)
-  Switched from Busybox to SystemD for boot

| 
| ---- \**HOME PAGE: \*\* :doc:`Linux for ADSP-SC5xx Processors </wiki-migration/resources/tools-software/linuxdsp>`
