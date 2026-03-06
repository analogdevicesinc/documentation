DPG2
====

The Data Pattern Generator is a bench-top instrument for driving vectors into Analog Devices' high-speed Digital-to-Analog converters. The DPG connects to a PC over USB, and allows a user to download a vector from their PC into the DPG’s internal memory. Once downloaded, the vector can be played out to an attached Evaluation Board for a specific DAC at full speed. This allows for rapid evaluation of the DAC with both generic and customer-generated test data.

**Please note:** *Analog Devices' pattern generators and high-speed DAC evaluation boards are designed and sold solely to support an efficient and thorough means by which to evaluate Analog Devices high speed DACs in a lab environment for a wide range of end applications. Any application or use of the pattern generators and/or high-speed DAC evaluation boards, other than specified above, will not be supported.*

The DPG2 has been replaced by the :doc:`DPG3 </wiki-migration/resources/eval/dpg/dpg3>`. For information on the software used to control the DPG2 and DPG3, see the :doc:`High-Speed DAC Software Suite </wiki-migration/resources/eval/dpg/dacsoftwaresuite>` page.

Ordering Code
=============

The part number for the DPG2 is AD-DAC-DPG-BZ.

Hardware Specifications
=======================

*Please note that not all hardware options and specifications are supported with any particular evaluation board or software package. Specifications are subject to change without notice.*

-  Converter Interfaces

   -  CMOS Interface

      -  32-bits (shared with the P lines of the LVDS bus)
      -  Up to 250Mbps (SDR)

   -  LVDS Interface

      -  32-bits (P lines shared with CMOS interface)
      -  Up to 1.25Gbps (625MHz DDR)

-  Memory

   -  Dual DDR2 DIMM
   -  Maximum pattern length of 134M samples (*limited to 30M samples in most applications*)

-  PC Interface

   -  USB 2.0 "B" connector

-  Clocking

   -  On-connector clock input for all interfaces
   -  Optional external clock input via SMA jack for CMOS interfaces

-  Rated for operation only at 25ºC
-  Multi-Unit Synchronization

   -  Up to four DPG2's may have their LVDS interfaces synchronized together
   -  Requires additional Synchronization Board and cabling

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/dpg2_board_layout.png

Output Data
===========

The DPG2 has two 16-bit ports capable of interfacing with both LVDS and LVCMOS devices. When transmitting a data vector each sample from the data file is played sequentially on the output port. Note that while the two data ports are labeled "I" and "Q" in the pinout, the actual mapping of bits to DACs will depend on the particular evaluation board connected. Many DACs with interfaces of 16-bits or less will only use a single port (generally the "I" port).

For LVCMOS/LVTTL devices, 3.3V, 2.5V, and 1.8V levels are supported.

The vector length must be at least 256 points per channel, and the length must be divisible by 256 for proper operation.

Clocking
========

The DPG requires an input clock to set the frequency of the data output. This is labeled DCO, for Data Clock Out. In LVDS mode, this clock is supplied through the main connector, and no other cables are required. In CMOS mode, the clock can either come through the main connector, or can be supplied via the SMA jacks J12 and J13. Which method is available will depend on the design of the evaluation board. When selecting a configuration, the names ending in (DCO) will have the clock received through the main connector. Configuration names ending in (SMA) will expect a clock to be cabled into J12 or J13.

The DPG also provides an output clock, *DCI*, which is synchronous with the data leaving the DPG2.

Hexadecimal Display
===================

Each DPG2 is equipped with a small red display. When a DPG2 is powered up, but not yet connected to software, the display will read 0. Once software has initiated communication with the DPG2, the display will indicate the index of the DPG2. This is used when multiple DPG2s are connected to the same PC.

The left "decimal point" on the display indicates if the DPG2 has been "configured". If the left point is not lit, the DPG2 will need to be configured before any other operations.

The right decimal point indicates the status of the vector. The point will not be lit if a vector has not been downloaded into the DPG2. The point will stay lit when a vector is downloaded but not playing, and the point will blink when the vector is being played to the DUT.

SMA Jacks
=========

There are two SMA jacks location on the DPG2 (J12 and J13). These are an optional input clock path for use with older CMOS interface DAC evaluation boards.

Multi-Unit Synchronization
==========================

Up to four DPG2's can be synchronized together so that the LVDS data coming out of all the DPGs is aligned to a common clock. Synchronization is not supported with the CMOS interface.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/dpg2_multisync.png
   :align: center

A clock distribution module (Part Number HSC-DAC-DPG-CLKDIS) is required, as well as one Samtec HQCD-030-15.00-TED-TEU-1 cable per DPG2, for synchronizing. When ordering the distribution module, please indicate how many cables are needed. A schematic of the clock distribution board is available `here <https://wiki.analog.com/_media/resources/eval/dpg/dpg2_multisync_schematic.pdf>`__.

The synchronization system works by having the Master unit forward the clock it receives (from the evaluation board attached to the Master) on to the Clock Distribution Module. The module then sends this clock back out to each unit, including the Master. The trace lengths and cables are all very well matched, and ensure that the clocks arrive at each slave DPG2 at the same time. The DPG2s then use this clock, instead of the clock from their respective evaluation board, to clock the data.

This requires that all the evaluation boards be clocked with exactly the same clock, as any frequency drifts between the evaluation boards will not be seen in the data, leading to data overrun or underrun.

Setting up Multi-Unit Synchronization
-------------------------------------

1. Connect the sync cables between the DPGs (up near the main data connector) and the sync board. Power the sync board with +5V. Make sure one of the DPG2’s is connected to the “Master” connector on the sync board, the other units can be connected to any of the other outputs on the sync board.

2. Connect a DAC board up to each DPG2 as you normally would, except only connect one of the DAC eval board to USB. Power up the eval boards.

3. Configure the DAC eval board as you would like with the SPI program. Then disconnect the USB, and connect it to the next eval board, configure it, and so on until all eval boards are setup.

4. With all the DPG2s powered on and connected to USB, open DPGDownloader. It should see all the DGP2s, and have a separate “panel” for each. On the left side of each panel, there is an option that defaults to “Single”. On the Master DPG2, change this to Master, and on the others change it to Slave.

5. Import or create the vectors you want the DACs to play out, and assign them to each DAC. You can correlate each DAC in the software with the number displayed in red on the DPG2 itself.

6. Download the vectors to all the DPG2s. Hit play on all the units except the Master. This arms the slaves to be ready to transmit.

7. Hit Play on the Master unit. This starts playback on all the units.

Connector Pinouts
=================

.. image:: https://wiki.analog.com/_media/section>resources/eval/dpg/z-pack_pinout&nofooter
   :alt: z-pack_pinout&nofooter

Support
=======

Please contact `DPG Support <https://wiki.analog.com/mailto/dpg.support@analog.com>`__ with any additional questions regarding the DPG or DAC Software Suite.
