AD-FMCOMMS1-EBZ Introduction
============================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



The :adi:`AD-FMCOMMS1-EBZ <en/evaluation/eval-fmcomms/eb.html>` high-speed analog module is designed to showcase the latest generation high-speed data converters. The :adi:`AD-FMCOMMS1-EBZ <en/evaluation/eval-fmcomms/eb.html>` provides the analog front-end for a wide range of compute-intensive FPGA-based radio applications.

The :adi:`AD-FMCOMMS1-EBZ <en/evaluation/eval-fmcomms/eb.html>` is an analog front end hardware platform that addresses a broad range of research, academic, industrial and defense applications. The :adi:`AD-FMCOMMS1-EBZ <en/evaluation/eval-fmcomms/eb.html>` enables RF applications from 400MHz to 4 GHz. The module is customizable to a wide range of frequencies by software without any hardware changes, providing options for GPS or IEEE 1588 Synchronization, and MIMO configurations.

When combined with the Xilinx ZYNQ® Software-Defined Radio Kit, :adi:`AD-FMCOMMS1-EBZ <en/evaluation/eval-fmcomms/eb.html>` enables a variety of wireless communications functions at the physical layer, from baseband to RF. With up to 4 GB of flash storage space, 512 MB of RAM, Gigabit Ethernet interface (depending on the base platform) and a Linux image built specifically for the :adi:`AD-FMCOMMS1-EBZ <en/evaluation/eval-fmcomms/eb.html>`, you can get everything you need for a easy out of the box experience. The platform offers enough flexibility for many applications, and supports streaming data, and standard web interfaces to analyze transmited RF data.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/dscn1188.png
   :alt: FMComms + Zynq Board
   :align: center
   :width: 400px

.. warning::

   The AD-FMCOMMS1-EBZ FMC Card is not fully ANSI/VITA 57.1 compatible:

   
   -  does not meet the mechanical form factor (too tall, too long),
   
   It was designed, and meets the needs of prototyping platforms, and will work with FPGA Development systems which include an FMC connector. It may not mechanically fit on other ANSI/VITA 57.1 carrier cards.


Applications
------------

-  Wireless communications demonstration and learning tool
-  Remote radio head
-  Software-defined radio
-  Satellite modems
-  Test and measurement equipment
-  Radar and advanced imaging
-  General purpose data acquisition

Specifications & Features
-------------------------

-  General purpose design suitable for any application
-  Software tunable across wide frequency range (400MHz to 4GHz) with 125MHz channel bandwidth (250MSPS ADC, 1GSPS DAC)
-  RF section bypass for baseband sampling
-  Phase and frequency synchronization on both transmit and receive paths
-  Allows high channel density
-  LPC FMC Compatible, meets VITA specifications except card length
-  Powered from single FMC connector
-  Supports MIMO radio, with less than 1 sample sync on both ADC and DAC
-  Includes schematics, layout, BOM, HDL, Linux drivers and application software
-  Supports add on cards for spectrum specific designs (PA, LNA etc)
-  Common I\ :sup:`2`\ C access for all device registers
