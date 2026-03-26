Software Packs & Board Support Package
======================================

.. note::

   There are no separate toolchain, On-Board Peripheral Drivers & Software for EV-COG-AD3029WZ; the toolchain, On-Board Peripheral Drivers & Software for EV-COG-AD3029LZ works with EV-COG-AD3029WZ. The user needs to change only the pin muxing based on the application. For help regarding pin mapping refer to the Hardware Details section.

A modular software framework is provided for quick application prototyping.
Based on the application use case, developers need to download the respective
software packs.

.. important::

   Please make sure you install either of the below toolchain before installing
   any of the below packs

   
   -  IAR Embedded Workbench for ARM 8.20.1 or higher
   -  CrossCore Embedded Studio 2.7.0 ® or higher

The Cog software development kit consists of these packs

-  :doc:`Analog Devices ADuCM302x Device Support Packs </solutions/reference-designs/ev-cog-ad3029wz/software/aducm302x>` - This is a bare minimum pack required to enable working with ADuCM3029 and develop simple applications using the on-chip drivers.

   -  *Version History*

      -  **Version: 3.1.0** - Extended support for IAR Embedded Workbench and Keil uVision. **[Latest]**

         -  Version: 2.0.0 - API Changes to suit IoT applications
         -  Version: 1.0.6 - Support Release
         -  Version: 1.0.5 - Enables ECC during flash programming

-  :doc:`Analog Devices EV-COG-AD3029WZ Off-Chip Drivers and Examples </solutions/reference-designs/ev-cog-ad3029wz/software/ev-cog-ad3029wz>` - This pack along with the DFP is required to develop applications using the on-board drivers.

   -  *Version History*

      -  **Version 3.1.0** - Extended support for IAR Embedded Workbench. **[Latest]**

         -  Version: 1.0.0 - Initial Release

-  `Analog Devices Sensor Drivers and Examples <https://wiki.analog.com/resources/eval/user-guides/ev-cog-ad3029lz/software/sensor>`_ - This pack is required only to develop applications using the GEARs.

   -  *Version History*

      -  **Version: 1.1.0** - Move example projects to respective board support packages. **[Latest]**

         -  Version: 1.0.0 - Initial Release

-  `Analog Devices Bluetooth Low Energy Software <https://wiki.analog.com/resources/eval/user-guides/ev-cog-ad3029lz/software/connectivity>`_ - This pack is required to enable BLE connectivity using EV-COG-BLEINTP1Z connectivity Cog.

   -  *Version History*

      -  **Version: 1.0.0** - Initial Release **[Latest]**

