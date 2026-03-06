:doc:`Click here to return to A2B Analyzer Studio Homepage. </wiki-migration/resources/tools-software/a2b-analyzer-studio>`

A2B Analyzer Studio Quick Start Guide
=====================================

Introduction
============

The guidelines on these pages are intended to help A\ :sup:`2`\ B users configure and use the ADI A\ :sup:`2`\ B Analyzer Studio tool in Monitor or Emulator mode for A2B1.0 networks on A2B Bus Analyzer and A2B2.0 networks on A2B Analyzer HP respectively. 

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_1.png
   :width: 600px

Installation and Upgrades
=========================

Supported Operating Systems
---------------------------

A\ :sup:`2`\ B Analyzer Studio runs on Windows, Linux, and macOS. The Operating Systems table describes the operating system versions supported currently. 

+-------------------+---------------------------------------------------------------------------------------------+
| **Platform**      | **Details**                                                                                 |
+===================+=============================================================================================+
| |image4| macOS    | 14.x (Sonoma or) later on ARM.                                                              |
|                   | **Note**: macOS x64 platforms are not supported. Only ARM-based macOS systems are supported |
+-------------------+---------------------------------------------------------------------------------------------+
|  |image5| Linux   | Ubuntu 22.04+ (64-bit)                                                                      |
+-------------------+---------------------------------------------------------------------------------------------+
|  |image6| Windows | Windows 10 and 11 Home, Pro, Enterprise (64-bit)                                            |
+-------------------+---------------------------------------------------------------------------------------------+

Software Installation Instructions
----------------------------------

The following sub-sections include installation information for the supported Operating Systems. 

Windows
~~~~~~~

-  To install A\ :sup:`2`\ B Analyzer Studio, double-click on a2b_analyzer_studio-vX.Y.Z_win32.exe.
-  A\ :sup:`2`\ B Analyzer Studio is installed in the following default location: C:\\Analog Devices\\A2B Analyzer Studio.
-  To uninstall A\ :sup:`2`\ B Analyzer Studio, go to the Programs and Features applet in the Control Panel.

Linux
~~~~~

-  To install A\ :sup:`2`\ B Analyzer Studio, download the .AppImage. Copy the file into a directory such as ~/Applications
-  If required, ensure that file has execute permissions by running chmod a+x a2b_analyzer_studio\_\*.AppImage
-  Launch A\ :sup:`2`\ B Analyzer Studio by running ./a2b_analyzer_studio-vX.Y.Z_linux_x86_64_linux.AppImage
-  Simply delete the .AppImage file to uninstall A\ :sup:`2`\ B Analyzer Studio.

**Note:** By default a USB device is only accessible if the A\ :sup:`2`\ B Bus Analyzer is run with sudo. The **Linux USB Configuration Script** configures a USB device to be accessible by the currently logged-in user.

::

   #!/bin/sh
    
   # The following is an example script of how to configure your USB on Linux
   # to be accessible by other users.
    
   if [ $(id -u) != 0 ]; then
       echo "You must run this script with sudo:"
       echo "sudo $0 $*"; exit 1
   fi
   adirules=/etc/udev/rules.d/adi.rules
   # Customize the group name that can access your USB device(s)
   adigroup=adiusb
   echo "Creating '"$adirules"' ..."
   echo ATTRS{idVendor}==\"064b\", GROUP=\"$adigroup\" > $adirules
   echo ATTRS{idVendor}==\"0d28\", ATTRS{idProduct}==\"0204\", GROUP=\"$adigroup\" >> $adirules
   echo "Done."
   if [ -z $(getent group $adigroup) ]; then
       addgroup $adigroup
   fi
   echo "Adding user '"$SUDO_USER"' to group '"$adigroup"' ..."
   usermod -a -G $adigroup $SUDO_USER
   echo "Done."
   echo "Restarting '/etc/init.d/udev' ..." /etc/init.d/udev restart
   echo "Done."
   lsusb | grep "ID 064b"
   echo "===================================================================="
   echo "You must restart your computer for these settings to take effect."
   echo "" echo "If you wish to remove ADI device permissions:"
   echo "sudo groupdel" $adigroup
   echo "sudo rm" $adirules
   echo "===================================================================="

macOS
~~~~~

