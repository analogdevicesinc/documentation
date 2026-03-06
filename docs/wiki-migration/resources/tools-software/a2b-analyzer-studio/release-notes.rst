:doc:`Click here to return to A2B Analyzer Studio Homepage. </wiki-migration/resources/tools-software/a2b-analyzer-studio>`

A2B Analyzer Studio Release Notes v1.1.0 (December 2025)
========================================================

New and Noteworthy
------------------

Ethernet Connectivity for A²B Analyzer HP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now connect to your A²B Analyzer HP either via USB like before or via Ethernet to enable more flexible communication and remote access. Please follow the User Guide for details of the correct method.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/ethernet_connect.jpg
   :alt: a2b-analyzer-studio/ethernet_connect.jpg
   :width: 500px

Network settings can be displayed in the device settings whether the board is connected via USB or Ethernet

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/network_props.jpg
   :alt: a2b-analyzer-studio/network_props.jpg
   :width: 250px

Ethernet Audio is not supported, only Ethernet communication.

Connecting to the Same Device from Two Ethernet Instances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   **Note:** Connecting to the same A²B Analyzer HP device from two separate instances simultaneously is not supported regardless of the type of connection. Only one Ethernet connection to the device can be active at a time. If a second instance attempts to connect, the first connection will be terminated. Please ensure only one session is active at a time.

Node Name Changes and JSON Support for A²B Analyzer HP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Node naming conventions have been updated for consistency. The new format is ``<node number>:<node name>``.

By default, names are similar to previous releases. For A²B Analyzer HP, you can use node names from the Sigma Studio+ project JSON file provided at monitor or emulator start. This improves clarity and traceability in network analysis. To use JSON node names, select the relevant option in project settings.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/proj-adv-settings.jpg
   :alt: a2b-analyzer-studio/proj-adv-settings.jpg
   :width: 250px

Node names from the JSON file are retrieved only at monitor or emulator start; project changes take effect at that point. If you change the setting while monitor or emulator is running, the change will not apply immediately.

Stream names are not supported in this release but are planned for a future update.

USB Resolution Configuration for A²B Analyzer HP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now change the USB audio resolution for more precise control and compatibility with different audio setups.

Access device audio and network properties from the device toolbar using the properties dropdown.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/audio_props.jpg
   :alt: a2b-analyzer-studio/audio_props.jpg
   :width: 300px

New SDK APIs support getting and changing device data.

**Notes:** Property settings only apply after you reset the device. Modifying the sample rate is not supported in this release

Monitor SPI Events and Redesigned Monitor Page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Monitor in A²B Analyzer Studio can now detect SPI data tunnel events. SPI tunnel events are grouped in a new table. To improve consistency, all events for all platforms are now separated onto a new “Events” page under monitor for all devices.

You can filter both tables by a range of frame numbers to correlate standard and SPI events.

Firmware Behavior Change in 5.1.x Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Up to version 5.1.0, A²B Bus Analyzer and A²B Analyzer Studio would connect to a device even if it meant disconnecting an existing session. Customers did not need to manually disconnect before reconnecting.

From version 5.1.0, connection is refused by default if another instance is connected, preventing multiple ethernet connections from interfering. If an existing connection is detected, the UI displays a pop-up to let you reset your hardware and therefore disconnect the other session.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/force_connect.jpg
   :alt: a2b-analyzer-studio/force_connect.jpg
   :width: 300px

From the SDK, ensure you disconnect the device on exit, reset the device before connecting, or use the new API to force connection regardless of others.

**Note:** Multiple USB connections to the same COM port are not allowed by the operating system and are always rejected.

Changes to User Guides and Release Notes Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All user guides included with the project are now HTML instead of PDF. Continue using the same links as previous releases to open the files.

Removed support for python 3.9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The user-accessible SDK no longer supports python 3.9. Python 3.9 reached its end of life in October 2025 so it is not expected to work with the SDK wheel.

Resolved Issues
---------------

-  None listed for this release.

A2B Analyzer Studio 1.0.1 Release Notes
=======================================

This release is a small patch release to solve a race condition in the UI related to the restoring of audio interfaces from a file for monitor projects discovered with Sigma Studio/Sigma Studio+.

A2B Analyzer Studio 1.0.0 Release Notes
=======================================

A\ :sup:`2`\ B Analyzer Studio is the next-generation continuation of A\ :sup:`2`\ B Bus Analyzer Software, introducing new features and support for the new A\ :sup:`2`\ B Analyzer HP. It is designed to maintain compatibility with existing software while providing extended functionality and scalability for future needs.

This document describes new and noteworthy changes for A\ :sup:`2`\ B Analyzer Studio as well as known issues.

This release supports monitor and emulator both in the A\ :sup:`2`\ B Analyzer HP with personality modules and the original A\ :sup:`2`\ B Bus Analyzer hardware. The only supported personality modules in A\ :sup:`2`\ B Analyzer HP are for ADAA245x networks.

System Hardware Requirements
----------------------------

