FreeRTOS Release History
========================

Support and Assistance
----------------------

For documentation about FreeRTOS, please visit the FreeRTOS website where extensive documentation on the operating system can be found at http://www.freertos.org/FreeRTOS-quick-start-guide.html For questions regarding the examples provided in this product please post questions in the FreeRTOS community in Engineer Zone at :ez:`community/dsp/software-and-development-tools/freertos`

Use of System Services and Device Driver libraries with FreeRTOS
----------------------------------------------------------------

As of the 1.3.0 release of the Analog Devices FreeRTOS product the pre-built versions of the System Services and Devices Driver libraries are no longer compatible with FreeRTOS for the ADSP-21569, ADSP-SC5xx and Blackfin BF7xx platforms. In order to use the System Services and Device Drivers the project must include the source versions of these libraries rather than linking against the pre-built versions of the libraries. For more information on configuring FreeRTOS projects for use with System Services and Device Drivers please refer to the Using CrossCore Embedded Studio System Services and Device Drivers with FreeRTOS section of the FreeRTOS User Guide.

Version 2.1.0
~~~~~~~~~~~~~

Supported Parts
---------------

-  ADSP-BF7xx
-  ADSP-SC5xx (SHARC+)
-  ADSP-SC5xx (Cortex-A5)
-  ADSP-SC5xx (Cortex-A55)
-  ADSP-SC8xx (SHARC-FX)
-  ADSP-SC8xx (Cortex-M33)
-  ADSP-215xx

New Features
------------

-  Upgraded FreeRTOS from 10.4.3-LTS2 to 10.5.1 (LTS)
-  Add support for Cortex-M33 and SHARC-FX cores for ADSP-SC8xx and ADSP-218xx

   -  Cortex-M33 needs an external DFP for OSAL support available from :doc:`/wiki-migration/resources/tools-software/freertos/osal-dfp`

Changes
-------

-  SHARC+ asm sources now include FreeRTOSConfig.h, so changes may be required in your FreeRTOSConfig.h to be asm safe by macro guarding with:

::

   #if !defined(_LANGUAGE_ASM)

Compatibility
-------------

This FreeRTOS product is a standalone product containing FreeRTOS 10.4.3-LTS2. No additional FreeRTOS product needs to be used. CrossCore Embedded Studio version 2.10.0 or later is required.

Version 2.0.0
~~~~~~~~~~~~~

.. _supported-parts-1:

Supported Parts
---------------

-  ADSP-BF7xx
-  ADSP-SC5xx (SHARC+)
-  ADSP-SC5xx (Cortex-A5)
-  ADSP-SC5xx (Cortex-A55)
-  ADSP-215xx

.. _new-features-1:

New Features
------------

-  Upgraded FreeRTOS from 10.0.0 to 10.4.3-LTS2
-  Add support for Cortex-A55 on ADSP-SC59x

.. _changes-1:

Changes
-------

-  FreeRTOS sources are included so no overlay is required

.. _compatibility-1:

Compatibility
-------------

This FreeRTOS product is a standalone product containing FreeRTOS 10.4.3-LTS2. No additional FreeRTOS product needs to be used. CrossCore Embedded Studio version 2.10.0 or later is required.

Version 1.5.0
~~~~~~~~~~~~~

.. _supported-parts-2:

Supported Parts
---------------

-  ADSP-BF7xx
-  ADSP-SC5xx (SHARC+)
-  ADSP-SC5xx (Cortex-A5)
-  ADSP-215xx

.. _new-features-2:

New Features
------------

-  Support for ADSP-SC594 (ARM and SHARC+ Core) processor added

.. _changes-2:

Changes
-------

-  ADuCM3/4\* support has been removed from this product

.. _compatibility-2:

Compatibility
-------------

This FreeRTOS product is intended to be used in conjunction with version 10.0.0 of the FreeRTOS product as provided for free at FreeRTOS.org. This product was tested using version 10.0.0 of FreeRTOS and we strongly recommend that you use this version of the operating system. CrossCore Embedded Studio version 2.10.0 or later is required.

Version 1.4.0
~~~~~~~~~~~~~

.. _supported-parts-3:

Supported Parts
---------------

-  ADSP-BF7xx
-  ADSP-SC5xx (SHARC+)
-  ADSP-SC5xx (Cortex-A5)
-  ADSP-215xx
-  ADuCM302x
-  ADuCM4x50

