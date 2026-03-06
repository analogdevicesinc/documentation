:doc:`Click here to return to A2B Bus Analyzer Homepage. </wiki-migration/resources/tools-software/a2b-bus-analyzer>`

A2B Bus Analyzer Quick Start Guide
==================================

Introduction
============

The guidelines on these pages are intended to help A\ :sup:`2`\ B users configure and use the Analog Devices' (ADI) A\ :sup:`2`\ B Bus Analyzer tool in Monitor and/or Node Emulator modes for AD242x and AD243x devices with HDAC/Duraclik connectors. AD241x and devices with XLR/RJ45 connectors (AD2437) are not supported.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image1.png
   :width: 600px

Installation and Upgrades
=========================

A\ :sup:`2`\ B Bus Analyzer can be downloaded from :doc:`Software Downloads </wiki-migration/resources/tools-software/a2b-bus-analyzer/software-downloads>`.

Supported Operating Systems
---------------------------

The A\ :sup:`2`\ B Bus Analyzer runs on Windows, Linux, and macOS. The Operating Systems table describes the operating system versions supported in this release. 

+----------+--------------+---------------------------------------------------------------------+
|          | **Platform** | **Details**                                                         |
+==========+==============+=====================================================================+
| |image4| | Windows      | Windows 10 Home, Pro, Enterprise (64-bit), Windows 11 Home (64-bit) |
+----------+--------------+---------------------------------------------------------------------+
| |image5| | Linux        | Ubuntu 18.04+ (64-bit)                                              |
+----------+--------------+---------------------------------------------------------------------+
| |image6| | macOS        | 10.15.x Catalina and later                                          |
+----------+--------------+---------------------------------------------------------------------+

Software Installation Instructions
----------------------------------

The following sub-sections include installation information for the supported OS platforms. 

Windows
~~~~~~~

-  To install the A\ :sup:`2`\ B Bus Analyzer, double-click on ``a2b_bus_analyzer-X.Y.Z-channel-win32-x64.exe``.
-  The A\ :sup:`2`\ B Bus Analyzer is installed in the following default location: C:\\Analog Devices\\A2B Bus Analyzer.
-  To uninstall the A\ :sup:`2`\ B Bus Analyzer, go to the Programs and Features applet in the Control Panel.

Linux
~~~~~

-  To install A\ :sup:`2`\ B Bus Analyzer, download the .AppImage. Copy the file into a directory such as ~/Applications
-  If required, ensure that file has execute permissions by running ``chmod a+x a2b_bus_analyzer_*.AppImage``
-  Launch A\ :sup:`2`\ B Bus Analyzer by running ``./a2b_bus_analyzer-X.Y.Z-channel-x86_64_linux.AppImage``
-  Simply delete the .AppImage file to uninstall A\ :sup:`2`\ B Bus Analyzer.

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

-  To install the A\ :sup:`2`\ B Bus Analyzer double-click on ``a2b_bus_analyzer-X.Y.Z-channel-macos-x64.pkg``

   -  If the Installation Wizard does not launch, right-click the ``.pkg`` file and select ``Open with... | Installer``.

-  The A\ :sup:`2`\ B Bus Analyzer is installed in /Applications.

Product Activation
------------------

To use the A\ :sup:`2`\ B Bus Analyzer product, you must activate your product with a License Key that was issued when you purchased the product.

The license is associated with the A\ :sup:`2`\ B Bus Analyzer hardware so you need to follow the steps at :doc:`Bus Analyzer Setup </wiki-migration/resources/tools-software/a2b-bus-analyzer/quick-start-guide>` in order to activate your license. Pressing the Software Power button while selecting the serial number of an unlicensed analyzer launches the license menus as described in this section.

A brand-new Analyzer will show a License error when you first try to connect to the device. Click **Yes** to continue with the activation process.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image5.png

Select **Activate or Update License…**

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image6.png
   :width: 400px

**Enter** the License key that you received when you purchased the A\ :sup:`2`\ B Bus Analyzer select the **Activate** **online** if you have access to the Internet or **Activate** offline if you already have a validation code or you want to request one.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image7.png
   :width: 400px

**Complete** the required fields and click **Activate**. Your product should now be activated. Use Help \| Email Support... menu option to contact technical support should you have any issues.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image8.png

Software Upgrades
-----------------

Updating A2B Bus Analyzer Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The upgrade process is the same for all supported operating systems.

Run the A\ :sup:`2`\ B Bus Analyzer, visit the Home screen, click 'Check for Updates'. If a newer version is available 'Download' and then 'Restart to Install' to update your copy of A\ :sup:`2`\ B Bus Analyzer.

You can also use the Help \| Check for Updates... menu item to find out if there are any new updates available.

