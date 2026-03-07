Prerequisites for RapidNet IP
=============================

This document lists the steps required for successful installation of development environment, software packs and RapidNet IP source installer.

IAR EWARM - Installation
------------------------

-   Install IAR Embedded Workbench for ARM

   -  Please visit https://www.iar.com/ to download IAR Embedded Workbench for ARM (version 8.22.2 preferred)

-   License Installation

   -  Make sure valid license is installed for the corresponding version.

Software Packs and Driver - Installation
----------------------------------------

-  Following packs for ADuCM3029 can be downloaded directly from ARM website using IAR tool.

   -  ARM CMSIS Pack

      -  ADuCM302x_DFP (3.2.0) - Device Family Pack for ADuCM302x
      -  EV-COG-AD3029LZ_BSP - Board Support Pack for EV-COG-AD3029LZ

-  Start IAR Embedded Workbench for ARM.
-  Go to Project-> CMSIS-Pack-> Pack Installer.

|image1|

-  In **'CMSIS Pack Manager'** window, click 'Search for updates'.

|image2|

-  After search is complete, expand 'ARM' and 'CMSIS' under ARM. Right click on the latest version and select install from drop down options.
-  After successful installation of ARM CMSIS pack, expand 'AnalaogDevices', then expand 'ADuCM302x_DFP'. Right click on **'3.2.0'** and click install drop down options.
-  After successful installation of ADuCM302x_DFP, expand 'AnalaogDevices', then expand EV-COG-AD3029LZ_BSP'. Right click on **'3.1.0'** and click install drop down options.
-  Restart IAR after successful installation of all the packs.

RapidNet IP Source Installer - Download and Installation
--------------------------------------------------------

Below steps will guide how to download the RapidNet IP Source Installer.

-  Click www.analog.com/SRF to go to Analog devices software request form, to request the source installer.
-  Fill required details.
-  Under 'Target Hardware', select 'Ultra Low Power Microcontroller'
-  Under 'Software requested' section, check 'RapidNet IP'.
-  Click 'SUBMIT' button available at the bottom of the page.
-  An e-mail notification with a download link will be sent.

Import RapidNet IP Example Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Power the using a USB (micro-B) Cable. You should see a red LED and a yellow LED turn on by default.
-  Start IAR Embedded Workbench for ARM.
-  Go to File-> Open Workspace...
-  Navigate to the RapidNet IP installation directory in Open Workspace. By default it will be installed at C:\\Analog Devices\\RapidNet-IP-Rel1.1.0.
-  In 'Open Workspace' window go to Mote->application->esl->IAR.
-  Select 'esl_lib.eww' and click open.
-  Once the workspace is open, make sure 'esl_app' is select in the 'Workspace' tab (left side). If not, select it from the bottom of the 'Workspace' tab.

|image3|

-  Right click on 'esl_app - Debug' on Workspace Tab and select 'Options...'.
-  Go to Debugger->Setup and under 'Driver' drop down menu select 'CMSIS DAP'.\

|image4|

-  Click on 'Debug and Download' icon |image5|\ on the menu bar. This will compile, build and download the project on EV-COG-AD3029LZ using CMSIS-DAP.

mBed windows serial driver - Installation
-----------------------------------------

Install mBed windows serial driver from https://developer.mbed.org/handbook/Windows-serial-configuration

You are all set!

:doc:`Back </wiki-migration/resources/eval/user-guides/rapidnet-ip>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/cmsis_pack_install_1.png
   :width: 750px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/2.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/3.png
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/rapidnet-ip/4.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/quickstart_guide/iar/debug_debug_button.png
