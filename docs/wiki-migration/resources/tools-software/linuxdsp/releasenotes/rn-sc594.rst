Yocto Linux for ADSP-SC5xx Processors - Release for ADSP-SC594: Release Notes
=============================================================================

Introduction
------------

This release of Yocto Linux for ADSP-SC5xx Processors is a release specific to the ADSP-SC594 SOM board and ADSP-EZKIT Carrier board. This release **does not** support other ADSP-SC5xx processors that are supported by the 1.0 Release of Yocto Linux for ADSP-SC5xx Processors.

Future of this Release
----------------------

Once the other existing processors have been upgraded to the same versions of U-Boot, Linux and Yocto, this release will be merged and all processors will be supported under a single 2.0 release. At that point, support for this release will cease. All future maintenance for the ADSP-SC594 will then be incorporated into the main Yocto Linux Release.

Supported Linux Distributions
-----------------------------

The Yocto Linux for ADSP-SC5xx processors product is formally supported on **Ubuntu 20.04 LTS 64-bit**. While the product will likely build on other modern Linux distributions, ADI support for build issues will only be provided when using the supported Linux distribution.

Supported Processors and EZ-KITs
--------------------------------

The following processors and silicon revisions are supported by the Yocto Linux for ADSP-SC5xx product.

\* ADSP-SC594 SOM-EZ in combination with the ADSP-EZKIT-CRR Carrier Board

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

This is the first release of the Yocto Linux for ADSP-SC594 Processor. This is an intermediate release and it does not support any other processors. For existing supported processors please continue to use the 1.0 Release. The following changes have been applied since the 1.0 release of Yocto Linux for ADSP-SC5xx Processors.

-  U-Boot forked from upstream (Hurrah) upgraded to 2020.10 LTS release
-  Linux kernel upgraded to 5.4 LTS release
-  Yocto upgraded to 3.1 (Dunfell) LTS release
-  GCC upgraded to 9.3
-  Recommended host OS upgraded from Yocto 18.04 to 20.04 (Although both should work)
-  Switched from Busybox to SystemD for boot
-  Ethernet driver upgraded to support additional features

   -  EMAC driver supports hardware timestamping
   -  AF_XDP socket is supported
   -  adjtime syscall supported to adjust PTP and system clock
   -  qdisc command supported with Multiqueue priority Qdisc (MQPRIO), Credit based sharing Qdisc (CBS), Earliest TxTime First Qdisc (ETC)
   -  qdisc also supports the SO_PRIORITY socket option to enqueue network packets from userspace
   -  VLAN configurations are supported through the \*ip-link add-link\* command
   -  Ethernet driver supports PPS output for media clock recovery

-  Profiling support via oProfiler, Ftrace, Strace and perf

| 
| ---- \**HOME PAGE: \*\* :doc:`Linux for ADSP-SC5xx Processors </wiki-migration/resources/tools-software/linuxdsp>`
