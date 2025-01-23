
AD-APARD32690-SL 
================

Introduction
------------

The :adi:`AD-APARD32690-SL <AD-APARD32690-SL>` is an Arduino Form-factor
Development Platform based on :adi:`MAX32690 <MAX32690>` ARM Cortex-M4
Microcontroller, targeted for prototyping intelligent, secure, and connected
industrial field devices. Some of the main features and benefits include:

- Arduino Mega-compatible form factor
- Two Pmod™-compatible connectors
- ARM Cortex-M4 Ultra Efficient Microcontroller with integrated Bluetooth 5.2 LE
- WiFi connectivity
- Long-range, single-pair 10BASE-T1L Ethernet interface
- Built-in security for root-of-trust, mutual authentication, data confidentiality and integrity, secure boot, and secure communications
- Open-source software stack

 .. image:: eval-max32690-ardz_angle.jpg
    :width: 450 px
    :align: left

 .. image:: ad-apard32690-sl-fbl.png
   :width: 450 px
   :align: right


.. csv-table:: Specifications
    :file: specifications.csv

**Hardware design files:**

- :download:`Schematics <02-073637-01-c.pdf>`
- :download:`Layout <08_073637c.zip>`
- :download:`Bill of Materials <05-073637-01-c.zip>`

System Setup & Evaluation
-------------------------

The development kit is delivered with a set of accessories required to put the
system together and get it up and running in no time.

This is what you’ll find in the development kit box:

- 1 x AD-APARD32690-SL board
- 1 x :dokuwiki:`AD-T1LUSB2.0-EBZ <resources/eval/user-guides/ad-t1lusb-ebz>` 10BASE-T1L to USB adapter board
- 1 x PROFIBUS (1x2x18AWG) cable for Single Pair Ethernet (SPE) connectivity
- 1 x USB 2.0 cable

:dokuwiki:`Getting the system up and running <resources/eval/user-guides/ad-apard32690-sl/software>`



Application Development
-----------------------

.. image:: sw_block_diagram.png
    :width: 400 px

The :adi:`AD-APARD32690-SL <AD-APARD32690-SL>` firmware is based on ADI’s
open-source no-OS framework. It includes the bare-metal device drivers for all
the components in the system as well as example applications enabling
connectivity via the 10BASE-T1L interface for system configuration and data
transfer.

`AD-APARD32690-SL Firmware Source Code and User Guide <https://github.com/analogdevicesinc/no-OS/tree/main/projects/apard32690>`__

User Guides
-----------

.. toctree::
   :titlesonly:
   :glob:

   */index

Help and Support
----------------

For questions and more information, please visit the :ez:`/`.