After the A\ :sup:`2`\ B Bus Analyzer software updates, settings from the previous version are preserved.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image9.png
   :width: 600px

Updating A2B Bus Analyzer firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current firmware version on the device is shown on the Home screen after connecting to an A\ :sup:`2`\ B Bus Analyzer device.

If a firmware update is available, click 'Update Firmware' and follow the on-screen instructions to flash the new version to your A\ :sup:`2`\ B Bus Analyzer.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image10.png
   :width: 600px

A2B Bus Analyzer Package Contents
=================================

+-------------+-----------------------------------------------------------+--------------+
| **Sl. No.** | **Content**                                               | **Quantity** |
+=============+===========================================================+==============+
| 1           | A\ :sup:`2`\ B Bus Analyzer HW Unit                       | 1            |
+-------------+-----------------------------------------------------------+--------------+
| 2           | USB-A to Micro-B cable                                    | 1            |
+-------------+-----------------------------------------------------------+--------------+
| 3           | 12V power supply adapter (US)                             | 1            |
+-------------+-----------------------------------------------------------+--------------+
| 4           | A\ :sup:`2`\ B Cable with HDAC to Duraclik connectors     | 1            |
+-------------+-----------------------------------------------------------+--------------+
| 5           | A\ :sup:`2`\ B Cable with HDAC to HDAC connectors         | 2            |
+-------------+-----------------------------------------------------------+--------------+
| 6           | A\ :sup:`2`\ B Cable with Duraclik connectors             | 2            |
+-------------+-----------------------------------------------------------+--------------+
| 7           | A\ :sup:`2`\ B Analyzer Application download instructions | 1            |
+-------------+-----------------------------------------------------------+--------------+

-  The physical dimension of A2B Bus Analyzer box is 15.25" x 9.5" x 4.125".
-  The A2B Bus Analyzer box alone weighs about 533 g. The entire box (including connectors and power supply) may weigh ~ 1kg.

Getting Started with A2B Bus Analyzer
=====================================

Bus Analyzer Setup
------------------

1. Connect the A\ :sup:`2`\ B Bus Analyzer to your PC using the supplied USB-A to Micro-B cable.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image11.png

2. Connect 12V power supply to A\ :sup:`2`\ B Bus Analyzer.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image12.png
   :width: 350px

3. Ensure your A\ :sup:`2`\ B Bus Analyzer software is installed, registered, and upgraded as explained in the Installation and Upgrades section of this guide.

\*\* Note: \*\* If using USB-C for Power, use one of the recommended wall adapters. Refer to the A2B Bus Analyzer User Manual for more details.

4. Launch A2B Bus Analyzer application. Connect to your A2B Bus Analyzer device by selecting it from the device selection drop-down menu then clicking the Power button. Once connected, the Power button becomes green.


|image7|

HDAC Connector and Cable Drawing for Custom Cabling
---------------------------------------------------

Required Components

For 0.35mm2 Cable

+------------+----------------------+-----------------+-------------+--------------+----------------------+
| **S. No.** | **Components**       | **Part Number** | **Company** | **Quantity** | **Remarks**          |
+============+======================+=================+=============+==============+======================+
| 1          | Connector Receptacle | 0310681010      | Molex       | 2            |                      |
+------------+----------------------+-----------------+-------------+--------------+----------------------+
| 2          | Crimp Pins           | 1393367-1       | TE          | 4            | 2 in each receptacle |
+------------+----------------------+-----------------+-------------+--------------+----------------------+
| 3          | Cable                | Dacar-546       | Leoni       | 1.8m         |                      |
+------------+----------------------+-----------------+-------------+--------------+----------------------+

Drawing

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/cable.jpg
   :width: 600px

Using Analyzer as Bus Monitor
-----------------------------

1. Complete steps in the Bus Analyzer Setup section above.

For custom cabling, please use the below pinout details

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/monitor_pins.png
   :width: 400px

-  P1 (towards main): 1 - NC, 2 - AN, 3 - AP, 4 – NC (left to right)
-  P2 (towards sub): 1 - NC, 2 - AP, 3 - AN, 4 – NC (left to right)

2. Connect A\ :sup:`2`\ B Bus Analyzer unit between two nodes in an A\ :sup:`2`\ B network.

**Note:** It is recommended to place the analyzer between the Main and first Sub node (Sub node 0) to allow capturing of all events on the bus.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image13.png
   :width: 400px

3. Launch the A\ :sup:`2`\ B Bus Analyzer application and create a new project or open an existing project using the links on the Welcome panel.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image14.png
   :width: 600px

4. Switch to Bus Monitor view using the link in the side panel.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/qsg_mon2.png
   :width: 600px

5. Activate bus monitoring by sliding the Enable Switch

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/qsg_mon3.png
   :width: 600px