Verify that your PC meets the following minimum operating system version and requirements to install and run A\ :sup:`2`\ B Analyzer Studio.

A\ :sup:`2`\ B Analyzer Studio runs on Windows, Linux, and macOS. The Operating Systems table describes the operating system versions supported in this release. 

+------------------+---------------------------------------------------------------------------------------------+
| Platform         | Details                                                                                     |
+------------------+---------------------------------------------------------------------------------------------+
| |image4| Windows | Windows 10 and 11 Home, Pro, Enterprise (64-bit)                                            |
+------------------+---------------------------------------------------------------------------------------------+
| |image5| Linux   | Ubuntu 22.04+ (64-bit)                                                                      |
+------------------+---------------------------------------------------------------------------------------------+
| |image6| macOS   | 14.x (Sonoma or) later on ARM.                                                              |
|                  | **Note**: macOS x64 platforms are not supported. Only ARM-based macOS systems are supported |
+------------------+---------------------------------------------------------------------------------------------+

A2B Analyzer Studio Installation
--------------------------------

The A\ :sup:`2`\ B Analyzer Studio installer for each supported platform is described in the table below and can be downloaded from :doc:`Software Downloads </wiki-migration/resources/tools-software/a2b-analyzer-studio/software-downloads>`.

======== =======================================================
|image7| a2b_analyzer_studio-X.Y.Z-channel-win-x64.exe
|image8| a2b_analyzer_studio-X.Y.Z-channel-linux-x86_64.AppImage
|image9| a2b_analyzer_studio-X.Y.Z-channel-macos-arm64.pkg
======== =======================================================

Installation Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~

The following sub-sections include installation information for supported platforms.

Windows
^^^^^^^

-  To install A\ :sup:`2`\ B Analyzer Studio, double-click on a2b_analyzer_studio-X.Y.Z-channel-win-x64.exe
-  A\ :sup:`2`\ B Analyzer Studio is installed in the following default location: C:\\Analog Devices\\A2B Analyzer Studio
-  To uninstall A\ :sup:`2`\ B Analyzer Studio, go to the Programs and Features applet in the Control Panel

Linux
^^^^^

-  To install A\ :sup:`2`\ B Analyzer Studio, download the .AppImage. Copy the file into a directory such as ~/Applications
-  If required, ensure the downloaded file has execute permissions by running chmod a+x a2b_analyzer_studio\_\*.AppImage
-  Launch the A2B Analyzer Studio by running ./a2b_analyzer_studio-X.Y.Z-channel-x86_64_linux.AppImage
-  Delete the .AppImage file to uninstall A\ :sup:`2`\ B Analyzer Studio.

macOS
^^^^^

-  To install A\ :sup:`2`\ B Analyzer Studio, double-click on a2b_analyzer_studio-X.Y.Z-channel-macos-arm64.pkg
-  Follow the installation wizard to install the A\ *2*\ B Analyzer Studio. You may choose your desired install location
-  To uninstall the A\ *2*\ B Analyzer Studio, find the application in your install location, right click it and click "Move to Bin"

.. _new-and-noteworthy-1:

New and Noteworthy
------------------

While A\ :sup:`2`\ B Analyzer Studio is a continuation of A\ :sup:`2`\ B Bus Analyzer, there are significant differences between the two products.

Installed alongside A2B Bus Analyzer Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A\ :sup:`2`\ B Analyzer Studio can be installed in the same machine as the A\ :sup:`2`\ B Bus Analyzer since their install locations are different. For example on Windows this product is installed in 

c:\\Analog Devices\\A2B Analyzer Studio

You cannot do UI updates between the two products.

To use A2B Analyzer Studio you must update the firmware to 5.0.x. If you need to go back to using the A2B Bus Analyzer Software you must downgrade to the version of firmware released with the specific version of the software.

Support for both A2B Bus Analyzer for A2B1.0 networks and A2B Analyzer HP for A2B2.0 networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A\ :sup:`2`\ B Analyzer Studio supports both monitor and emulator for the A\ :sup:`2`\ B Bus Analyzer for A2B1.0 networks (AD243x, AD242x) and A\ :sup:`2`\ B Analyzer HP with replaceable personality modules for A2B2.0 networks (ADAA245x). In future A\ :sup:`2`\ B Analyzer HP may support A2B1.0 networks in their personality modules. At that point new releases of this software will add the support.

In this version, the software supports emulator in personality module 1 and monitor in personality module 2. Other combinations are not supported.

When creating a project now it is necessary to specify the type of hardware that the project applies to.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/a2bas_project_creation.png
   :width: 400px

Doing this ensures that the project settings match the hardware that will be used.

SDK Updates
~~~~~~~~~~~

New SDK API format
^^^^^^^^^^^^^^^^^^

While the A\ :sup:`2`\ B Bus Analyzer Software SDK API is still supported for both python and C/C++ this API may be deprecated in future releases.

