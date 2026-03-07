BeMicro FPGA Project for ADMP441 with Nios driver
=================================================

Supported Devices
-----------------

-  :adi:`ADMP441`

Evaluation Boards
-----------------

-  :adi:`EVAL-ADMP441Z`

Overview
========

This lab presents the steps to setup an environment for using the :adi:`EVAL-ADMP441Z` evaluation board together with the `BeMicro SDK <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`_ USB stick and the Nios II Embedded Development Suite (EDS). Below is presented a picture of the EVAL-ADMP441Z Evaluation Board with the BeMicro SDK Platform.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/admp441_bemicro.jpg
   :alt: admp441_bemicro.jpg
   :align: center
   :width: 400px


.. note::

   See `common_sdp <https://wiki.analog.com/common_sdp>`_


Below is presented a picture of **SDP-B** Controller Board with the **EVAL-ADMP441Z** Evaluation Board.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/admp441_sdp1z.jpg
   :alt: admp441_sdp1z.jpg
   :align: center
   :width: 400px

The **EVAL-ADMP441Z** evaluation board is a member of a growing number of boards available for the **SDP**. It was designed to help customers evaluate performance or quickly prototype new **ADMP441** circuits and reduce design time. When using this evaluation board with the SDP board or BeMicro SDK board, provide a 5 V to 6 V supply to J4.

The :adi:`ADMP441` is a high performance, low power, digital output, omnidirectional MEMS microphone with a bottom port. The complete ADMP441 solution consists of a MEMS sensor, signal conditioning, an analog-to-digital converter, antialiasing filters, power management, and an industry standard 24-bit I2S inter-face. The I2S interface allows the ADMP441 to connect directly to digital processors, such as DSPs and microcontrollers, with-out the need for an audio codec in the system.

The ADMP441 has a high SNR and high sensitivity, making it an excellent choice for far field applications. The ADMP441 has a flat wideband frequency response, resulting in natural sound with high intelligibility.

More information
----------------

-  :adi:`ADMP441 Product Info <ADMP441>` - pricing, samples, datasheet
-  :adi:`EVAL-ADMP441Z evaluation board user guide <media/cn/technical-documentation/user-guides/UG-362.PDF>`
-  `BeMicro SDK <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`_
-  `Nios II Embedded Development Suite (EDS) <http://www.altera.com/devices/processor/nios2>`_

Getting Started
===============

The first objective is to ensure that you have all of the items needed and to install the software tools so that you are ready to create and run the evaluation project.

Hardware Items
--------------

Below is presented the list of required hardware items:

-  Arrow Electronics `BeMicro SDK <https://www.intel.com/content/www/us/en/programmable/b/bemicro-sdk.html>`_ FPGA-based MCU Evaluation Board
-  :adi:`BeMicro SDK/SDP Interposer <sdp-bemicro>` adapter board
-  **EVAL-ADMP441Z** evaluation board
-  Intel Pentium III or compatible Windows PC, running at 866MHz or faster, with a minimum of 512MB of system memory

Software Tools
--------------

Below is presented the list of required software tools:

-  `Quartus II Web Edition <http://www.altera.com/products/software/quartus-ii/web-edition/qts-we-index.html>`_ design software v11.0
-  `Nios II EDS <https://www.altera.com/download/software/nios-ii>`_ v11.0

The **Quartus II** design software and the **Nios II EDS** is available via the Altera Complete Design Suite DVD or by downloading from the web.

Downloads
---------

-  `Lab Design Files <https://wiki.analog.com/_media/{{/resources/fpga/altera/bemicro/admp441_evalboardlab.zip>`_

Extract the Lab Files
---------------------

Create a folder called “\ **ADIEvalBoardLab**\ ” on your PC and extract the **admp441_evalboardlab.zip** archive to this folder. Make sure that there are **NO SPACES** in the directory path. After extracting the archive the following folders should be present in the **ADIEvalBoardLab** folder: **FPGA**, **Software**, **UserInterface**, **NiosCpu**.


.. note::

   See `common_usb <https://wiki.analog.com/common_usb>`_


Quick Evaluation
================


.. note::

   See `common_quick_eval <https://wiki.analog.com/common_quick_eval>`_


FPGA Design
===========


.. note::

   See `common_spi_i2c <https://wiki.analog.com/common_spi_i2c>`_


NIOS II Software Design
=======================


.. note::

   See `common <https://wiki.analog.com/common>`_


Demonstration Project User Interface
====================================

The demonstration project records audio files of 20 seconds length from the two EVAL-ADMP441Z-FLEX boards connected to the EVAL-ADMP441Z board. The audio is recorded at a sample rate of 8 kHz.

To start a recording process, run the ADIEvalBoard/UserInterface/record.bat script. A DOS command prompt window will be opened. This window will be closed after the recording process will be done.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/admp441_interface.png
   :alt: admp441_interface.png
   :align: center
   :width: 500px

The data recorded is saved into the record.wav file, located in the same folder as the record.bat file.

The process can be repeated as many times as needed, but the record.wav file will be overwritten.