-  To install A\ :sup:`2`\ B Bus Analyzer double-click on a2b_analyzer_studio-vX.Y.Z-macos-arm64.pkg
-  Right-click on the Installer .pkg and select Open with... or Installer if the Installation Wizard does not appear.
-  A\ :sup:`2`\ B Analyzer Studio is installed in /Applications.
-  To uninstall A\ *2*\ B Analyzer Studio, find the application in your install location, right click it and click "Move to Bin". 

Software Upgrades
-----------------

Updating the A2B Analyzer Studio Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The upgrade process is the same for all supported operating systems.

Run A\ :sup:`2`\ B Analyzer Studio, visit the Home screen, click 'Check for Updates'. If a newer version is available 'Download' and then 'Restart to Install' to update your copy of A\ :sup:`2`\ B Analyzer Studio.

You can also use the Help \| Check for Updates... menu item to find out if there are any new updates available.

| A\ :sup:`2`\ B Analyzer Studio software updates preserve the settings from the previous version installed.
| |image7|

Updating the Firmware for A2B Bus Analyzer or A2B Analyzer HP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current firmware version on the device is shown on the Home screen after connecting to an A\ :sup:`2`\ B Bus Analyzer or A\ :sup:`2`\ B Analyzer HP device.

If a firmware update is available, click 'Update Firmware' and follow the on-screen instructions to flash the new version to the connected device (A\ :sup:`2`\ B Bus Analyzer or A\ :sup:`2`\ B Analyzer HP).

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_3.png
   :width: 600px

A2B Analyzer HP Package Contents
================================

+-------------+------------------------------------------------------------------------+--------------+
| **Sl. No.** | **Content**                                                            | **Quantity** |
+=============+========================================================================+==============+
| 1           | A\ :sup:`2`\ B Analyzer HP HW Unit with 2 ADAA245x personality modules | 1            |
+-------------+------------------------------------------------------------------------+--------------+
| 2           | USB Type C to USB Type C cable                                         | 1            |
+-------------+------------------------------------------------------------------------+--------------+
| 3           | 24V power supply cable + adapter                                       | 1            |
+-------------+------------------------------------------------------------------------+--------------+
| 4           | A\ :sup:`2`\ B Cable with MINI50-MINI50 to MINI50-MINI50 connectors    | 4            |
+-------------+------------------------------------------------------------------------+--------------+
| 6           | A\ :sup:`2`\ B Analyzer Studio Application download instructions       | 1            |
+-------------+------------------------------------------------------------------------+--------------+

A2B Bus Analyzer Package Contents
=================================

+-------------+-----------------------------------------------------------+--------------+
| **Sl. No.** | **Content**                                               | **Quantity** |
+=============+===========================================================+==============+
| 1           | A\ :sup:`2`\ B Bus Analyzer HW Unit                       | 1            |
+-------------+-----------------------------------------------------------+--------------+
| 2           | USB-A to Micro-B cable                                    | 1            |
+-------------+-----------------------------------------------------------+--------------+
| 3           | USB Type C cable + adapter                                | 1            |
+-------------+-----------------------------------------------------------+--------------+
| 4           | 12V power supply cable + adapter                          | 1            |
+-------------+-----------------------------------------------------------+--------------+
| 5           | A\ :sup:`2`\ B Cable with HDAC to Duraclik connectors     | 1            |
+-------------+-----------------------------------------------------------+--------------+
| 6           | A\ :sup:`2`\ B Cable with HDAC to HDAC connectors         | 2            |
+-------------+-----------------------------------------------------------+--------------+
| 7           | A\ :sup:`2`\ B Cable with Duraclik connectors             | 2            |
+-------------+-----------------------------------------------------------+--------------+
| 8           | A\ :sup:`2`\ B Analyzer Application download instructions | 1            |
+-------------+-----------------------------------------------------------+--------------+

-  The physical dimension of A2B Bus Analyzer box is **15.25" x 9.5" x 4.125".**
-  The A2B Bus Analyzer box alone weighs about **533 g. **\ The entire box (including connectors and power supply) may weigh ~ 1kg.

Getting Started with A2B Analyzer HP or A2B Bus Analyzer
========================================================

Using A2B Analyzer HP as Bus Monitor
------------------------------------

1. To configure the device as a monitor follow the instructions in :doc:`A2B Bus Analyzer and A2B Analyzer HP Hardware Setup </wiki-migration/resources/tools-software/a2b-analyzer-studio/a2b-analyzer-hardware-setup>`.

