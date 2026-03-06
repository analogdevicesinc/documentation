FMC-SDP Interposer Board Test / Xilinx KC705 Reference Design
=============================================================

Overview
========

This document presents the steps to setup an environment for testing the **FMC-SDP Interposer Board** together with the **ADZS-BRKOUT-EX3** SDP breakout board, the Xilinx KC705 FPGA board and the Xilinx Embedded Development Kit (EDK). Below is presented a picture of the test system setup using the the Xilinx KC705 board.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/sdp_brkout.jpg
   :alt: sdp_brkout.jpg
   :align: center
   :width: 400px

More information
----------------

-  `Xilinx KC705 FPGA board <https://www.xilinx.com/products/boards-and-kits/EK-K7-KC705-G.htm>`__

Getting Started
===============

The first objective is to ensure that you have all of the items needed and to install the software tools so that you are ready to create and run the evaluation project.

Required Hardware
-----------------

-  `Xilinx KC705 FPGA board <https://www.xilinx.com/products/boards-and-kits/EK-K7-KC705-G.htm>`__
-  **FMC-SDP interposer board**
-  **ADZS-BRKOUT-EX3** evaluation board

Required Software
-----------------

-  Xilinx ISE 13.4 (Programmer (IMPACT) is sufficient for the demo and is available on Webpack).

Downloads
---------

-  `Reference Design Files <https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/fmc_sdp_test.zip>`__

The following table presents a short description the reference design archive contents.

+------------+-------------------------------------------------------------------------------------------------------+
| **Folder** | **Description**                                                                                       |
+============+=======================================================================================================+
| Bit        | Contains the KC705 configuration file that can be used to program the system for quick evaluation.    |
+------------+-------------------------------------------------------------------------------------------------------+
| Microblaze | Contains the EDK 13.4 project for the Microblaze softcore that will be implemented in the KC705 FPGA. |
+------------+-------------------------------------------------------------------------------------------------------+
| Software   | Contains the source files of the software project that will be run by the Microblaze processor.       |
+------------+-------------------------------------------------------------------------------------------------------+

Testing procedure
=================

The testing of the FMC-SDP adapter board is carried out by checking the connectivity between the board’s pins. This is done by connecting the pins in pairs, applying a digital 1 on one pin form each pair and reading back the value on the other pin. All the pins are tested except the CON_RESETOUT which resets the adapter board. The IC pins are tested by checking that the level on these pins corresponds to a logic 1. The following steps must be performed for testing the FMC-SDP adapter board:

-  Connect all the hardware items as shown in Fig. 1 and power up the system.
-  Connect the UART port of the Xilinx KC705 board to the PC.
-  On the PC start a UART terminal (ex. TeraTerm) and configure the serial port liked to the KC705 to Baud Rate: 57600, Data length: 8bit, Parity: None, Stop bits: 1 bit, Flow control: none.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/baud_config.png
   :width: 300px

-  Program the Xilinx KC705 adapter board with the **“download.bit”** file provided in the test project archive in the **Bit** folder. Programming is done using the Xilinx Impact application.
-  After the FPGA is programmed the test will start automatically and on the terminal window the test status will be displayed. If any errors are detected the application will list the pins on which the errors were detected.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/test_output.png
   :width: 300px

-  A new test can be run by pressing any key.

.. _more-information-1:

More information
================


.. note::

   See `ez_common <https://wiki.analog.com/ez_common>`__

