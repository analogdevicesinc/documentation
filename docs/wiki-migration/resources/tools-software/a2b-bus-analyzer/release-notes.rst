:doc:`Click here to return to A2B Bus Analyzer Homepage. </wiki-migration/resources/tools-software/a2b-bus-analyzer>`

A2B Bus Analyzer 3.4.0 Release Notes
====================================

New and Noteworthy
------------------

Improvements in Test Tone support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for multiple streams contributing to the same Test Tone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Similarly to being able to select multiple streams contributing to the same source channel as released in 3.3.0, you can now select for the same test tone to go to multiple streams.


|image1|

Increased precision in Test Tone gain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The precision of the gain has been increased to allow the gain to be changed in increments of 0.01 dB.

Support for setting sub-specific registers in the Regs Any Node tab when emulating main
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previous releases of the A2B Bus Analyzer only displayed the list of registers for the node being emulated. As a consequence of this, when emulating main, it was impossible to read/write sub-specific registers like mailbox registers. Further, emulating a AD242x main node with some AD243x sub nodes would result on not being able to read/write AD243x specific registers.

For this reason you now need to select which node to display the registers for before adding them to the register sequence. Reading/Writing registers to multiple nodes in the same register sequence is supported as before.


|image2|

Improved Emulator Start Sequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This release reduces the steps required to start the emulator. For this the "Enable" toggle has been removed. Further, the Start Emulator and Reset Emulator buttons have been made accessible from all emulator pages and therefore you do not need to go to the device tab unless changes are needed to the current project setup.

New SDK APIs for enhanced tone support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since the UI supports multiple streams for the same tone and a precision of cdB, new SDK APIs have been introduced which support the new tones, a2ba_sdk_emulator_tone_ex_start and a2ba_sdk_emulator_tone_ex_update.

The previous APIs a2ba_sdk_emulator_tone_start and a2ba_sdk_emulator_tone_update are now considered deprecated and may be removed in a future release.

See the SDK documentation in the SDK menu for more information about the arguments that these APIs support.

Use of IntEnum rather than integers in the a2ba_sdk Python package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previous releases of the a2ba_sdk Python package used integers wherever the C interface used enumerations; this release of the a2ba_sdk Python package uses classes that inherit from the IntEnum class imported from the built-in enum module. This is to provide greater clarity over the meaning of values returned by the SDK. For example, the possible values for the status of register access are now documented in the a2ba_sdk_register_status_t class type. An affect of this is that they now have different types and may throw a ValueError exception if provided with an invalid value. The namespace of the enumeration is also affected as the enum member needs to be prepended by its type, for example A2BA_SDK_SUCCESS is now a2ba_sdk_result_t.A2BA_SDK_SUCCESS . To maintain backwards compatibility, the original integer constants remain in the interface and can be used interchangeably as they are equivalent in value.

New SDK menu for easy access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to make the SDK documentation easier to find, the UI now contains a dedicated SDK menu item where you can export the SDK and access both the C/C++ and python documentation in a clearer manner.

A2B Bus Analyzer 3.3.0 Release Notes
====================================

.. _new-and-noteworthy-1:

New and Noteworthy
------------------

Selection of channels/slots for Monitor and Sink Streams (Line Out/SPDIF Out/USB Out)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since version 3.2.0 channel/slot number for Line Out/ SPDIF Out etc was determined by the order that the streams were selected. While this is still the default, the Stream Info window which pops up when clicking the pencil next to Bus Traffic or Sink/Source Audio now contains a pencil for edit itself. If you then choose the type of route you are interested in (Line/SPDIF/USB) you will be able to select the channels for each stream you had selected in the Audio Table, including choosing the same stream for multiple channels. Note that the Stream Edit page should not be used to add/remove streams, just to change the channels of the already selected.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/sink_channels.png
   :width: 600px

Support for multiple streams contributing to the same Source channel (Line In/SPDIF In/USB In)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Similarly to being able to select multiple channels for a given stream in Sink/Monitor streams, the A2B Bus Analyzer now supports being able to have the multiple streams contributing to the same source channel. For this you tick in the audio table as many streams as you want to source and then in the Stream Info → Stream Edit window launched from the Source area you can select all those streams to be in the same channel. As for selecting channels for streams on sink, you should not use the steam edit pane to add/remove stream, just to change the channel where they are routed.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/source_channels.png
   :width: 600px