| 2. Launch the A\ :sup:`2`\ B Analyzer Studio and create a new project or open an existing project using the links on the Welcome panel.
| |image8|

| 3. In the New Project tab, choose analyzer as A\ :sup:`2`\ B Analyzer HP and select the features you want to enable.
| |image9|

| 4. Switch to Monitor PM2 view using the link in the side panel.
| |image10|

| 5. The transceiver is selected from the personality module connected to the board
| |image11|

| 6. Provide json file for the ADAA24xx network. This is required to know the position of the traffic within the A2B super frame. JSON file can be exported from SigmaStudio+ schematic.
| |image12|

| 7. Select the position of the bus monitor in the network and then activate bus monitoring by clicking **Start** .
| |image13|

| 8. Now you are ready to start capturing audio and event traffic on the bus.
| |image14|

**Note: **\ Event and Audio Traffic area will remain blank until the network host initiates A\ :sup:`2`\ B discovery. 9. Switch to the A\ :sup:`2`\ B network host program (e.g., SigmaStudio+, Head-unit software) and initiate discovery process.

| 10. With network discovery initiated on the host, the A\ :sup:`2`\ B Analyzer Studio will begin capturing event and audio traffic. Use Audio-Output controls to playback captured audio on the device's Line Out/SPDIF Out or Save as .WAV File or even stream to Host PC over USB using drivers appropriate for your platform (ASIO/ALSA/CoreAudio).
| **Note: **\ Refer to the A\ :sup:`2`\ B Analyzer Studio User Guide PDF for more advanced device usage.

11. Click Stop to finish collecting audio and event traffic. Collected data can be saved to a file (CSV or JSON) using the Download button.

Using A2B Analyzer HP as Node Emulator
--------------------------------------

Main Node Emulator
~~~~~~~~~~~~~~~~~~

1. To configure the device as main node, follow the instructions in the :doc:`A2B Bus Analyzer and A2B Analyzer HP Hardware Setup </wiki-migration/resources/tools-software/a2b-analyzer-studio/a2b-analyzer-hardware-setup>`.

| 2. Launch the A\ :sup:`2`\ B Analyzer Studio and create a new project or open an existing project using the links on the Welcome panel. Ensure to Enable Emulator option if available when creating a new project and switch to Emulator PM1 view using the link in the side panel.
| |image15|

| 3. Configure the device by setting properties as per the node being emulated. Ensure to set Emulate option to ‘Main’. When emulating a Main node, the network information corresponding to the connected nodes shall be provided as a .json file exported from SigmaStudio+ schematic.
| |image16|

| 4. Click on the ‘Start Emulator’ button to set the emulator in Main node mode and initiate the discovery/configuration of the network as per the provided .json file. A successful discovery of the network is indicated with the Discovery status icon turning green.
| |image17|

5. Use Audio Output controls in each sink stream to listen/save/stream any audio stream(s) of interest. Use Audio Input controls in each source stream to feed audio from Line/SPDIF/File/USB In or Test Tones/Loop back options on to the bus. 

Sub Node Emulator
~~~~~~~~~~~~~~~~~

1. To configure the device as a sub node, follow the instructions in the :doc:`A2B Bus Analyzer and A2B Analyzer HP Hardware Setup </wiki-migration/resources/tools-software/a2b-analyzer-studio/a2b-analyzer-hardware-setup>`.

2. Launch the A\ :sup:`2`\ B Analyzer Studio and create a new project or open an existing project using the links on the Welcome panel. Ensure to Enable Emulator option if available when creating a new project and switch to Emulator PM1 view using the link in the side panel.

| 3. Configure the device by setting properties as per the node being emulated. The correct position for the sub node number is recommended although some of the functionality would behave correctly even when choosing the wrong node number. The transceiver is selected from the personality module connected to the board. There is an optional field "Register Writes File" defining the registers to be written for discovering smart sub-nodes. Sigma Studio/Sigma Studio+ defines the format for the JSON and XML.
| |image18|

4. Click on the ‘Start Emulator’ button to set the emulator in Sub node mode (indicated by Node Active icon turning green).

5. Switch to the A\ :sup:`2`\ B network host program (e.g., SigmaStudio+, Head-unit software) and initiate discovery process.

| 6. With network discovery initiated on the host, A\ :sup:`2`\ B Analyzer HP will auto detect the settings for the Sub node being emulated (based on the A\ :sup:`2`\ B Analyzer HP position in the network) and configures itself to emulate the Sub node. A successful discovery of A\ :sup:`2`\ B Analyzer HP as a sub node is indicated by the Discovery status icon turning green.
| |image19|

