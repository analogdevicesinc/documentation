.. imported from: https://wiki.analog.com/resources/eval/user-guides/ev-cog-ad3029wz

.. _ev-cog-ad3029wz:

EV-COG-AD3029WZ Development Kit
===============================

The
:adi:`EV-COG-AD3029WZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EV-COG-AD3029.html>`
(referred also as MCU Cog) is a development platform based on the industry
leading ultra low power :adi:`ADuCM3029` 32-bit ARM Cortex™-M4F microcontroller.
The platform is designed to be a development and prototyping vehicle to get
customer ideas from concept to production with a minimal risk and faster time to
market.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/front_image_new.png
   :width: 550px

Applications using EV-COG-AD3029WZ board can be developed using one of the
following toolchains.

#. Crosscore Embedded Studio 2.7.0 and above - an Eclipse based Analog Devices
   Interactive Development Environment.
#. IAR Embedded Workbench for ARM 8.20 and above
#. Keil uVision 4 and above
#. ARM mbed Compiler

Make sure a valid license for the selected toolchain is installed before using
EV-COG-AD3029WZ board. **The software and power measurement is same for both
EV-COG-AD3029WZ and EV-COG-AD3029LZ**

#. :dokuwiki:`Introduction <ev-cog-ad3029wz/introduction>`

#.
   :dokuwiki:`Software Packs & Board Support Package <ev-cog-ad3029wz/packs_&_bsp>`:
   EV-COG-AD3029WZ software architecture is categorized into 4 groups as below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/drawing1-copy.png

::

   - [[resources:eval:user-guides:ev-cog-ad3029wz:software:aducm302x| Analog Devices ADuCM302x Device Support Pack]]
   - [[resources:eval:user-guides:ev-cog-ad3029wz:software:ev-cog-ad3029wz| Analog Devices EV-COG-AD3029WZ Off-Chip Drivers and Examples]]
   - [[resources:eval:user-guides:ev-cog-ad3029lz:software:sensor| Analog Devices Sensor Drivers and Examples]]
   - [[resources:eval:user-guides:ev-cog-ad3029lz:software:connectivity| Analog Devices Bluetooth Low Energy Software]]
- [[.:ev-cog-ad3029wz:quickstart_1|QuickStart Guide ]]
   -
     [[resources:eval:quickstart:ev-cog-ad3029wz:tools:cces_guide|EV-COG-AD3029WZ with CrossCore Embedded Studio ]]
   -
     [[resources:eval:user-guides:ev-cog-ad3029wz:tools:iar_guide|EV-COG-AD3029WZ with IAR Embedded Workbench for ARM]]
   -
     [[resources:eval:user-guides:ev-cog-ad3029wz:tools:other_ide|EV-COG-AD3029WZ Keil uVision IDE ]]

#. :dokuwiki:`Hardware Details <ev-cog-ad3029wz/hw_details>`

::

   - [[.:ev-cog-ad3029wz:Cog_HW_UserGuide| EV-COG-AD3029WZ MCU Cog ]]
           *[[.:ev-cog-ad3029lz: powermeasurement| Power Measurement on EV-COG-AD3029WZ MCU COG]]
- [[.:ev-cog-ad3029wz:tools_driver| Development Tools & Driver]]
   - [[resources:eval:user-guides:ev-cog-ad3029wz:tools:cces_download|CrossCore
     Embedded Studio Download & Install]]
         *[[resources:eval:user-guides:ev-cog-ad3029lz:tools:cces_guide|CrossCore Embedded Studio Quickstart Userguide]]
   - [[resources:eval:user-guides:ev-cog-ad3029lz:tools:hardware_usb|Driver
     installation for on-board debugger (CMSIS-DAP)]]
- [[.:ev-cog-ad4050w:example_project |Example Project ]]
- [[.:ev-cog-ad4050lz:help_support|Help & Support]]
