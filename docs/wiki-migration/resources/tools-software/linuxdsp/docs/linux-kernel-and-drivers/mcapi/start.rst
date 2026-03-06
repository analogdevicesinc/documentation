Multi-Core Communication
========================

The Yocto Linux Product provides user space APIs that allow applications to easily communicate with the SHARC cores of the ADSP-SC5xx processor.

Communication is performed using the Multi-core Communications API (MCAPI) specification which defines an API and a semantics for communication and synchronization between processing cores in embedded systems. MCAPI is supported on the SHARC cores of the ADSP-SC5xx processors in both bare-metal and RTOS using CrossCore Embedded Studio. For more information about MCAPI, please refer to the MCAPI Specification document from MCAPI.org.

ADSP-SC5xx is a series of products with multiple processor cores (two SHARC+ cores and an ARM® Cortex-A5 processor), this page provides some approaches to support the multi-core communication/control termed as the Internal Cores Communications (ICC) which contains the sections:

::

   ; **''Core Control''**
   : [[/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/mcapi/control_sharc_cores|Enable and Disable SHARC Cores]]
     ; **''RemoteProc''**
   : [[/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/remoteproc/remoteproc|Remoteproc]]
   : [[/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/mcapi/sec_driver_and_multicore_development|SEC driver and multicore development]]

::

   ; **''MCAPI''**
   : [[/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/mcapi/mcapi_introduction|Introduction of MCAPI examples]]
   : [[/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/mcapi/mcapi_example|Run Linux on ARM and bare-metal application on SHARC]] 
   : [[/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/mcapi/mcapi_api|MCAPI Supported Functions]]

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