To replace it, a new API has been introduced where one of the main changes is that all monitor/emulator APIs use a monitor/emulator handle instead of a device handle. To find documentation about this new API export the User-Accessible SDK in the SDK menu and open the C/Python documentation at

-  C/C++: uasdk/C/docs/A2B_Analyzer_UASDK_help.html 
-  Python: uasdk/python/docs/a2ba_python_sdk_help.html

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/a2bas_sdk_docs.png
   :width: 400px

Example:

-  Old API:  ``a2ba_sdk_result_t a2ba_sdk_monitor_audio_level( a2ba_sdk_device_handle hAnalyzer, a2ba_sdk_monitor_audio_level_t * const pMonitorAudioLevel);``
-  New API:``a2ba2_sdk_result_t a2ba2_sdk_monitor_audio_level(a2ba2_sdk_monitor_handle hMonitor a2ba2_sdk_monitor_audio_level_t const pMonitorAudioLevel);``

Unique SDK python wheel
^^^^^^^^^^^^^^^^^^^^^^^

The A\ :sup:`2`\ B Bus Analyzer Software SDK for python contained a different wheel per version of python. This made it difficult for customers who were not using any of the versions provided. A\ :sup:`2`\ B Analyzer Studio provides one single wheel that supports versions from python 3.9 to version 3.13.

You can find the Python wheels in your exported SDK in the uasdk/python folder

| a2ba_sdk-1.0.0-py3-none-linux_x86_64.whl
| a2ba_sdk-1.0.0-py3-none-macosx_14_0_arm64.whl
| a2ba_sdk-1.0.0-py3-none-win_amd64.whl

The wheels are still OS-specific since they internally use the C/C++ libraries which are OS-specific

Removal of licensing restrictions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A\ :sup:`2`\ B Analyzer Studio no longer requires that your hardware is licensed. This means that there is no limitation in the software updates that you can use. We encourage users to move to the latest version of the software possible since it is where fixes/enhancements are developed. For this reason, the computer where A\ :sup:`2`\ B Analyzer Studio is used does not need to be connected to the internet.

User Interface Updates
~~~~~~~~~~~~~~~~~~~~~~

New Feature: Saving/Restoring Audio Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To allow for a fast configuration of monitor and emulator audio A\ :sup:`2`\ B Analyzer Studio let you save the running audio interfaces state  (which streams are in USB out for example) onto a json file. This json file can at a later stage be applied to the project while monitor/emulator are running and the previous state can be restored.

-  To save the current running state go to Audio Interfaces and click on the "Save" icon or choose "Save Audio file" as from the Options dropdown
-  To apply an already saved json file first add it to your project by choosing "Add Audio Interfaces File". This links the project with that file. After that, you can either click on the Audio Interfaces "Apply" button or select "Apply/Reapply Audio Interfaces" from the Options dropdown.

|image10|

User Interface enhancements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

As a result of carrying out interviews with customers to evaluate their experience, A\ :sup:`2`\ B Analyzer Studio has streamlined some of the operations. The supported functionality has not changed but the way of accessing it may be different.

Some examples are:

-  Easier to use monitor and emulator start toolbars. They include an intuitive way of detecting why monitor/emulator cannot be started by hovering over the error banner


|image11|

-  The "i" symbol is now commonly used for tooltips that provide more clarity or information. Those tooltips can be seen by hovering over the symbol. For example, in the Audio Tables, hovering over the "i" on a stream row shows the Slot Size and other features of that stream including which interfaces it is being used on (line in/out, SPDIF in/out etc).

|image12|

-  Enhanced filters on tables

|image13|

-  A summary of the monitor events is now easily accessible

|image14|

For more information about the features available see the A\ :sup:`2`\ B Analyzer Studio User Guide which is included as PDF in the software and can be accessed from the Help Menu.

Quick Start Guide
-----------------

For further A\ :sup:`2`\ B Analyzer Studio documentation, please see the documentation in Help. There you will find the link to the `Quick Start Guide <:doc:`/wiki-migration/resources/tools-software/a2b-analyzer-studio/quick-start-guide`>`__ and the you can open the PDF *User Guide.*

Support
-------

For technical support contact Analog Devices A\ :sup:`2`\ B Analyzer Studio and A\ :sup:`2`\ B Bus Analyzer Support at: *<fc #4682b4>a2b.analyzer.support@analog.com</fc>*

Known Issues
------------

An up-to-date list of issues for both the A\ :sup:`2`\ B Analyzer Studio and the A\ :sup:`2`\ B Bus Analyzer can be found at :doc:`/wiki-migration/resources/tools-software/a2b-bus-analyzer/known-issues`

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
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image2.png
   :width: 20px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image3.png
   :width: 20px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image4.png
   :width: 20px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/a2bas_audio_interfaces_menu.png
   :width: 300px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/a2bas_start_toolbar.png
   :width: 500px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/a2bas_stream_info_tooltip.png
   :width: 150px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/a2bas_stream_table_filter.png
   :width: 300px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/a2bas_event_trace_summary.png
   :width: 300px
