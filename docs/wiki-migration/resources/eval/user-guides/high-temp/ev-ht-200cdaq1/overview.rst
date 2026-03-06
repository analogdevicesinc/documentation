.

EV-HT-200CDAQ1 Overview
=======================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/high-temp/ev-ht-200cdaq1dtop.jpg
   :align: center

The EV-HT-200CDAQ1 is a complete system reference platform enabling precision data acquisition and control in extreme temperatures up to 200°C. Based upon the AD7981 analog-to-digital SAR converter, this reference design demonstrates a full featured system with two high speed simultaneously sampled channels along with 8 additional multiplexed channels suitable for covering the acquisition requirements for many high temperature, harsh environment application such as downhole oil and gas instrumentation. The data acquisition front end is connected to the VORAGO Technologies VA10800 ARM® Cortex®-M0 based microcontroller via multiple SPI ports. Once acquired, the data can be processed locally or transmitted via a UART or optional RS485 communications interface. In addition to the hardware, open source firmware uses FreeRTOS with optimized drivers and a data acquisition protocol with multiple modes of operation. Open source host software allows the users to connect to the board via UART to control acquisition modes, view data, log data and perform signal analysis. This platform is suitable as reference design, for rapid prototyping and lab testing of high temperature instrumentation systems.

--------------

Hardware Features
-----------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/high-temp/ev-ht-200cdaq1/block_diagram.jpg
   :align: center

All Components and PCB Rated and Tested for 200°C Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  PCB aspect ratio suitable for downhole tools and instrumentation - 1.0" x 11.5"
-  Rugged Micro D 15-S and Micro D 21-S connectors

Optimized Analog Devices Data Acquisition Front End
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  2 AD7981 ADC channels capable of 400ksps simultaneous sampling
-  1 AD7981 multiplexed channel (8 inputs) capable of 16ksps min sampling
-  0-2.5V analog input range

VORAGO VA10800 32-bit ARM® Cortex®-M0 MCU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  50MHz clock rate
-  32KB on-chip data SRAM
-  128kB on-chip program memory SRAM
-  TTL UART communications, optional RS485
-  HT Boot flash, system clock and core power supply
-  Optmized hardware interface to Analog Devices data acquisition front end

Flexible, Low Power Configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  +/-5VDC bipolar analog and 3.3VDC Digital power supplies for best analog performance
-  +3.3V single supply operating mode for simpler power configuration, with reduced analog performance
-  Low power operation: 155mW typical power consumption

Ease of Use Features for Prototype and Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Analog and Digital Breakout Boards included for extremely fast hookup on the bench
-  IDC header connector on board to facilitate easy probing of analog inputs
-  JTAG debug connector for MCU firmware programming

--------------

Software Features
-----------------

Open Source Firmware and Software Optimized for Data Acquisition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Firmware and Host software design driven by a common protocol definition, which enables flexible data acquisition optimized for resource constrained systems
-  Multiple modes of data acquisition supported

   -  Burst mode for frequency domain analysis or high throughput data capture
   -  Continuous mode for time domain analysis or lower throughput data capture

==== FreeRTOS Firmware Integration ====

-  Optimized drivers and data acquisition controls functions partitioned into tasks allows end user to focus on application coding right away

PC Host Data Viewer
~~~~~~~~~~~~~~~~~~~

-  Supports control of the board operation and real-time viewing of all channels of data acquisition
-  Robust frequency domain signal analysis tools
-  Ability to log data to CSV format

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/high-temp/ev-ht-200cdaq1/dataviewer.jpg
   :align: center

--------------

Design Package Details
----------------------

Hardware Design Package
~~~~~~~~~~~~~~~~~~~~~~~

-  Schematics
-  Assembly Drawing
-  Fabrication Drawing
-  Gerbers
-  Bill of Materials

Software Binaries
~~~~~~~~~~~~~~~~~

-  Host Data Viewer Executable

Software Source
~~~~~~~~~~~~~~~

-  Firmware and Data Viewer source codes available on ADI GitHub

See the :doc:`software and design package download </wiki-migration/resources/eval/user-guides/high-temp/ev-ht-200cdaq1/software>` page for more information.
