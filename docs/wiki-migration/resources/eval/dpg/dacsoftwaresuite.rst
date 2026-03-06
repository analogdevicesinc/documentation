Prerequisites
=============

The following items are required before the DAC Software Suite can be installed. If they are not present on your system before the DAC Software Suite Setup is run, setup will install them automatically:

-  Microsoft Windows Installer 3.1 or later
-  Microsoft .NET Framework version 3.5 SP1
-  National Instruments VISA Runtime Version 4.6.2 or later
-  National Instruments LabVIEW Runtime Version 7.1.1 (later versions are not compatible)
-  National Instruments LabVIEW Runtime Version 2009 SP1 (later versions are not compatible)

Supported Hardware
------------------

-  `dpg1 <https://wiki.analog.com/dpg1>`__\  [1]_
-  `dpg2 <https://wiki.analog.com/dpg2>`__
-  `dpg3 <https://wiki.analog.com/dpg3>`__
-  DPGI/O
-  :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>`
-  `ADS7-V1/-V2 <https://wiki.analog.com/ads7>`__
-  All High-Speed DAC evaluation boards with USB

Downloading
-----------

.. tip::

   The DAC Software Suite is no longer maintained. See :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` available bundled with :adi:`ace` which supports many DAC products.


The latest edition of the full DAC Software Suite can be downloaded from the Software section of the following page:

:adi:`DAC Software Suite 1.3.77.154 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-DPG3.html#eb-relatedsoftware>` Updated 16-May-2018

Installation
------------

.. tip::

   \ **Administrator Privileges:** Administrator privileges are required to install the DAC Software Suite.

   
   **Upgrading:** Previous versions of the DAC Software Suite do not need to be un-installed before installing a newer version. The installer will automatically upgrade from any existing versions already installed.


Run the setup program. The following screen will be displayed after the installer loads:

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/install_1.png
   :align: center

Read the Analog Devices Software License Agreement. If you accept the terms of the agreement, click I Agree.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/install_2.png
   :align: center

The installer can check online to ensure the version you are installing is the latest. You can choose not to allow the installer to check online.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/install_3.png
   :align: center

The Choose Components page allows you to select which components of the DAC Software Suite you would like to install. The installer will automatically select the best option for your system. The prerequisites will only be selected if the installer determines they are not present on your system. The various software interfaces will only be selected if the corresponding software package is already installed. Therefore, install the DAC Software Suite after installing other software you would like to use with the DPG (for example, Visual Analog.)

.. important::

   **Warning:** If you have another vendor's VISA libraries installed (for example, the Agilent IO Libraries), you should not install the NI-VISA runtime from within the DAC Software Suite Setup. NI-VISA will need to be manually installed according to both National Instruments' and your 3rd party VISA library's instructions, before installing the DAC Software Suite. For more information on NI-VISA, see http://www.ni.com/visa


.. image:: https://wiki.analog.com/_media/resources/eval/dpg/install_4.png
   :align: center

For most users, the default install location should be used. Some software interfaces may not function properly if the default directory is changed.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/install_5.png
   :align: center

This screen allows you to change the location where shortcuts to various parts of the DAC Suite will be installed. Press Next to begin the installation.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/install_6.png
   :align: center

During the installation, a progress bar will be displayed, with various status messages appearing above it. Depending on what prerequisites need to be installed, the process may take up to an hour or more. Additional installers may be displayed as part of the prerequisites install process. Proceed through those installers with the default options.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/install_7.png
   :align: center

The main software installation is now complete. Press Next to select which evaluation boards you will be using.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/install_9.png
   :align: center

This screen lists the available evaluation boards. Select which boards you will be using and click Next. Additional boards may be added at any time in the future.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/install_10.png
   :align: center

The installation is now complete.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/install_11.png
   :align: center

DPGDownloader
-------------

DPGDownloader is an application created for quickly and easily interfacing with DPGs for creating, loading, and playing data vectors. For complete documentation, see the `dpgdownloader <https://wiki.analog.com/dpgdownloader>`__ page.

VisualAnalog™
-------------

For designers who are selecting or evaluating high speed ADCs, VisualAnalog(tm) is a software package that combines a powerful set of simulation and data analysis tools with a user-friendly graphical interface. An interface to DPGs allows for evaluation of DACs and mixed-signal converters in the software package. For more information, see the :adi:`Visual Analog <visualanalog>` page.

.. tip::

   To use VisualAnalog with a DPG, the DAC Software Suite must be installed after VisualAnalog is installed. If the DAC Software Suite was installed first, the installer should be run again to install the DPG interface into VisualAnalog.


Interfacing to 3rd Party Applications
-------------------------------------

Applications besides DPGDownloader and VisualAnalog can communicate directly with the DPGs. Interfacing with several popular applications is described below, followed by the general `programming_reference <https://wiki.analog.com/programming_reference>`__ which is used with all applications.

-  `LabVIEW 7 <https://wiki.analog.com/labview7>`__
-  `labview_8 <https://wiki.analog.com/labview_8>`__
-  `matlab <https://wiki.analog.com/matlab>`__
-  `vee <https://wiki.analog.com/vee>`__

See the `programming_reference <https://wiki.analog.com/programming_reference>`__ for the methods and properties that are used with all applications.

Support
-------

Please contact `DPG Support <https://wiki.analog.com/mailto/dpg.support@analog.com>`__ with any additional questions regarding the DPG or DAC Software Suite.

.. [1]
   The DPG1 is not supported by DPGDownloader, however the installer for the DPG1 software is included in the DAC Software Suite.