.. _new-features-3:

New Features
------------

-  Support for ADSP-2156x (SHARC+ Core) processor added

.. _changes-3:

Changes
-------

-  LwIP examples removed due to incompatability between LwIP 2.6.0 and CCES 2.9.0.

.. _compatibility-3:

Compatibility
-------------

This FreeRTOS product is intended to be used in conjunction with version 10.0.0 of the FreeRTOS product as provided for free at FreeRTOS.org. This product was tested using version 10.0.0 of FreeRTOS and we strongly recommend that you use this version of the operating system. CrossCore Embedded Studio version 2.9.0 or later is required. ADuCM parts require IAR 5.2.1.a or Keil 7.60.1 or later.

Version 1.3.1
~~~~~~~~~~~~~

.. _supported-parts-4:

Supported Parts
---------------

-  ADSP-BF7xx
-  ADSP-SC5xx (SHARC+)
-  ADSP-SC5xx (Cortex-A5)
-  ADSP-215xx
-  ADuCM302x
-  ADuCM4x50

.. _new-features-4:

New Features
------------

-  Introduced complete support for the Cortex-A5 core of the ADSP-SC5xx processor family.
-  Fix issues related to use of System Service and Device Drivers with ADSP-SC5xx and ADSP-BF7xx processors
-  Support for UART based I/O for ADSP-SC5xx Cortex-A core FreeRTOS

.. _changes-4:

Changes
-------

This release contains support for UART based I/O when using FreeRTOS on the ADSP-SC5xx Cortex-A5 core. This changes the method of I/O used for this processor core and care should be taken to understand this change when upgrading existing projects.

.. _compatibility-4:

Compatibility
-------------

This FreeRTOS product is intended to be used in conjunction with version 10.0.0 of the FreeRTOS product as provided for free at FreeRTOS.org. This product was tested using version 10.0.0 of FreeRTOS and we strongly recommend that you use this version of the operating system. CrossCore Embedded Studio version 2.8.3 or later is required. ADuCM parts require IAR 5.2.1.a or Keil 7.60.1 or later.

Version 1.3.0
~~~~~~~~~~~~~

.. _supported-parts-5:

Supported Parts
---------------

-  ADSP-BF7xx
-  ADSP-SC5xx (SHARC+ Beta)
-  ADSP-SC5xx (Cortex-A5 Beta)
-  ADSP-215xx
-  ADuCM302x
-  ADuCM4x50

.. _new-features-5:

New Features
------------

-  Upgraded from FreeRTOS 9.0.0 to FreeRTOS 10.0.0.
-  Beta support for ADSP-SC5xx (SHARC+ and Cortex-A5 cores)
-  LwIP example for Cortex-A5

While this port is functionally complete, it is considered a beta release due to an issue with performance when host based I/O is enabled in an application debug session (see known issues below for more details). This issue will be addressed in a future version of the FreeRTOS product from Analog Devices.

.. _compatibility-5:

Compatibility
-------------

This FreeRTOS product is intended to be used in conjunction with version 10.0.0 of the FreeRTOS product as provided for free at FreeRTOS.org. This product was tested using version 10.0.0 of FreeRTOS and we strongly recommend that you use this version of the operating system. CrossCore Embedded Studio version 2.8.0 or later is required. ADuCM parts require IAR 5.2.1.a or Keil 7.60.1 or later.

Known Issues
------------

-  FreeRTOS and CrossCore Embedded Studio conflict on use of SVC interrupt (Cortex-A5 only)
-  The current implementation of FreeRTOS for ADSP-SC5xx (Cortex-A5 Core) relies on the SVC interrupt to perform context switching within the RTOS.

