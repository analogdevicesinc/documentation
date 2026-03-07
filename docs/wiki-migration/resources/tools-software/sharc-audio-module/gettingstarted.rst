Getting Started
===============

The :adi:`SHARC Audio Module <sharcaudiomodule>` development environment is Analog Devices' :adi:`CrossCore Embedded Studio <cces>`. Requirements and additional information can be found in the installation section below.

Pre-Requisites and Requirements List
====================================

There are a few things needed in order to successfully complete all the tutorials

-  Windows PC or laptop computer
-  :adi:`ICE-1000/ICE-2000 JTAG Emulator <ice1000>`
-  :doc:`SHARC Audio Module </wiki-migration/resources/tools-software/sharc-audio-module/hardware/main-board>`
-  :doc:`Audio Project Fin </wiki-migration/resources/tools-software/sharc-audio-module/hardware/audioproj-fin>`
-  `3.5mm Stereo Plug/Plug M/M Cable - Black <https://www.monoprice.com/product?p_id=644>`_ or equivalent
-  `1/4in TRS Male to Male Cable <https://www.monoprice.com/product?c_id=115&cp_id=11509&cs_id=1150901&p_id=4793&seq=1&format=2>`_ or equivalent
-  `S/PDIF (Toslink) Digital Optical Audio Cable <https://www.monoprice.com/product?p_id=6273>`_
-  Powered speakers

Installing and Activating CrossCore Embedded Studio
===================================================

.. admonition:: Download
   :class: download

   
   **Download CrossCore Embedded Studio 2.8.0 or greater:**
   
   .. container:: indent

      :adi:`CrossCore Embedded Studio <cces>`

   


**Note:** It is recommended that you install into the default directories recommended by the CrossCore Embedded Studios installer. This way all the instructions and support provided will be easier.

To install CrossCore Embedded Studio, double-click the installer executable (e.g. ``ADI_CrossCoreEmbeddedStudio-Rel2.10.0.exe``). By default the installer places all necessary components in the ``C:\Analog Devices\CrossCore Embedded Studio 2.10.0`` directory.

The first time you launch CrossCore Embedded Studio, you will be prompted to input a serial number, name, and email address. The serial number for **ALL** SHARC Audio Module boards is:

.. important::

   
   | **SHARC Audio Module CrossCore Serial Number**
   | ``EZK-CCES-9FYX-DSAC-FPNV-4WVP-E5X4-VGKC-GI01``
   


The New License Wizard will guide you through the process.

-  Select Yes to install a license at this time.
-  Choose "I have a serial number that I would like to activate" and click Next.
-  Enter the serial number above and click Next.
-  Choose "Install and activate a license on-line all in one step" and click Next.
-  Complete your name and address and click Finish.
-  Once you see the "Your license has been successfully activated" message click OK.

Once the serial number has been activated, the CrossCore development tools will be enabled to allow you to connect to the ADSP-SC589 processor using an ICE-1000 emulator.

.. warning::

   This license will only allow the use of ICE-1000 emulator hardware with CCES. If you have an ICE-2000 you will need a full CCES license.


Installing the SHARC Audio Module Bare Metal SDK
================================================

.. admonition:: Download
   :class: download

   **SHARC Audio Module Bare Metal SDK 2.2.0(LATEST-Needed for SHARC Audio Module HW rev 2.1+)**

   
   Click the link to the release notes below to see the full list of changes in this release.
   
   |
   
   .. container:: indent

      |image1| `Release Notes for SHARC Audio Module Bare Metal SDK 2.2.0 <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/release_notes_for_sharc_audio_module_bare_metal_sdk_2.2.0.pdf>`_

      | |image2| `Microsoft Windows Installer (.exe) <https://download.analog.com/tools/sharcaudiomodule/baremetal/releases/2.2.0/ADI_SAM_BareMetal_SDK-Rel2.2.0.exe>`_

   