Selection of slots to store in standalone mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In 3.2, Standalone mode was introduced, allowing the A2B network activities to be sniffed by the Bus Monitor and get logged onto an SD card without the use of a computer for field/in-vehicle testing. At the time, there was no way to choose the streams recorded by the A2B Bus Analyzer and the first 8 would be recorded. With 3.3, the new Stream Edit dialog allows up to 8 streams to be selected, preventing any unnecessary data being recorded and allowing any streams to be chosen.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/bmsa_channels.png
   :width: 600px

Support for emulation of smart sub nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Smart subnodes require certain register writes in order to be able to discover the network. For this reason, A2B Bus Analyzer 3.3.0 adds the capability of specifying an optional JSON or XML file which contains the register writes required. If a node number is specified in this file it is ignored. The format for the XML is the same as the one generated by Sigma Studio and the format for JSON is the same as generated by the A2B Bus Analyzer when saving a sequence in the Regs Any Node pane.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/smart_subs.png
   :width: 600px

Changes to format in import/export of register sequences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

o help discover smart sub-nodes, the A2B Bus Analyzer Application now allows the user to select a register sequence JSON or XML file before starting the emulator, to allow for registers to be read and written between Emulator Connect and Start. The JSON structure of the register sequence has changed, but ones from previous versions (3.2 and below) will still be compatible.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/regs_all.png
   :width: 400px

Solved Issues
-------------

For all solved issues see https://wiki.analog.com/resources/tools-software/a2b-bus-analyzer/known-issues. The list below contains the most notable.

Audio bit exactness and clock skew elimination
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previous versions did not maintain bit exactness of USB Audio and interpolation/decimation of audio was performed to correct clock skew. Release 3.3.0 maintains USB audio bit exactness and eliminates clock skew.

Incorrect value used for delays in peripheral programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Version 3.2.0 introduced the peripheral programming window. Unfortunately there was a bug in the code where the value for "delay" was not accepted correctly and therefore always having a delay of 1 or 2ms. Release 3.3.0 fixes this issue.

File Out may not work in windows systems that are not in English
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Version 3.2.0 of the A2B Bus Analyzer replaced the way file out is done in order to be able to support more than two channels. This version required the Audio Devices in Device Manager to be called “Microphone (A2B Bus Analyzer)” and/or “Speakers (A2B Bus Analyzer)”. In windows devices in other languages file out does not work since the device is not found.

A2B Bus Analyzer 3.2.0 Release Notes
====================================

.. _new-and-noteworthy-2:

New and Noteworthy
------------------

New Stand-alone mode
~~~~~~~~~~~~~~~~~~~~

During field/in-vehicle testing, it may not be possible to connect the A2B Bus Analyzer to a PC/laptop to view runtime insights of the network using the A2B Bus Analyzer UI. To overcome this limitation, the A2B Bus Analyzer includes support for Standalone Mode operation where all the runtime A2B network activities that the Bus Monitor can sniff are logged onto an SD card. Once the in-vehicle testing is completed, you can then connect the Analyzer back to the PC to view and analyze all the logged data which may include any errors observed on the bus, the control data and optionally the audio streams available on the bus.

Note that when the analyzer HW is recording data in stand-alone mode, the USB connection cannot be used and therefore the A2B Bus Analyzer application cannot be used at the same time. The position of the stand-alone switch was ignored in previous releases.

.. warning::

   If your board does not connect to your UI after the firmware update ensure that the standalone switch is down.


New Peripheral Programming Window for Emulator Main
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The UI now incorporates as a tab in the register windows in which providing a XML file with I2C peripheral accesses in the same format generated by Sigma Studio, an output file is generated with the result of the accesses. Json is also supported but there are no tools currently that generate that file format. To match this there is a new SDK API in both python and C/Cpp which takes a whole file instead of a list of accesses. The API is *a2ba_sdk_peri_file*.

Changes to Audio File-Out - now linked to USB Out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to be able to support file out to more than two channels, file out has been completely re-implemented to not poll the firmware for data. Instead, the output is redirected to USB Out and captured to a file from there. This means that as well as being able to record up to a total of 32 channels at a time, you can also record to file simultaneously from monitor and emulator.

As a consequence of the change, file out does not work on windows remote desktop sessions since the USB device is not found in device manager or on macOS when connecting remotely. This is the same limitation that other tools like Audacity have.

Redesign of the audio panes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

