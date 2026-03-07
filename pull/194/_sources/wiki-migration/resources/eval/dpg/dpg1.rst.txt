DPG1
====

The DAC Pattern Generator (DPG) is designed to simplify the evaluation of Analog Devices’ High Speed DAC products. It supports LVCMOS outputs up to 250MSPS and LVDS outputs up to 1.6GSPS.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/dpg1_block_diagram.png
   :align: center

**Please note:** *Analog Devices' pattern generators and high-speed DAC evaluation boards are designed and sold solely to support an efficient and thorough means by which to evaluate Analog Devices high speed DACs in a lab environment for a wide range of end applications. Any application or use of the pattern generators and/or high-speed DAC evaluation boards, other than specified above, will not be supported.*

The DPG1 has been replaced by the :doc:`DPG2 </wiki-migration/resources/eval/dpg/dpg2>`. The DPG1 is no longer sold.

Software
========

The DPG software includes drivers, a generic DLL and a basic user interface program. The Java runtime environment (www.java.com) is required to run the user interface program.

Installation
------------

-  If you don't have Java installed, install it from www.java.com
-  Run the :adi:`setup.exe <static/imported-files/eval_boards/setup.exe>` file

After Installation
------------------

-  Power up the DPG with the included power supply (5V, 8A minimum)
-  Plug the DPG into a USB port
-  The PC will find the new hardware and run the install wizard
-  Run the driver install dialog for the DPG in "auto"
-  If the "found new hardware" dialog comes up a second time, go through it again just like the first time
-  Run the GUI from the icon placed on the desktop. If it can't find the hardware it will tell you, otherwise, everything is ready to go

System Overview
===============

The DAC Pattern Generator is used to play the content of a raw data file on an output port. The generated signal can be used as a stimulus for digital to analog converter testing.

Components
----------

The DAC Pattern Generator consists of the physical module which connects to the Device Under Test (DUT), along with accompanying software.

Connections
-----------

The DAC Pattern Generator has a host control interface through a USB 1.1/2.0 compliant connection to the module. The USB driver on the host provides the physical link communication between the module and the controlling host.

DAC Pattern Generator Concepts
==============================

The primary tasks of the DAC Pattern Generator are to:

-  Convert the contents of a data file into a digital vector
-  Generate a digital signal based on the digital vector

Signal Ports
------------

The module has three ports that operate in a mutually exclusive fashion. The first two are used to interface with LVDS devices, and the third with LVCMOS devices. Each output port type, which is selectable through the application software, represents a distinct mode of operation for the module.

Serialized LVDS Stimulus Port
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The module supports a serialized low voltage differential signal (LVDS) port. When this port is active, the user has the choice of two operational modes based on the output clock and data bit alignment. The clock will either be aligned (coincident) or centered with the data stream.

Direct LVDS Stimulus Port
~~~~~~~~~~~~~~~~~~~~~~~~~

The module supports a direct-connect low voltage differential signal port. When this port is active, the user has the choice of three operational modes.

The first mode is used for SDR data transmission. The second and third modes are used for DDR data transmission. The data clock edge is placed between the data bit edges (with clock delay) for the second mode, and the data clock edge is coincident with the data bit edges (without clock delay) for the third mode.

LVCMOS Stimulus Port
~~~~~~~~~~~~~~~~~~~~

The module supports a Low Voltage CMOS port. When this port is active, the user has the choice of two operation modes: single port or dual port. Two data streams are required for this mode, and will be referred to as the I and the Q streams. In the single port mode, the data from the two streams will be generated alternately on the single shared 16-bit data port. In the dual port mode, both data streams will be played simultaneously on the 32-bit data port.

SPI Interface
~~~~~~~~~~~~~

The SPI port provides a direct interface with the DAC.

.. hint::

   \ **Note: Clock And Data Alignment** When running in LVDS HS mode, the firmware executes a clock tuning algorithm based on the mode settings (aligned or centered). This algorithm is triggered when data playback is started.

   
   The hardware implementation for the tuning is based on Programmable Delay Controllers, which are unfortunately susceptible to temperature variations. What this means is that if a playback is started when the device is still cold, the clock and data may eventually be misaligned as the board heats up.
   
   This may be corrected by either restarting the playback or from the “Re-Tune” button in the Tuning dialog.


Hardware
========

The DAC Pattern Generator connects to the ADI. development boards using board-to-board connectors in both the serialized and direct LVDS modes, and a cable for the LVCMOS mode.

The DAC Pattern Generator also has a host control interface through a USB 1.1/2.0 compatible connection to the module and an SPI connection to the ADI development board.

It must be noted that the board does not provide ESD protection for the signals routed to external connectors.

Support
=======

Please contact `DPG Support <https://wiki.analog.com/mailto/dpg.support@analog.com>`_ with any additional questions regarding the DPG or DAC Software Suite.
