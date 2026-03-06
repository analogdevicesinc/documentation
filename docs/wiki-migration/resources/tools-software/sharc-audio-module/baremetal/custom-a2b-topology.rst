Custom A2B Configuration for SHARC Audio Module
===============================================

This page describes the steps necessary to create A2B topologies (system configuration files) different to the :doc:`fixed topologies </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/preconfigured-a2b-topology>` currently supplied with the SHARC Audio Module (SAM) Baremetal Framework SDK.

The setup discussed on this page consists of the SHARC Audio Module, used in combination with the EVAL-AD2428WB1BZ and ADZS-AUDIOA2BAMP class-D amplifier A2B slave boards, as per the A2B SigmaStudio `schematics <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/demo_sam-wb1bz-classdamp.zip>`__.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/a2b_custom_ss.png
   :width: 800px

Required Software Components
----------------------------

The following software components must be installed prior to using this custom demo:

-  :adi:`CrossCore Embedded Studio(CCES) <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html>` development tools (version 2.9.2)
-  :doc:`SHARC Audio Module Bare Metal SDK </wiki-migration/resources/tools-software/sharc-audio-module/gettingstarted>` (version 2.1.1)
-  :adi:`SigmaStudio <en/design-center/evaluation-hardware-and-software/software/ss_sigst_02.html>` (version 4.5)
-  :adi:`A2B Software package <en/design-center/evaluation-hardware-and-software/software/a2b-software.html>` (version 19.3.1)

.. important::

   After installing this package, copy **A2B.dll** and **A2Bstack.dll** from the "*\\GUI\\x86_x64*" folder into "*C:\\Program Files\\Analog Devices\\SigmaStudio 4.5*" before launching SigmaStudio


-  Extract the supplied .zip file: `Demo SAM-WB1BZ-ClassDAmp.zip <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/demo_sam-wb1bz-classdamp.zip>`__

Required Hardware Components
----------------------------

The following hardware components are required to run this custom demo:

-  :adi:`ADZS-SC589-MINI SHARC Audio Module <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sharc-audio-module.html>` (master board)
-  :adi:`EVAL-AD2428WB1BZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD2428WB1BZ.html>` (slave board)
-  :adi:`ADZS-AUDIOA2BAMP <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADZS-AUDIOA2BAMP.html>` (slave board)
-  :adi:`ADZS-USBI2EZB <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-adusb2ebz.html>` (USBi programmer)
-  :adi:`ICE 1000/2000 JTAG Emulator <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/emulators.html>`
-  Two A2B® cables
-  Two passive speakers
-  Stereo aux cables and headphones

Hardware Setup
--------------

The hardware setup and audio routing used for running this particular custom demo consists of the following:

-  Audio source (Line In) into SHARC Audio Module
-  A2B routing from SAM(master) to AD2428WB1BZ (slave 0)
-  AD2428WB1BZ audio sink (Line Out)
-  A2B routing from AD2428WB1BZ (slave 0) to AUDIOA2BAMP (slave 1)
-  AUDIOA2BAMP Class-D amplifier to audio sink (passive speakers)

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/a2b_hw_setup.png
   :width: 600px

Creating Topology Files For the Bare Metal Framework
----------------------------------------------------

The following steps describe the procedure required for running the demo:

.. important::

   For this tutorial, the SigmaStudio schematics from the zip file will be used.


-  The custom A2B topology system configuration files need to be generated using SigmaStudio.
-  Create new System Config Files by clicking "Link, compile and download" for the "Demo SAM-WB1BZ-ClassDAmp (RevA).dspproj" project schematics.
-  After successful compilation, right click on the "Target Processor" and select "Export System Config Files.."

|image1|

-  The “Export A2B Configuration Files” pop-up window will appear

|image2|

-  Be sure to set the appropriate settings to generate the new A2B topology configuration file.
-  Click OK and then close the window (it doesn't automatically close)

Adding Topology Files To the Bare Metal Framework
-------------------------------------------------

Use the Bare Metal Project Wizard to create a project that the topology files will be integrated into.

.. tip::

   Reference the :doc:`Bare Metal Project Wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>` page for help creating a project.


The Bare Metal Project Wizard for the SHARC Audio Module Bare Metal SDK version 2.1.0 does not support custom hardware configurations. For purposes of this exercise, you should select one of the two options on the **A2B module Selection** page: *Class-D Amplifier A2B Module* or *Another SHARC Audio Module*.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/bm_wizard_options.png
   :width: 600px

-  Copy the previously A2B configuration header file to the SAM A2B topologies folder in the newly created bare metal project


|image3|

-  In CrossCore Embedded Studio (CCES 2.8.3 or later), a few code edits are required so that this new A2B configuration file can be invoked from the framework.

   -  Under core0 -> src -> common, edit the “audio_system_config.h” file to add the new topology, as shown below:


   |image4|

   -  Next, under core0 -> src -> audio_frameworks, navigate to “audio_framework_8ch_sam_and_audioproj_fin_arm.c”. Add the new A2B configuration, as shown below. Include the previously created header file “adi_a2b_i2c_commandlist_SAM_WBZ_Amp.h”

   |image5|

-  At this stage, the newly created A2B topology should be properly configured and ready to be compiled and downloaded to the SHARC Audio Module board.

.. tip::

   For details on the default audio routing to the A2B bus, under core1 → src, navigate to “callback_audio_processing.cpp”. Also, refer to SigmaStudio “Stream Config” under “Target Processor” for more details on the configured streams.


Executing the Code in CCES
--------------------------

|

.. tip::

   Some knowledge of CrossCore Embedded Studio(CCES) is assumed here. If unfamiliar with CCES, please go through the :doc:`CCES Getting Started Guide </wiki-migration/resources/tools-software/crosscore/cces/getting-started>` prior to working in CCES.


   |image6|

-  Build all 3 core projects
-  Create the debug configuration to load all 3 cores using the ICE-1000
-  After creating the debug configuration, click Debug
-  Core 0 needs to run first to release the 2 SHARC cores so that they run to main
-  Once the SHARC cores are at main, run both cores
-  Be sure you have audio input to the board
-  You should hear audio a few octaves higher than expected


--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#preconfigured-a2b-topology
   :alt: Using Pre-configured A2B Topology Files#.|Bare Metal Framework#driver-creation-tutorial|Creating Drivers for New Audio Components

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/export_ss.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/a2b_export_config.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/a2b_header_file.png
   :width: 700px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/a2b_config_update.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/a2b_topology_include.png
   :width: 700px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/a2b_debug_configuration.png
   :width: 500px
