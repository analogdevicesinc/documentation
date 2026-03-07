Download no-OS
==============

The source code of the no-OS software and the scripts can be downloaded from the Analog Devices github.

.. admonition:: Download
   :class: download

   
   -  **AD9361 Example project** :git-no-OS:`projects/ad9361`
   -  **AD9361 Generic Driver** :git-no-OS:`drivers/rf-transceiver/ad9361`
   -  **Linux Makefile** :git-no-OS:`projects/ad9361/src/Makefile.linux`
   


Download HDL
============

.. note::

   Please note that the projects **FMCOMMS2**, **FMCOMMS3** and **FMCOMMS4** are using the :git-hdl:`same <projects/fmcomms2>` hdl design. The **ARRADIO** Quartus project uses :git-hdl:`Arradio <projects/arradio/c5soc>` hdl design.


.. include:: ../../../fpga/docs/hdl/downloads_insert.rst .. include:: ../../../fpga/docs/hdl/downloads_insert.rst .. include:: ../../../fpga/docs/hdl/downloads_insert.rst

Download Linux Image
====================

The **BOLD** is what you should type. It's not too much more than `Special Agent Oso <https://en.wikipedia.org/wiki/Special Agent Oso>`_'s three special steps, and it also allows you to go for that specialty coffee you have been craving.

For different platforms you'll need different images. Currently we provide a single pre-build images, that can work on all the platforms we support.

.. important::

   Make sure you unzip the image using either `7-zip <https://www.7-zip.org/>`_ or on Linux it can be done via command-line **xz -d <image_name>.img.xz**. The actual file that needs to be dumped to the SD card has to have the **\*.img** extension.


.. important::

   Your SD-card needs to be at least 16 GB for releases 2019-R2 and newer. Or 8 GB for older releases.


.. warning::

   If your computer has security restrictions imposed by your company's IT department, which prevent your from writing data to SD-cards (or the data is encrypted when written on the SD-card), then consider using a computer that doesn't have such restrictions, or communicating with your IT department to find a solution.


.. admonition:: Download
   :class: download

   
   -  :doc:`Download Release Images </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>`
   


Now, depending if you are using Linux or Windows, follow these instructions to write the file to your SD card.

-  :doc:`Linux Hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>`
-  :doc:`Windows Hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>`

Download Filters
================

.. important::

   \ **PREREQUISITES**

   
   In order to run the wizard, your `MATLAB <https://www.mathworks.com/products/matlab/>`_ license needs to include the following components:
   
   -  MATLAB (R2015b or higher version is required)
   -  Signal Processing Toolbox
   -  DSP System Toolbox
   
   In addition, in order to generate HDL, your `MATLAB <https://www.mathworks.com/products/matlab/>`_ license needs to include the following component:
   
   -  Fixed-Point Designer
   


In order to get the wizard, please go to Analog Devices GitHub. Different releases of AD9361 Filter Design Wizard and their source files can be found here:

.. admonition:: Download
   :class: download

   
   -  :git-ad936x-filter-wizard:`releases`
   -  For each release, the wizard is available as a MATLAB App installer (mlappinstall) or in archive form (zip or tarball).
   


For more information about install and running MATLAB apps, please refer to: http://www.mathworks.com/help/matlab/creating_guis/install-and-run-app.html

If using a checkout or unpacked archive, the application can be run in one of two ways:

-  Right click "AD9361_Filter_Wizard.fig" and select "Open in GUIDE" to open the figure. Then type "Ctrl+T" to run the figure.
-  Within the application directory run the command "AD9361_Filter_Wizard" from the MATLAB command line.

The Filter Design Wizard has been applied in the RF Blockset (formerly SimRF) models of AD9361, provided by MathWorks as a hardware support package. **Download this version if to be used with the AD9361 RF Blockset (formerly SimRF) model:**

.. admonition:: Download
   :class: download

   
   -  `AD9361 Filter Design Wizard for RF Blockset (formerly SimRF) Model <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/ad9361_filter_design_wizard_v2.mlappinstall>`_
   


To learn more about AD9361 modeling and to download the Tx and Rx models, the hardware support package can be found here:

.. note::

   
   -  http://www.mathworks.com/hardware-support/analog-devices-rf-transceivers.html
   


Download IIO-Oscilloscope
=========================

.. admonition:: Download
   :class: download

   Latest releases (goto this page to download the file):

   
   -  :git-iio-oscilloscope:`releases`
   


Download Libiio
===============

The libiio library can be obtained on the `Github <http://github.com/analogdevicesinc/libiio>`_ page of the project.

Libiio installer for Windows
----------------------------

.. admonition:: Download
   :class: download

   
   -  :git-libiio:`Installer for latest stable build (Windows 32-bit / 64-bit) <releases>`
   -  `Installer for latest nighty build (Windows 32-bit / 64-bit) <https://ci.appveyor.com/project/analogdevicesinc/libiio/build/artifacts?branch=master>`_ (may be unstable / buggy)
   

