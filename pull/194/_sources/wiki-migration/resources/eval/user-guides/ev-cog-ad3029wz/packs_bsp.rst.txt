Software Packs & Board Support Package
======================================

<note > **There are no seperate toolchain,On-Board Peripheral Drivers & Software for EV-COG-AD3029WZ, the toolchain,On-Board Peripheral Drivers & Software for EV-COG-AD3029LZ works with EV-COG-AD3029WZ.The user needs to change only the pin muxing based on the application.For help regarding pinmapping refer to the Hardware Details section.** </WRAP>

A modular software framework is provided for quick application prototyping. Based on the application use case, developers need to download the respective software packs.

.. important::

   Please make sure you install either of the below toolchain before installing any of the below packs

   
   -  IAR Embedded Workbench for ARM 8.20.1 or higher
   -  CrossCore Embedded Studio 2.7.0 ® or higher
   
   packs


The Cog software development kit consists of these packs

-  :doc:`Analog Devices ADuCM302x Device Support Packs </wiki-migration/resources/eval/user-guides/ev-cog-ad3029wz/software/aducm302x>` - This is a bare minimum pack required to enable working with ADuCM3029 and develop simple applications using the on-chip drivers.

   -  *Version History*

      -  **Version: 3.1.0** - Extended support for IAR Embedded Workbench and Keil uVision. **[Latest]**

         -  Version: 2.0.0 - API Changes to suit IoT applications
         -  Version: 1.0.6 - Support Release
         -  Version: 1.0.5 - Enables ECC during flash programming

-  :doc:`Analog Devices EV-COG-AD3029WZ Off-Chip Drivers and Examples </wiki-migration/resources/eval/user-guides/ev-cog-ad3029wz/software/ev-cog-ad3029wz>` - This pack along with the DFP is required to develop applications using the on-board drivers.

   -  *Version History*

      -  **Version 3.1.0** - Extended support for IAR Embedded Workbench.\ **[Latest]**

         -  Version: 1.0.0 - Initial Release

-  :doc:`Analog Devices Sensor Drivers and Examples </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz/software/sensor>` - This pack is required only to develop applications using the GEARs.

   -  *Version History*

      -  **Version: 1.1.0** - Move example projects to respective board support packages. **[Latest]**

         -  Version: 1.0.0 - Initial Release

-  :doc:`Analog Devices Bluetooth Low Energy Software </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz/software/connectivity>` - This pack is required to enable BLE connectivity using EV-COG-BLEINTP1Z connectivity Cog.

   -  *Version History*

      -  **Version: 1.0.0** - Initial Release **[Latest]**

:doc:`Back </wiki-migration/resources/eval/user-guides/ev-cog-ad3029wz>`

*End of Document*