::

    However the runtime libraries the ADSP-SC5xx ARM core, provided with CrossCore Embedded Studio, also use the SVC interrupt to perform I/O operations with the host (printf etc).
    The result of this is that the emulator latches on to each SVC instruction issued by the target processor and this results in a significant slow down for applications running under the emulator.
    To work around this issue users should disable semihosting within the CrossCore Embedded Studio debug session. This will improve the performance of the application under the emulator.
    Please note that this will disable all target-to-host I/O operations. Calls to functions such as printf, fopen etc should either be comments out, or the low level I/O device should be replaced to use an alternative, such as UART.
    To disable semihosting within CrossCore Embedded Studio:
     * Within the CrossCore Embedded Studio debug session launch the Debug Configurations Manager
     * Select the debug configuration from the left pane in the Debug Configurations Manager
     * Click the Automatic Breakpoints tab in the main window of the Debug Configurations Manager
     * Uncheck the Enable semihosting checkbox at the bottom of the window Click the Debug button to debug your application
   * Restrictions on size of semaphore where using FreeRTOS with CrossCore Embedded Studio OSAL. ADSP-SC5xx and ADSP-BF7xx ports, only
    Both configUSE_TRACE_FACILITY and configUSE_QUEUE_SETS increase the size of static semaphores in FreeRTOS, when set to 1.
    Using both together increases the size beyond the amount of space reserved by OSAL for its static semaphores, which may cause certain device-driver and service API calls to fail. This will prevent the setup of soft-switches, amongst other things.
    The recommended workaround is to set configUSE_TRACE_FACILITY to 0 in all projects, since it is not required for normal program operation. This only applies to platforms that use OSAL, i.e. Blackfin and 215xx.

Version 1.2.0
~~~~~~~~~~~~~

.. _supported-parts-6:

Supported Parts
---------------

-  ADSP-BF7xx
-  ADSP-SC5xx (Cortex-A5 Beta)
-  ADSP-215xx
-  ADuCM302x
-  ADuCM4x50

.. _compatibility-6:

Compatibility
-------------

This FreeRTOS product is intended to be used in conjunction with version 9.0.0 of the FreeRTOS product as provided for free at FreeRTOS.org. This product was tested using version 10.0.0 of FreeRTOS and we strongly recommend that you use this version of the operating system. CrossCore Embedded Studio version 2.6.0 or later is required. ADuCM parts require IAR 5.2.1.a or Keil 7.60.1 or later.

.. _known-issues-1:

Known Issues
------------

\* FreeRTOS and CrossCore Embedded Studio conflict on use of SVC interrupt (Cortex-A5 only) \* The current implementation of FreeRTOS for ADSP-SC5xx (Cortex-A5 Core) relies on the SVC interrupt to perform context switching within the RTOS.

::

    However the runtime libraries the ADSP-SC5xx ARM core, provided with CrossCore Embedded Studio, also use the SVC interrupt to perform I/O operations with the host (printf etc).
    The result of this is that the emulator latches on to each SVC instruction issued by the target processor and this results in a significant slow down for applications running under the emulator.
    To work around this issue users should disable semihosting within the CrossCore Embedded Studio debug session. This will improve the performance of the application under the emulator.
    Please note that this will disable all target-to-host I/O operations. Calls to functions such as printf, fopen etc should either be comments out, or the low level I/O device should be replaced to use an alternative, such as UART.
    To disable semihosting within CrossCore Embedded Studio:
     * Within the CrossCore Embedded Studio debug session launch the Debug Configurations Manager
     * Select the debug configuration from the left pane in the Debug Configurations Manager
     * Click the Automatic Breakpoints tab in the main window of the Debug Configurations Manager
     * Uncheck the Enable semihosting checkbox at the bottom of the window Click the Debug button to debug your application
   * Restrictions on size of semaphore where using FreeRTOS with CrossCore Embedded Studio OSAL. ADSP-SC5xx and ADSP-BF7xx ports, only
    Both configUSE_TRACE_FACILITY and configUSE_QUEUE_SETS increase the size of static semaphores in FreeRTOS, when set to 1.
    Using both together increases the size beyond the amount of space reserved by OSAL for its static semaphores, which may cause certain device-driver and service API calls to fail. This will prevent the setup of soft-switches, amongst other things.
    The recommended workaround is to set configUSE_TRACE_FACILITY to 0 in all projects, since it is not required for normal program operation. This only applies to platforms that use OSAL, i.e. Blackfin and 215xx.

Version 1.1.0
~~~~~~~~~~~~~

.. _supported-parts-7:

Supported Parts
---------------

-  ADuCM302x
-  ADuCM4x50

.. _compatibility-7:

Compatibility
-------------

This FreeRTOS product is intended to be used in conjunction with version 9.0.0 of the FreeRTOS product as provided for free at FreeRTOS.org. This product was tested using version 9.0.0 of FreeRTOS and we strongly recommend that you use this version of the operating system. ADuCM parts require IAR 5.2.1.a or Keil 7.60.1 or later.