| 7. Use Audio Output controls in each sink stream to listen/save/stream any audio stream(s) of interest. Use Audio Input controls in each source stream to feed audio from Line/SPDIF/File/USB In or Test Tones/Loop back options on to the bus. 
| **Note: **\ Refer to the A\ :sup:`2`\ B Analyzer Studio *User Guide* for more advanced device usage.

Using A2B Bus Analyzer as Bus Monitor
-------------------------------------

1. To configure the device as a monitor, follow the instructions in the :doc:`A2B Bus Analyzer and A2B Analyzer HP Hardware Setup </wiki-migration/resources/tools-software/a2b-analyzer-studio/a2b-analyzer-hardware-setup>`.

| 2. Launch the A\ :sup:`2`\ B Analyzer Studio and create a new project or open an existing project using the links on the Welcome panel. While creating the project choose Analyzer as A\ :sup:`2`\ B Bus Analyzer.
| |image20|

| 3. Switch to Bus Monitor view using the link in the side panel.
| |image21|

| 4. Select "Normal" mode of bus monitoring.
| |image22|

| 5. Click "Start Monitor" to capture audio and event traffic on the bus.
| **Note: **\ Event and Audio Traffic area will remain blank until the network host initiates A\ :sup:`2`\ B discovery.

6. Switch to the A\ :sup:`2`\ B network host program (e.g., SigmaStudio, Head-unit software) and initiate discovery process.

| 7. With network discovery initiated on the host, the A\ :sup:`2`\ B Analyzer Studio will begin capturing event and audio traffic. Use Audio-Output controls to playback captured audio on the device's Line Out/SPDIF Out or Save as .WAV File or even stream to Host PC over USB using drivers appropriate for your platform (ASIO/ALSA/CoreAudio).
| |image23|
| **Note: **\ Refer to the A\ :sup:`2`\ B Analyzer Studio A2B Analyzer Studio user guide PDF for more advanced device usage.

8. Click Stop to finish collecting audio and event traffic. Collected data can be saved to a file (CSV or JSON) using the Download button.

Bus Monitor in Standalone mode
------------------------------

Connection of Bus Monitor to A\ :sup:`2`\ B network is same as described above. In addition, standalone mode requires a mini-SD card to be inserted into A\ :sup:`2`\ B Bus Analyzer slot. Please refer to the "*Standalone mode*" section (4.6) in the A2B Analyzer Studio user guide PDF to understand how to capture data in standalone mode. The user guide PDF can be found in the A\ :sup:`2`\ B Analyzer Studio software installation. You can access it under the Help menu.

Using A2B Bus Analyzer as Node Emulator
---------------------------------------

.. _main-node-emulator-1:

Main Node Emulator
~~~~~~~~~~~~~~~~~~

1. To configure the device as a main node, follow the instructions in the :doc:`A2B Bus Analyzer and A2B Analyzer HP Hardware Setup </wiki-migration/resources/tools-software/a2b-analyzer-studio/a2b-analyzer-hardware-setup>`.

2. Launch A\ :sup:`2`\ B Analyzer Studio and create a new project or open an existing project using the options on the Welcome panel. Ensure to check Standard-Power/High-Power Emulator option if available when creating a new project.

| 3. Switch to Emulator view (Std/High) using the side panel. Ensure the Power icon is green at this time. If not green, click on the Reset, wait for a few seconds (until the status LED on the unit turns full green) and connect again using the Power icon.
| |image24|

| 4. Configure the device by setting properties as per the node being emulated. Ensure to set Emulate option to ‘Main’.  When emulating a Main node, the network information corresponding to the connected nodes shall be provided as a .dat file exported from SigmaStudio (or SigmaStudio+) for A\ :sup:`2`\ B.
| |image25|

   **Note**:             

-  A\ :sup:`2`\ B SW release package Rel19.9.0 or higher must be used to export adi_a2b_busconfig.dat when using SigmaStudio. Refer to user guide documentation available in the A\ :sup:`2`\ B SW package on how to create A\ :sup:`2`\ B project in SigmaStudio and export a .dat file. The SW release package details for SigmaStudio+ will be provided when that product is available.
-  .DAT files are not correctly exported when 32 streams are configured