There has been a redesign in the way that the tables with streams in order to remove the control pane. The change has been made to try to accommodate smaller screens better. From this versions, enabling Line Out/SPDIF out etc will be done from the stream description itself. As part of this redesign some of the previous user interface restrictions have been changed

+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Control                                                                                         | **3.1.0**                  | **3.2.0**                                                                                                                                                                                                                            |
+=================================================================================================+============================+======================================================================================================================================================================================================================================+
| Line Out used in both monitor and emulator simultaneously (total max 2 channels)                | <fc #ff0000>\ **✘**\ </fc> | <fc #008000>\ **✔**\ </fc>                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Line Out and SPDIF Out can be used simultaneously in monitor                                    | <fc #ff0000>\ **✘**\ </fc> | <fc #008000>\ **✔**\ </fc>                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Line Out and SPDIF Out can be used simultaneously in emulator                                   | <fc #ff0000>\ **✘**\ </fc> | <fc #008000>\ **✔**\ </fc>                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| USB Out can be used at the same time in monitor and emulator                                    | <fc #ff0000>\ **✘**\ </fc> | <fc #008000>\ **✔**\ </fc>                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| File Out can be used at the same time in monitor and emulator                                   | <fc #008000>\ **✔**\ </fc> | <fc #008000>\ **✔**\ </fc>                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Same sink stream can used in multiple controls simultaneously (other than Line out/SPDIF out)   | <fc #008000>\ **✔**\ </fc> | <fc #008000>\ **✔**\ </fc>                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Line In and SPDIF In can be used simultaneously in emulator                                     | <fc #ff0000>\ **✘**\ </fc> | <fc #008000>\ **✔**\ </fc>                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| USB In and Out start the moment a stream is selected without an "enable" button                 | <fc #ff0000>\ **✘**\ </fc> | <fc #008000>\ **✔**\ </fc>                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Same source stream can used in multiple controls simultaneously (other than Line out/SPDIF out) | <fc #ff0000>\ **✘**\ </fc> | <fc #ff0000>\ **✘**\ </fc>                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| A stream can be selected for both left and right in Line and SPDIF                              | <fc #008000>\ **✔**\ </fc> | <fc #ff0000>\ **✘**\ </fc> In order to find out which channels are being used, the A2B Bus Analyzer now includes a Stream Info window where you can see which input/output is used by each stream and the channels that they map to. |
+-------------------------------------------------------------------------------------------------+----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

New SDK Python wheel version - new Ubuntu version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This version includes a wheel for python 3.10 as well as the prior one for python 3.8. This has resulted in an increase to the minimum version of Ubuntu supported which has increased from 18.04 to 20.04.

A2B Bus Analyzer 3.1.0 Release Notes
====================================

.. _new-and-noteworthy-3:

New and Noteworthy
------------------

AD2430/38 transceiver support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This version includes Beta support for AD2430/38 emulator sub and main. The emulator transceiver drop-down includes the supported devices.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/adi2430_2438.png
   :width: 300px

The bus monitor features were always available for AD2430/38 even if this was not explicitly mentioned in the release notes.

For any known issues refer to :doc:`Functional Limitations </wiki-migration/resources/tools-software/a2b-bus-analyzer/known-issues>`

Enable monitoring of networks already discovered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previous versions of the A2B Bus Analyzer required network discovery to be triggered after the monitor had been enabled. This version introduces the ability of monitoring networks that have already been discovered by ticking a box in the UI. This would allow getting monitor events immediately but in order to see audio streams further steps need to be taken. Please see the A2B Bus Analyzer User Guide for more details.

New user-accessible SDK APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

APIs for programming peripherals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The User-Accessible SDK now supports the APIs a2ba_sdk_peri_access and a2ba_sdk_peri_combined_accesses to program I2C peripherals from either python or C/C++. These APIs are only available when emulating main nodes. Please see the A2B Bus Analyzer SDK HTML API documentation for more information.

APIs to support data tunnels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The User-Accessible SDK now supports the APIs a2ba_sdk_emulator_spi_info, a2ba_sdk_emulator_spi_responder_start/stop, a2ba_sdk_emulator_spi_responder_read, a2ba_sdk_emulator_spi_initiator_start/stop and a2ba_sdk_emulator_spi_initiator_transaction to match the current UI support for SPI data tunnels. Please see the A2B Bus Analyzer SDK HTML API documentation for more information.

