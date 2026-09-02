.. _adrv9361z7035 introduction:

Introduction
============

Overview
--------

The ADRV9361-Z7035 represents a Software Defined Radio (SDR) that combines the
Analog Devices :adi:`AD9361` integrated RF Agile Transceiver™ with the Xilinx
Z7035 Zynq®-7000 in module form suitable for product integration.

Key Features
------------

Low-Power Design
~~~~~~~~~~~~~~~~

Uses the Zynq SoC's -2LI version with DDR3L memory and efficient voltage
regulators enabling power scaling based on performance needs.

High Bandwidth Connectivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The module offers dual Gigabit Ethernet, USB2.0, four 6.6 Gb/s serial links
(PCIe x4, SFP+, others), and high-speed LVDS I/O for custom interfaces.

Wideband RF Capability
~~~~~~~~~~~~~~~~~~~~~~~

Provides a highly integrated radio that enables wideband 2x2 MIMO receive and
transmit paths from 70 MHz to 6.0 GHz with tunable channel bandwidth <200kHz to
56MHz.

Programmable SoC
~~~~~~~~~~~~~~~~

Features a Dual ARM® Cortex™-A9 MPCore™ running at 800MHz, with built in
peripherals like USB, Gigabit Ethernet, and memory interfaces.

Compact Form Factor
~~~~~~~~~~~~~~~~~~~~

The module measures 100mm x 62mm, compliant with DP10062 "Sick of Beige v1.0"
enclosure standards.

Production-Ready
~~~~~~~~~~~~~~~~~

Rated for industrial temperatures (-40°C to +85°C) and tested against MIL-STD
202G methods for thermal, vibration, and shock specifications.

Operating System Support
~~~~~~~~~~~~~~~~~~~~~~~~~

Comes with Analog Devices Linux reference design for Zynq, bootable from an SD
card. Also supports Linux, Android, FreeRTOS, eCos, VxWorks, and others.

Development Tools
~~~~~~~~~~~~~~~~~

Supports MATLAB® and Simulink® alongside Analog Devices Linux applications for
prototyping.

Open-Source Code
~~~~~~~~~~~~~~~~

Analog Devices provides precompiled reference designs on the
:ref:`ADRV9361 page <adrv9361z7035>` and
a source code support package hosted on Github.

Module Specifications
---------------------

+----------------------------+-------------------------------------+
| Category                   | Specification                       |
+============================+=====================================+
| **RF Band**                | 70MHz to 6.0GHz                     |
+----------------------------+-------------------------------------+
| **Tunable Channel BW**     | <200kHz to 56MHz                    |
+----------------------------+-------------------------------------+
| **Max Output Power**       | 6.5-8.0 dBm (typical)               |
+----------------------------+-------------------------------------+
| **Max RX Input Power**     | 2.5 dBm (peak)                      |
+----------------------------+-------------------------------------+
| **Processor**              | Dual ARM Cortex-A9 @ 800MHz         |
+----------------------------+-------------------------------------+
| **Logic Cells**            | 275K Kintex-7 with 900 DSP48 slices |
+----------------------------+-------------------------------------+
| **Memory (DDR3L)**         | 1GB @ 1,066 Mb/s                    |
+----------------------------+-------------------------------------+
| **Flash**                  | 256 Mb QSPI @ 400Mb/s               |
+----------------------------+-------------------------------------+
| **Power Consumption**      | <5 Watts (typical)                  |
+----------------------------+-------------------------------------+
| **Supply Voltage**         | 4.5V-5.5V (5.0V nominal)            |
+----------------------------+-------------------------------------+
| **Dimensions**             | 100mm x 62mm                        |
+----------------------------+-------------------------------------+
| **Operating Temp**         | -40°C to +85°C                      |
+----------------------------+-------------------------------------+

Important Compatibility Note
-----------------------------

.. important::

   ADRV9361-Z7035 is not pin compatible with standard PicoZed (non-SDR) carrier
   cards due to new pinout requirements for the Z-7035 and AD9361 digital I/O.

.. figure:: images/simplified_system_diagram.png
   :alt: ADRV9361-Z7035 simplified diagram
   :align: center
   :width: 500

   Simplified System Diagram

.. figure:: images/adrv9361-z7035_device_callout.png
   :alt: ADRV9361-Z7035 device callout
   :align: center
   :width: 500

   ADRV9361-Z7035 SOM Device Callout
