AD-SWIOT1L-SL
=============

Software-configurable Analog and Digital I/O with 10BASE-T1L Evaluation and Development Platform
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Introduction
------------

.. figure:: ad-swiot1l-sl_angle-web.jpg
   :align: right
   :width: 400 px

   AD-SWIOT1L-SL Development Platform

The :adi:`AD-SWIOT1L-SL` is a complete hardware and software platform for prototyping intelligent,
secure, network-capable field devices, with applications in factory automation,
process control, and intelligent buildings. Some of the main features and
benefits include:

- Ultimate flexibility in I/O interface configurability through software
- Embedded processing for implementing self-capable edge devices
- Built-in security for root-of-trust, mutual authentication, data confidentiality and integrity, secure boot, and secure communications
- Long-range single-pair 10BASE-T1L Ethernet interface
- Power delivery via the 10BASE-T1L interface or from a field supply enabling both low and high power applications
- Fully isolated design for safe operation
- Industry standard form factor compatible with DIN rail mounts

.. figure:: swiot1l_block_diagram.png
   :width: 800 px

   AD-SWIOT1L-SL Simplifed Block Diagram


Specifications
--------------

.. csv-table::
   :file: specifications.csv

Package Contents
----------------

The development kit is delivered with a set of accessories required to put the
system together and get it up and running in no time.

This is what you’ll find in the development kit box:

- 1 x :adi:`AD-SWIOT1L-SL` board with enclosure
- 1 x :adi:`AD-T1LUSB-EBZ` 10BASE-T1L to USB adapter board
- 1 x PROFIBUS (1x2x18AWG) cable for Single Pair Ethernet (SPE) connectivity
- 1 x USB 2.0 cable
- 1 x cable connector for the external 24 V power supply
- 1 x cable connector for channels connectivity

The AD-SWIOT1L-SL comes with pre-programmed firmware enabling the system to
interface with a PC application for system configuration, control, and data
acquisition over the 10BASE-T1L interface.

Application Development
-----------------------

.. figure:: sw_block_diagram.png
   :width: 300 px
   :align: right

The AD-SWIOT1L-SL firmware is based on ADI’s open-source no-OS framework. It
includes the bare-metal device drivers for all the components in the system as
well as example applications enabling connectivity via the 10BASE-T1L interface
for system configuration and data transfer.

.. admonition:: Download

   :git-no-OS:`AD-SWIOT1L-SL Firmware Source Code and User Guide <projects/swiot1l>`

User Guides
-----------

.. toctree::
   :titlesonly:
   :glob:

   */index

Help and Support
----------------

For questions and more information, please visit the :ez:`/`.