Incompatible change in User-accessible SDK API to allow monitoring of networks already discovered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The API a2ba_sdk_monitor_enable now takes an argument which indicates whether monitor will work on an already discovered network or if the network must be discovered after the call to the API. Setting this parameter to 0 will result on the same behaviour as prior releases of the SDK.

Volume setting for USB and SPDIF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previous versions of the SDK allowed changing volume (gain)  in USB and SPDIF inputs and outputs. This has been removed and trying to call the API for anything other than Line In/Out results in an error. The volume setting for SPDIFF from the UI has been removed.

A2B Bus Analyzer 3.0.1 Release Notes
====================================

Issues Adressed
---------------

Due to the lack of security support for Python 3.6, the A2B Bus Analyzer SDK has been moved from Python 3.6 to Python 3.8 with this being the only version supported.

User-accessible SDK for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A2B Bus Analyzer 3.0.0 Release Notes
====================================

.. _new-and-noteworthy-4:

New and Noteworthy
------------------

User-accessible SDK
~~~~~~~~~~~~~~~~~~~

To assist with testing and scripting this release includes a user-accessible SDK (UASDK). In order to provide a consistent experience in all operating systems, customers are required to export the SDK to a user-specified location.

To do this in the Help menu select Export User-Accessible SDK which will generate the SDK structure in the chosen folder.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/export_sdk.png
   :width: 300px

The selected folder will contain a uasdk folder with all the required files to use the SDK, including a PDF user guide, the HTML documentation, examples and license. The structure looks like this

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/sdk_folder_struct.png
   :width: 300px

All SDK variants are 64-bit only. The supported bindings are C/C++ and python 3.6.

A2B Bus Analyzer 2.3.0 Release Notes
====================================

.. _new-and-noteworthy-5:

New and Noteworthy
------------------

Emulator: Bulk register access support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This release contains the initial support for generating sequences of register read and writes which can be from the current or other nodes. The support also offers delaying some of the accesses ensuring that previous accesses take place.

These sequences can be stored and loaded in/from files to help with large or well known sequences.


|image3|

Emulator: Multiple Test Tone support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This release includes the ability of generating multiple test tones in the same application where each tone goes to a different stream

Emulator: Multiple channel audio recording
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This release adds the ability of selecting up to two channels when recording audio to a file. Only one channel can be streamed from a .wav.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/multi_channel_save.png
   :width: 600px

A2B Bus Analyzer 2.2.0 Release Notes
====================================

Introduction
------------

This document details updates and changes to A\ :sup:`2`\ B Bus Analyzer on Windows, Linux and macOS as well as minimum hardware requirements and supported versions of each operating system.

This document describes new and noteworthy changes for A\ :sup:`2`\ B Bus Analyzer as well as known issues.

System Hardware Requirements
----------------------------

Verify that your PC meets the following minimum operating system version and requirements to install and run A\ :sup:`2`\ B Bus Analyzer.

The A\ :sup:`2`\ B Bus Analyzer runs on Windows, Linux, and macOS. The Operating Systems table describes the operating system versions supported in this release.

======== ============ =========================================
\        **Platform** **Details**
======== ============ =========================================
|image4| Windows      Windows 10 Home, Pro, Enterprise (64-bit)
|image5| Linux        Ubuntu 18.04+ (64-bit)
|image6| macOS        10.15.x Catalina
======== ============ =========================================

USB
~~~

A\ :sup:`2`\ B Bus Analyzer only supports USB 2.0.

A2B Bus Analyzer Installation
-----------------------------

The A\ :sup:`2`\ B Bus Analyzer installer for each supported platform is described in the table below and they can be downloaded from :doc:`Software Downloads </wiki-migration/resources/tools-software/a2b-bus-analyzer/software-downloads>`.

|image7| ``a2b_bus_analyzer-X.Y.Z-channel-win-x64.exe``

|image8| ``a2b_bus_analyzer-Y.Y.Z-channel-linux-x86_64.AppImage``

|image9| ``a2b_bus_analyzer-X.Y.Z-channel-macos-x64.pkg``

Installation Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~

The following sub-sections include installation information for the supported platforms.

Windows
^^^^^^^

-  To install the A\ :sup:`2`\ B Bus Analyzer, double-click on ``a2b_bus_analyzer-X.Y.Z-channel-win-x64.exe``.
-  The A\ :sup:`2`\ B Bus Analyzer is installed in the following default location: ``C:\Analog Devices\A2B Bus Analyzer``.
-  To uninstall the A\ :sup:`2`\ B Bus Analyzer, go to the Programs and Features applet in the Control Panel.

