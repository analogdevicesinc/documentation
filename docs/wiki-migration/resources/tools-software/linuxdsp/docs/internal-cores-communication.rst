.. warning::

   These pages are not updated anymore. Documentation has been moved to :git-lnxdsp-adi-meta:`wiki\`


Internal Cores Communication
============================

The Yocto Linux Product provides user space APIs that allow applications to easily communicate between individual cores of the ADSP-SC5xx processor.

Communication is performed using the Remote Processor Messaging Protocol (RPMsg) which defines an API and a semantics for communication and synchronization between processing cores in embedded systems. RPMsg is supported on ARM as part of Linux and as RPMsg-Lite on SHARC and ARM cores of the ADSP-SC5xx processors in both bare-metal and RTOS using CrossCore Embedded Studio.

ADSP-SC5xx is a series of products with multiple processor cores (two SHARC+ cores and an ARM® Cortex-A5 processor), this page provides some approaches to support the multi-core communication/control termed as the Internal Cores Communications (ICC) which contains the sections:

::

   ; **''RPMsg''**
   : [[/resources/tools-software/linuxdsp/docs/internal-cores-communication/rpmsg-lite|RPMsg-Lite]]
     ; **''RemoteProc''**
   : [[/resources/tools-software/linuxdsp/docs/internal-core-communication/remoteproc|Remoteproc]]
   ; **''ICAP''**
   : [[/resources/tools-software/linuxdsp/docs/internal-core-communication/icap|Inter Core Audio Protocol]]
