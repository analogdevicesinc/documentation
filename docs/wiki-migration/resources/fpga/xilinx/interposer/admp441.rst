ADMP441 FMC-SDP Interposer & Evaluation Board / Xilinx KC705 Reference Design
=============================================================================

Supported Devices
-----------------

-  :adi:`ADMP441`

Evaluation Boards
-----------------

-  :adi:`EVAL-ADMP441Z`

Overview
========

This document presents the steps to setup an environment for using the :adi:`EVAL-ADMP441Z <en/audiovideo-products/mems-microphones/admp441/products/EVAL-ADMP441Z/eb.html>` evaluation board together with the Xilinx KC705 FPGA board and the Xilinx Embedded Development Kit (EDK). Below is presented a picture of the EVAL-ADMP441Z Evaluation Board with the Xilinx KC705 board.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/admp441.jpg
   :alt: admp441.jpg
   :align: center
   :width: 400px


.. note::

   See `common_sdp <https://wiki.analog.com/common_sdp>`_


Below is presented a picture of **SDP-B** Controller Board with the **EVAL-ADMP441Z** Evaluation Board.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/admp441_sdp.jpg
   :alt: admp441_sdp.jpg
   :align: center
   :width: 400px

The :adi:`ADMP441` is a high performance, low power, digital output, omnidirectional MEMS microphone with a bottom port. The complete ADMP441 solution consists of a MEMS sensor, signal conditioning, an analog-to-digital converter, antialiasing filters, power management, and an industry standard 24-bit I2S inter-face. The I2S interface allows the ADMP441 to connect directly to digital processors, such as DSPs and microcontrollers, with-out the need for an audio codec in the system. The ADMP441 has a high SNR and high sensitivity, making it an excellent choice for far field applications. The ADMP441 has a flat wideband frequency response, resulting in natural sound with high intelligibility. A built-in particle filter provides high reliability.

The :adi:`EVAL-ADMP441Z <en/audiovideo-products/mems-microphones/admp441/products/EVAL-ADMP441Z/eb.html>` is a simple evaluation board that allows quick evaluation of the performance of the ADMP441 MEMS microphone. The small size and low profile of the flexible PCB enables direct placement of the microphone into a prototype or an existing design for an in situ evaluation. The EVAL-ADMP441Z-FLEX consists of an ADMP441 microphone soldered to a flexible PCB. The only other component on the board is a 0.1 μF supply bypass capacitor.

More information
----------------

-  :adi:`ADMP441 Product Info <ADMP441>` - pricing, samples, datasheet
-

|EVAL-ADMP441Z evaluation board user guide|

-  `Xilinx KC705 FPGA board <https://www.xilinx.com/products/boards-and-kits/EK-K7-KC705-G.htm>`_

Getting Started
===============

The first objective is to ensure that you have all of the items needed and to install the software tools so that you are ready to create and run the evaluation project.

Required Hardware
-----------------

-  `Xilinx KC705 FPGA board <https://www.xilinx.com/products/boards-and-kits/EK-K7-KC705-G.htm>`_
-  FMC-SDP adapter board
-  **EVAL-ADMP441Z** evaluation board

Required Software
-----------------

-  Xilinx ISE 13.4
-  A UART terminal (ex. TeraTerm / Hyperterminal).

Downloads
---------

-  `Reference Design Files <https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/admp441_evalboard.zip>`_

The following table presents a short description the reference design archive contents.

+-------------+-------------------------------------------------------------------------------------------------------+
| **Folder**  | **Description**                                                                                       |
+=============+=======================================================================================================+
| Bit         | Contains the KC705 configuration file that can be used to program the system for quick evaluation.    |
+-------------+-------------------------------------------------------------------------------------------------------+
| DataCapture | Contains the script used to read data from the ADMP441 and save it into a file on the PC.             |
+-------------+-------------------------------------------------------------------------------------------------------+
| Microblaze  | Contains the EDK 13.2 project for the Microblaze softcore that will be implemented in the KC705 FPGA. |
+-------------+-------------------------------------------------------------------------------------------------------+
| Software    | Contains the source files of the software project that will be run by the Microblaze processor.       |
+-------------+-------------------------------------------------------------------------------------------------------+

Run the Demonstration Project
=============================

Hardware Setup
--------------

.. important::

   Before connecting the ADI evaluation board to the Xilinx KC705 make sure that the VADJ_FPGA voltage of the KC705 is set to 3.3V. For more details on how to change the setting for VADJ_FPGA visit the Xilinx KC705 product page.


-  Use the FMC-SDP interposer to connect the ADI evaluation board to the Xilinx KC705 board on the FMC LPC connector.
-  Connect the JTAG and UART cables to the KC705 and power up the FPGA board.
-  Start IMPACT, and double click “\ *Boundary Scan*\ ”. Right click and select *Initialize Chain*. The program should recognize the Kintex 7 device (see screenshot below).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/impact_config.png
   :alt: impact_config.png
   :align: center
   :width: 300px

-  Program the KC705 FPGA using the "*Bit/download.bit*" file provided in the reference design archive.
-  Power the ADI evaluation board.
-  Start a UART terminal and set the baud rate to 115200 bps.

At this point everything is set up and it is possible to start the evaluation of the ADI hardware. To capture data from the microphones run the *data_capture.bat* script located in the *DataCapture* folder from the reference design .zip file. Every time the script is run, 20 seconds of audio data is recorded at 25000 Hz sample rate, and saved in **EVAL_ADMP441Z_Demo.wav**. The user can change the sample rate by modifying the value stored in Timer0, and the duration of the recording in seconds, by modifying the nrSeconds variable in **main.c**. The sample rate is calculated according to the period of the WS signal. If the user chooses to modify the duration of the recording, modifications must also be made in the tcl script in order to acquire the desired number of samples (for 20 seconds of audio data, the script acquires data for 10 \* 100000 times).

.. tip::

   The first time the data capture script is run it is possible that an error will occur while the script is trying to connect to the system. Just run the script again and the error shouldn't appear anymore. The same applies if you do not see any waveforms on the WS or SCLK pins on the evaluation board.


.. _more-information-1:

More information
================


.. note::

   See `ez_common <https://wiki.analog.com/ez_common>`_


.. |EVAL-ADMP441Z evaluation board user guide| image:: http://www.analog.com/static/imported-files/user_guides/UG-303.pdf