Linux
^^^^^

-  To install A\ :sup:`2`\ B Bus Analyzer, download the .AppImage. Copy the file into a directory such as ~/Applications.
-  If required, ensure that the downloaded file has execute permissions by running ``chmod a+x a2b_bus_analyzer_*.AppImage``.
-  Launch the A\ :sup:`2`\ B Bus Analyzer by running ``./a2b_bus_analyzer-Y.Y.Z-channel-linux-x86_64.AppImage``.
-  Delete the .AppImage file to uninstall A\ :sup:`2`\ B Bus Analyzer.

A USB device is only accessible if the A\ :sup:`2`\ B Bus Analyzer is run with ``sudo``.

The Linux USB Configuration Script below configures a USB device to be accessible by the user who is currently logged in.

**Linux USB Configuration Script**

::

   #!/bin/sh
    
   # The following is an example script of how to configure your USB on Linux
   # to be accessible by other users.
    
   if [ $(id -u) != 0 ]; then
       echo "You must run this script with sudo:"
       echo "sudo $0 $*" exit 1
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
^^^^^

-  To install theA\ :sup:`2`\ B Bus Analyzer double-click on ``a2b_bus_analyzer-X.Y.Z-channel-macos-x64.pkg``.

   -  If the Installation Wizard does not launch, right-click the ``.pkg`` file and select ``Open with... | Installer``.

-  The A\ :sup:`2`\ B Bus Analyzer is installed in ``/Applications``.

.. _new-and-noteworthy-6:

New and Noteworthy
------------------

AD242x transceiver support
~~~~~~~~~~~~~~~~~~~~~~~~~~

This version includes support for AD242x emulator sub and main which also includes mixed AD242x and AD243x networks. The emulator transceiver drop-down includes the supported devices.

This version also includes an updated A2B (C) Stack version 19.10.0 with bug fixes and improvements to support AD242x.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/ad242x_support.png
   :width: 600px

Bus Monitor
-----------

A\ :sup:`2`\ B Bus Analyzer supports Bus Monitor. For more information on how to set-up and use the Bus Monitor feature, please see our :doc:`Quick Start Guide </wiki-migration/resources/tools-software/a2b-bus-analyzer/quick-start-guide>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/image1.png
   :width: 600px

Emulator Main and Emulator Sub
------------------------------

As well as supporting Bus Monitor, A\ :sup:`2`\ B Bus Analyzer supports utilizing the A2B Bus Analyzer as an emulator for a Main or Sub node. For more information on how to set-up and use the Emulator feature, please see our :doc:`Quick Start Guide </wiki-migration/resources/tools-software/a2b-bus-analyzer/quick-start-guide>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/a2ba120.png
   :width: 600px

Emulator Audio Source
~~~~~~~~~~~~~~~~~~~~~

A\ :sup:`2`\ B Bus Analyzer supports Audio Sourcing from Line In, File In, USB Audio 2.0, Test Tones, and Loopback of bus Audio streams.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/hp.png
   :width: 600px

SPI Data Tunnels
~~~~~~~~~~~~~~~~

As part of the emulator support the A\ :sup:`2`\ B Bus Analyzer contains a new view entitled Data where you can see and control the data sent and received via SPI Data Tunnels. Please see our :doc:`Quick Start Guide </wiki-migration/resources/tools-software/a2b-bus-analyzer/quick-start-guide>` for more information.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/spi.png
   :width: 600px

Quick Start Guide
-----------------

For further A\ :sup:`2`\ B Bus Analyzer documentation, please visit our :doc:`Quick Start Guide </wiki-migration/resources/tools-software/a2b-bus-analyzer/quick-start-guide>`

Support
-------

For technical support contact Analog Devices A2B Bus Analyzer Support at *<fc #4682b4>a2b.analyzer.support@analog.com</fc>*

Known Issues
------------

An up-to-date list of issues can be found at :doc:`Known Issues </wiki-migration/resources/tools-software/a2b-bus-analyzer/known-issues>`

Frequently Asked Questions
--------------------------

An up-to-date list of questions can be found at :doc:`Frequently Asked Questions </wiki-migration/resources/tools-software/a2b-bus-analyzer/faq>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/340_rel_notes_tone_1.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/340_rel_notes_regs_1.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/advanced_regs.png
   :width: 600px
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
