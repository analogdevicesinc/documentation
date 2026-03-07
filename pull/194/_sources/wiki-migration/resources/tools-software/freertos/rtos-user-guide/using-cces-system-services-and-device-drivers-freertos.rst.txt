Using CrossCore Embedded Studio System Services and Device Drivers with FreeRTOS
================================================================================

Note:This section of the document applies to the ADSP-SC5xx (Cortex-A and SHARC+) and ADSPBF7xx processors.

CrossCore Embedded Studio provides support for the on-chip peripherals and EZ-KIT hosted device drivers that are provided for its processors.

In order to use these features with FreeRTOS the source based versions of the drivers must be used rather than the default pre-built libraries that are provided.

.. note::

   Use of the library based version of the System Services and Device Drivers is not compatible with FreeRTOS. Use of the pre-built libraries may result in run-time corruption and execution failure.


To use the System Services and Device Drivers in your CrossCore Embedded Studio project:

-  Ensure that the pre-processor macro \__ADI_FREERTOS is defined for all assembler,C/C++ and linker operations. This requires the pre-processor macro to defined in three separate locations in the project settings.
-  Ensure that the pre-built libdrv library is not linked into the application.

   -  For Cortex-A projects this is controlled by adding the following option to the Settings >Tool Settings > CrossCore

      -  ARM Bare Metal C Linker > Additional Options settings: - specs=PATH_TO_FREERTOS\\FreeRTOS\\FreeRTOSv10.0.0\\FreeRTOSSource\\portable\\CCES\\ARM_CA5\\freertos.specs where PATH_TO_FREERTOS is replaced with the path to the installation of your FreeRTOS product.
      -  For SHARC+ and Blackfin projects this is controlled by checking the Settings > Tool Settings > CrossCore Blackfin/SHARC Linker > Libraries > Omit device driver library checkbox

-  Enable the source based version of the required services and drivers:

   -  Double click the system.svc file in the Project Explorer

      -  Click the Add button in the System Configuration Overview
      -  Browse the list of Device Drivers and System Services to add new components to the project

-  Build the project

.. note::

   The provided demo examples for the EZ-KITs contain all the appropriate project settings already configured and are an easy way to get started with a new FreeRTOS project