.. admonition:: Download
   :class: download

   **SHARC Audio Module Bare Metal SDK 2.1.2**

   
   Click the link to the release notes below to see the full list of changes in this release.
   
   |
   
   .. container:: indent

      |image3| `Release Notes for SHARC Audio Module Bare Metal SDK 2.1.2 <http://download.analog.com/tools/sharcaudiomodule/baremetal/releases/2.1.2/SAM_BareMetal_SDK_2.1.2_Release_Notes.pdf>`_

      | |image4| `Microsoft Windows Installer (.exe) <http://download.analog.com/tools/sharcaudiomodule/baremetal/releases/2.1.2/ADI_SAM_BareMetal_SDK-Rel2.1.2.exe>`_

   


Configuring The Hardware For Use With CCES
==========================================

.. important::

   When using CCES, the emulator can introduce some noise into the audio output stream when running. Disconnecting from CCES will produce an unaltered audio stream.


In order to use the ICE-1000 to connect to the SHARC Audio Module main board be sure to connect the adapter and cable to the ICE-1000 as shown below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/ice_connections.jpg
   :width: 600px

The SHARC Audio Module main board must be powered and the ICE-1000 emulator must be connected to P1(DEBUG) as shown below:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/sam_connections.jpg
   :width: 600px

Help and Support
================

Do you need help or have general support questions, then this section helps you resolve those.

This section should give you all the information you need to contact someone that can help answer your questions.

Also, check out our :doc:`Troubleshooting </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/troubleshooting>` page for solutions to common problems with the SHARC Audio Module, CrossCore Embedded Studio 2.8.0, and the bare metal framework.

Hardware, Software, and Documentation Questions
-----------------------------------------------

If you have questions on the SHARC Audio Module hardware or software or if you just want to show off your latest creation please visit the :ez:`SHARC Audio Module EngineerZone forum <dsp/software-and-development-tools/sharcaudiomodule>`.

When asking a question please take the time to give a detailed description of your problem. If you are experiencing a problem please state the steps you have executed, the result you expected you would get and the result you actually got. By doing so you enable us to provide you precise and detailed answers in a timely manner.

.. tip::

   Before asking questions please take the time to check if somebody else already asked the same question. You might just find your question already answered.


CrossCore Embedded Studio Questions
-----------------------------------

If you have questions regarding the tools and tool chain that is used with the SHARC Audio Module, either post a question or send an email.

-  :ez:`CrossCore Embedded Studio support community <community/dsp/software-and-development-tools/cces>` for questions about:

   -  Download/Install issues
   -  Build, debug, run, issues
   -  Other tools related issues

-  The CrossCore Embedded Studio team can also be emailed using the address below:

   -  `processor.tools.support@analog.com <https://wiki.analog.com/mailto/processor.tools.support@analog.com>`_

Getting Familiar with CCES
==========================

If already familiar with CCES, continue on to the **Next** page using the Navigation section at the bottom of the page.

If not familiar with CCES, please go through the :doc:`CCES Getting Started Guide </wiki-migration/resources/tools-software/crosscore/cces/getting-started>` prior to beginning the :doc:`Bare Metal Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal>` page.

After completing the :doc:`Bare Metal Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal>` there are various tutorials to go through in order to get familiar with the bare metal framework. It is recommended that you run the :doc:`Bare Metal Project Wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>` to create a starting point for each tutorial. Once you have a starting point, you can update specific options as needed. The tutorials will walk through changes that can be made to the code in order to get familiar with the various features that the framework provides.

Linux Add-In for the SHARC Audio Module
=======================================

CrossCore Embedded Studio provides support for the SHARC Audio Module. Please refer to the :doc:`Linux for ADSP-SC5xx Processors page </wiki-migration/resources/tools-software/linuxdsp>` for more information.

Audio Elements and Effects
==========================

Check out our :doc:`audio elements and effects section </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/audio-elements>` for information about the audio elements and effects that can be used with the baremetal framework.

--------------

`SHARC Audio Module#.|SHARC Audio Module#.baremetal|Bare Metal Framework <https://wiki.analog.com/_media/navigation SHARC Audio Module#.>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/pdf-icon.png
   :width: 16px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/windows-icon.png
   :width: 16px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/pdf-icon.png
   :width: 16px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/windows-icon.png
   :width: 16px
