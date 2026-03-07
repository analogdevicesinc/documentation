Introduction
============

Analog Devices FreeRTOS
-----------------------

The Analog Devices FreeRTOS product is a modified version of the FreeRTOS Kernel, providing support for the Analog Devices Blackfin (BF70x), SHARC+ (ADSP-215xx/ADSP-SC5xx) and SHARC-FX (ADSP-218xx/ADSP-SC8xx) DSP families. It is stand-alone set of sources based on version 10.5.1 of the FreeRTOS operating system.

:doc:`Initial setup documentation and User Guides </wiki-migration/resources/tools-software/freertos/rtos-user-guide>` have been created to help users get started with using FreeRTOS with CrossCore Embedded Studio.

:doc:`Release notes </wiki-migration/resources/tools-software/freertos/release-notes>` provide details on what's changed between releases and any compatability concerns.

--------------

Analog Devices FreeRTOS Add-In
------------------------------

The **FreeRTOS Add-In** has been developed by **Analog Devices** using CrossCore Embedded Studio to make it easier to add FreeRTOS into CrossCore projects, configure and debug FreeRTOS.

The **FreeRTOS Add-In**, once added to your project, will clone the required FreeRTOS source files from a repository hosted by **Analog Devices** into your project, this will be dependent on the architecture of the processor, and do all of the necessary steps to allow the project to build correctly out of the box, this includes

-  setting up the proper include paths
-  definition of required pre-processor macros
-  downloading related :doc:`FreeRTOS source files </wiki-migration/resources/tools-software/freertos/freertos-addin/freertos-repo>`
-  generation of editable and non editable :doc:`FreeRTOS Add-In files </wiki-migration/resources/tools-software/freertos/freertos-addin/generated-files>`
-  creation of a new UI element added to the system.svc, which is used to configure the **FreeRTOS**

:doc:`Installation details and documentation </wiki-migration/resources/tools-software/freertos/freertos-addin>` have been created for the FreeRTOS Add-In to help users get started.
