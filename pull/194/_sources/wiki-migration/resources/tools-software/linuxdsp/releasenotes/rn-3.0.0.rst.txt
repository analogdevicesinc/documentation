Yocto Linux for ADSP-SC5xx Processors - Release 3.0.0: Release Notes
====================================================================

Introduction
------------

This release contains an upgrade of both the kernel and the build system to a recent LTS release. It also enriches and enhances the choice regarding LDR firmware loading and generally handling the audio and SHARC firmware.

Another notable addition is the ability to boot from flash on SC573 & SC58x boards. Several more features and changes are noted in detail on the following section.

For more information on testing, see :doc:`the test report for this release </wiki-migration/resources/tools-software/linuxdsp/docs/testing/release3.0.0>`

New Features And Changes
------------------------

The following changes have been applied since the 1.0 release of Yocto Linux for ADSP-SC5xx Processors.

-  Linux kernel upgraded to 5.15.78 LTS release
-  Yocto upgraded to 4.0.1 (Kirkstone) LTS release
-  Sound-related LDR firmware options:

   -  ``linux_only_audio`` (default): Audio is handled entirely through Linux drivers and no SHARC firmware is needed. ramdisk includes ``rpmsg-echo-example`` package. This installs ``echo_core1-{MACHINE}.ldr'' to ''/lib/firmware/adi_adsp_core1_fw.ldr'' and ''echo_core2-{MACHINE}.ldr`` to ``/lib/firmware/adi_adsp_core2_fw.ldr``
   -  ``adi_sharc_alsa_audio`` (supported on: SC598): Audio playback handled through SHARC firmware, no codec control (volume, etc) from Linux. Remoteproc is used to load the SHARC LDR firmware files. This installs ``icap-sharc-alsa_Core1.ldr`` to ``/lib/firmware/adi_adsp_core1_fw.ldr`` and ``icap-sharc-alsa_Core2.ldr`` to ``/lib/firmware/adi_adsp_core2_fw.ldr``
   -  ``adi_sharc_alsa_audio_uboot``: Audio playback handled through SHARC firmware, no codec control (volume, etc) from Linux. Remoteproc is not used to load the SHARC LDR firmware files ramdisk does not include any LDR firmware files. These must be loaded from U-Boot prior to booting Linux
   -  ``adi_hybrid_audio``: Audio playback handled through SHARC firmware, codec control (volume, etc) is still available from Linux, ramdisk includes hybrid-audio package. This installs ``icap-device-example_Core1.ldr`` to ``/lib/firmware/adi_adsp_core1_fw.ldr``

-  Added new ``adsp-sc5xx-tiny`` image (<16 MB) to enable ADSP-SC573 & ADSP-SC58x boards to be able to boot from SPI Flash :doc:`to enable ADSP-SC573 & ADSP-SC58\* boards to be able to boot from SPI Flash </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/boot-flash-sc58x-573>`
-  Added new boot methods: SD Card & USB Mass Storage for some of the supported boards:

   -  SD Card Boot:

      -  ADSP-SC598 EZ-KIT
      -  ADSP-SC589 EZ-KIT
      -  ADSP-SC589-MINI

   -  USB Mass Storage Boot:

      -  ADSP-SC598 EZ-KIT
      -  ADSP-SC594 EZ-KIT
      -  ADSP-SC589-MINI
      -  ADSP-SC589 EZ-KIT

-  Added USB Audio Class 2.0 support and :doc:`example </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/device_mode/gadget_audio_3_0_0>`
-  Added Packet Engine Driver (PKTE) for ADSP-SC598 EZ-KIT. The supported algorithms are: ``adi-ecb-des3``, ``adi-ecb-des``, ``adi-ecb-aes``, ``adi-cbc-des3``, ``adi-cbc-des``, ``adi-cbc-aes``, ``adi-hmac-sha256``, ``adi-sha256``, ``adi-hmac-sha224``, ``adi-sha224``, ``adi-hmac-sha1``, ``adi-sha1``, ``adi-hmac-md5`` and ``adi-md5``
-  Added `U-Boot Falcon Mode <https://github.com/u-boot/u-boot/blob/master/doc/README.falcon>`_ support for SC59x and :doc:`example </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/u-boot-falcon-mode>`

| 

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

Frequently Asked Questions
--------------------------

*Q: Why is ``/usr/sbin/rngd`` has a very high CPU utilisation for some time after booting up SC59x?*

A: This is due to the jitter entropy source (software-based) that was added in rng-tools version 6. The initialization of it takes quite some time on smaller ARMs. There is a patch that fixes that, by moving the entropy generation sources so that hardware RNG is always used (through ``/dev/hwrng``). You can apply that from the develop/3.1.0 branch `Placeholder link <https://github.com>`_

Known Issues
------------

The following issues have been identified in this release but have not been assessed yet:

-  SC589-mini: When attempting to save the U-Boot environment, it fails with the following message: ``Erasing SPI flash...failed (-22)``. This means that it is not possible to make any persistent changes to the U-Boot environment, such as IP addresses.

Obtaining Technical Support
---------------------------

You can reach Analog Devices software and tools technical support in the following ways:

-  Post your questions in the software and development tools support community at :ez:`Analog Devices Engineer Zone <dsp/software-and-development-tools/linux-for-adsp-sc5xx-processors/f/q-a>` ®
-  E-mail your questions about processors and processor applications to processor.support@analog.com
-  Submit your questions to technical support directly via http://www.analog.com/support
-  Contact your Analog Devices sales office or authorized distributor

--------------

\**HOME PAGE: \*\* :doc:`Linux for ADSP-SC5xx Processors </wiki-migration/resources/tools-software/linuxdsp>`