5. Click on the ‘Start emulator’ button to set the emulator in Main node mode and initiate the discovery/configuration of the network as per the provided .dat file.

6. A successful discovery of the network is indicated with the Discovery status icon turning green.  

| 7. To view audio streams sourced or sinked by the node switch to Audio panel. Use Audio Output controls in each sink stream to listen/save/stream any audio stream(s) of interest. Use Audio Input controls in each source stream to feed audio from Line/SPDIF/File/USB In or Test Tones/Loop back options on to the bus. 
| |image26|

8. Switch to the Data panel to view SPI data tunnel streams (if any) available on the node. Use Data controls to send/receive data over SPI tunnels different transfer modes.

| 9. Switch to Regs and Logs panel to view Config logs and Registers. Use this panel to read/write registers to/from a node.
| |image27|

.. _sub-node-emulator-1:

Sub Node Emulator
~~~~~~~~~~~~~~~~~

1. To configure the device as a sub node, follow the instructions in the :doc:`A2B Bus Analyzer and A2B Analyzer HP Hardware Setup </wiki-migration/resources/tools-software/a2b-analyzer-studio/a2b-analyzer-hardware-setup>`.

2. Launch A\ :sup:`2`\ B Analyzer Studio and create a new project or open an existing project using the options on the Welcome panel. Ensure to check Standard-Power/High-Power Emulator option if available when creating a new project.

3. Switch to Emulator view (Std/High) using the side panel. Ensure the Power icon is green at this time. If not green, click on the Reset, wait for a few seconds (until the status LED on the unit turns full green) and connect again using the Power icon.

| 4. Configure the device by setting properties as per the node being emulated. Ensure to set Emulate option to ‘Sub’. 
| |image28|

   **Note**: When emulating a Sub node, the configuration information corresponding to the emulated node is automatically detected by the A\ :sup:`2`\ B Bus Analyzer from the bus. 

5. Click on the ‘Start Emulator’ button to set the emulator in Sub node mode (indicated by Node Active icon turning green). 

6. Switch to the A\ :sup:`2`\ B network host program (e.g., SigmaStudio or Head-unit software) and initiate discovery process. 

   **Note**:  A\ :sup:`2`\ B SW release package Rel19.9.0 or higher must be used when using SigmaStudio. Refer to the user guide documentation available in the A\ :sup:`2`\ B SW package on how to create A\ :sup:`2`\ B project in SigmaStudio. 

| 7. With network discovery initiated on the host, A\ :sup:`2`\ B Bus Analyzer will auto detect the settings for the Sub node being emulated (based on the A\ :sup:`2`\ B Bus Analyzer position in the network) and configures itself to emulate the Sub node. A successful discovery of A\ :sup:`2`\ B Bus Analyzer as a sub node is indicated by the Discovery status icon turning green.   
| |image29|

8. Switch to the Audio panel to view audio streams sourced or sinked by the node. Use Audio Output controls to listen/save/stream any audio stream(s) of interest. Use Audio Input controls to feed audio from Line/SPDIF/File/USB In or Test Tones/Loop back options on to the bus.

9. Switch to the Data panel to view SPI data tunnel streams (if any) available on the node. Use Data controls to send/receive data over SPI tunnels different transfer modes.

Further documentation
=====================

Most of the user documentation is located with this guide in the Analog Devices wiki under :doc:`/wiki-migration/resources/tools-software/a2b-analyzer-studio`

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_26.png
   :width: 600px

A more in-depth user guide PDF which can be found in the A\ :sup:`2`\ B Analyzer Studio software installation. You can access it under the Help menu.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_27.png
   :width: 600px

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image4.png
   :width: 20px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image3.png
   :width: 20px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image2.png
   :width: 20px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image4.png
   :width: 20px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image3.png
   :width: 20px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image2.png
   :width: 20px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_2.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_4.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_5.png
   :width: 250px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_6.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_7.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_8.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_9.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_10.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_11.png
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_12.png
   :width: 600px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_13.png
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_14.png
   :width: 600px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_15.png
   :width: 600px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_16.png
   :width: 250px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_17.png
   :width: 600px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_18.png
   :width: 600px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_19.png
   :width: 600px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_20.png
   :width: 600px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_21.png
   :width: 600px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_22.png
   :width: 600px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_23.png
   :width: 600px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_24.png
   :width: 600px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASQSG_25.png
   :width: 600px