6. Click Play to start capturing audio and event traffic on the bus.

**Note:** Event and Audio Traffic area will remain blank until the network host initiates A\ :sup:`2`\ B discovery.

7. Switch to the A\ :sup:`2`\ B network host program (e.g., SigmaStudio, Head-unit software) and initiate discovery process.

8. With network discovery initiated on the host, the A\ :sup:`2`\ B Bus Analyzer application will begin capturing event and audio traffic. Use Audio-Output controls to playback captured audio on the device's Line Out/SPDIF Out or Save as .WAV File or even stream to Host PC over USB using drivers appropriate for your platform (ASIO/ALSA/CoreAudio).

\*\* Note: \*\* Refer to the A2B Bus Analyzer User Manual for more advanced device usage.

9. Click Stop to finish collecting audio and event traffic. Collected data can be saved to a file (CSV or JSON) using the Download button.

.. tip::

   AD2438/30 evaluation boards have only one A2B port and the analog front end expects straight-through UTP cabling where as the default cables with the A2B Bus Analyzer box is cross-over cables.

   
   For usage with AD2438/30 evaluation boards, the monitor connection needs to be different as shown in below diagram. Ensure that the upstream node's A2B_CONTROL.XCVRBINV bit is set.
   
   **Note**: AD2438 can only be used as Main node.

   
   |image8|

Using Analyzer as Node Emulator
-------------------------------

For customer cabling, please use the below pinout details:

**High power connector:**

\* P7 (towards sub): 1 - GND, 2 - BP, 3 - BN, 4 – GND (left to right)

\* P8 (towards main): 1 - GND, 2 - AN, 3 - AP, 4 – GND (left to right)

**Standard power connector:**

\* P6 (towards sub): 1 - BP, 2 – BN (left to right)

\* P3 (towards main): 1- AN, 2- AP (left to right)

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/emulator_pins.png
   :width: 400px

Main Node Emulator
~~~~~~~~~~~~~~~~~~

1. Complete steps in the Bus Analyzer Setup section above.

2. Connect Sub node or chain of Sub nodes to the node emulator port labelled “TOWARDS SUB” on STD or HIGH PWR depending on the power configuration of the node being emulated.

**Note:** **AD242x node emulator** is also supported on STD PWR. Thus use emulator port labelled “TOWARDS SUB” on STD PWR port to connect sub node(s) when emulating AD242x Main node.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/stdpower1.png
   :width: 600px

3. Switch to the A\ :sup:`2`\ B Bus Analyzer application and create a new project or open an existing project using the options on the Welcome panel. Ensure to check Enable Standard-Power/High-Power Emulator option if available when creating a new project.

4. Switch to Emulator view (Std/High) using the side panel and turn on the function by sliding the Enable switch. Ensure the Power icon is green at this time. If not green, click on the Reset, wait for a few seconds (until the status LED on the unit turns full green) and connect again using the Power icon.

5. Configure the device by setting properties as per the node being emulated. Ensure to set Emulate option to ‘Main’. When emulating a Main node, the network information corresponding to the connected nodes shall be provided as a .dat file exported from SigmaStudio (or SigmaStudio+) for A\ :sup:`2`\ B.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/emuconnect1.png
   :width: 600px

**Note:** A\ :sup:`2`\ B SW release package Rel 19.9.0 or higher must be used to export adi_a2b_busconfig.dat when using SigmaStudio. Refer to SigmaStudio user guide documentation available in the A\ :sup:`2`\ B SW package on how to create A\ :sup:`2`\ B project in SigmaStudio and export a .dat file.

6. Click on the ‘Apply’ button to set the emulator in Main node mode and initiate the discovery/configuration of the network as per the provided .dat file.

7. A successful discovery of the network is indicated with the Discovery status icon turning green.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/emustatus.png
   :width: 600px

8. Switch to the Audio panel to view audio streams sourced or sinked by the node. Use Audio Output controls to listen/save/stream any audio stream(s) of interest. Use Audio Input controls to feed audio from Line/SPDIF/File/USB In or Test Tones/Loop back options on to the bus.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/emuaudio.png
   :width: 600px

9. Switch to the Data panel to view SPI data tunnel streams (if any) available on the node. Use Data controls to send/receive data over SPI tunnels different transfer modes.

Sub Node Emulator
~~~~~~~~~~~~~~~~~

1. Complete steps in the :doc:`Bus Analyzer Setup </wiki-migration/resources/tools-software/a2b-bus-analyzer/quick-start-guide>` section above.

2. Insert the Analyzer unit in an A\ :sup:`2`\ B network at a desired Sub node position to be emulated. Connect the unit to an upstream node, using TOWARDS MAIN, and to a downstream node, using TOWARDS SUB (if it is not the last node), on STD or HIGH PWR node emulator ports depending on the power configuration of the node being emulated.

**Note:**\ \*\* AD242x node emulator*\* is also supported on STD PWR. Thus use emulator ports labelled TOWARDS MAIN and TOWARDS SUB on STD PWR when emulating AD242x Sub node.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/stdpowersub1.png
   :width: 600px

3. Switch to A\ :sup:`2`\ B Bus Analyzer application and create a new project or open an existing project using the options on the Welcome panel. Ensure to check Enable Standard-Power/High-Power Emulator option if available when creating a new project.

4. Switch to Emulator view (Std/High) using the side panel and turn on the function by sliding the Enable switch. Ensure the Power icon is green at this time. If not green, click on the Reset, wait for a few seconds until the status LED on the unit turns full green and connect again using the Power icon.

5. Configure the device by setting properties as per the node being emulated. Ensure to set Emulate option to ‘Sub’.

**Note:** When emulating a Sub node, the configuration information corresponding to the emulated node is automatically detected by the Analyzer from the bus.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/emuconnectsub1.png
   :width: 600px

6. Click on the ‘Apply’ button to set the emulator in Sub node mode (indicated by Node Active icon turning green).

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/emustatussub1.png
   :width: 600px

7. Switch to the A\ :sup:`2`\ B network host program (e.g., SigmaStudio or Head-unit software) and initiate discovery process.

**Note:** A\ :sup:`2`\ B SW release package Rel 19.9.0 or higher must be used when using SigmaStudio. Refer to SigmaStudio user guide documentation available in the A\ :sup:`2`\ B SW package on how to create A\ :sup:`2`\ B project in SigmaStudio.

8. With network discovery initiated on the host, Analyzer will auto detect the settings for the Sub node being emulated (based on the Analyzer position in the network) and configures itself to emulate the Sub node. A successful discovery of Analyzer as a sub node is indicated by the Discovery status icon turning green.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/emudiscoverysub1.png
   :width: 600px

9. Switch to the Audio panel to view audio streams sourced or sinked by the node. Use Audio Output controls to listen/save/stream any audio stream(s) of interest. Use Audio Input controls to feed audio from Line/SPDIF/File/USB In or Test Tones/Loop back options on to the bus.

10. Switch to the Data panel to view SPI data tunnel streams (if any) available on the node. Use Data controls to send/receive data over SPI tunnels different transfer modes.

Using A2B Bus Analyzer with SigmaStudio+
========================================

SigmaStudio+ supports representation of A\ :sup:`2`\ B Bus Analyzer for creating A\ :sup:`2`\ B networks containing the A\ :sup:`2`\ B Bus Analyzer hardware in the signal chain. It also integrates with the A\ :sup:`2`\ B Bus Analyzer UI to support the following functionality:

-  A\ :sup:`2`\ B Bus Analyzer UI launch from SigmaStudio+
-  A\ :sup:`2`\ B Bus Analyzer UI Project Creation, Automatic Load of Monitor\\Emulator Views and Device Connect
-  Automatic Emulator Enable and .DAT file Apply of a schematic
-  Node highlighting and Line fault error notification in SigmaStudio+ during Main Node Emulation
-  Post Discovery Register Read/Write from SigmaStudio+ during Main Node Emulation
-  Post Discovery Peripheral Read/Write from SigmaStudio+ during Main Node Emulation

**Note:** SigmaStudio+ release package 2.0.0 and A2B-SS+ Plugin release package 1.1.0 or above need to be installed for using the A\ :sup:`2`\ B Bus Analyzer with SigmaStudio+. Refer to AE_65_A2B-SSPlus_QuickStartGuide in the A2B-SS+ plugin installation package for steps to create schematics with A\ :sup:`2`\ B Bus Analyzer hardware in the network. Refer to the user guide PDF which can be found in the A2B Bus Analyzer software installation for steps to Launch and operate A2B Bus Analyzer UI from SigmaStudio+. Section :doc:`Further documentation </wiki-migration/resources/tools-software/a2b-bus-analyzer/quick-start-guide>` describes how to find the User Guide.

Further documentation
=====================

Most of the user documentation is located, with this guide in the Analog Devices wiki under :doc:`A2B Bus Analyzer Homepage </wiki-migration/resources/tools-software/a2b-bus-analyzer>`.

The exception is a more in-depth user guide PDF which can be found in the A2B Bus Analyzer software installation. You can access it under the Help menu

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/userguidemenu.png
   :width: 200px

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image2.png
   :width: 20px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image3.png
   :width: 20px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image4.png
   :width: 20px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image2.png
   :width: 20px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image3.png
   :width: 20px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image4.png
   :width: 20px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image16.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/cross_over_cables.jpg
   :width: 600px
