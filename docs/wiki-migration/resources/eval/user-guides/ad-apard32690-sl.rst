AD-APARD32690-SL User Guide
===========================

|

.. important::

   **Notice:** This page has been fully migrated to GitHub.io and is no longer maintained on the Wiki. Please refer to the GitHub link below for the most current and accurate information.

   | https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-apard32690-sl/index.html
   | If you would like to contribute updates to this document, please submit your suggestions via a Pull Request on the GitHub page.
   | Thank you for your understanding, and we apologize for any inconvenience this transition may cause.
   


Introduction
------------

| The :adi:`AD-APARD32690-SL` is an Arduino Form-factor Development Platform based on :adi:`MAX32690` ARM Cortex-M4 Microcontroller, targeted for prototyping intelligent, secure, and connected industrial field devices. Some of the main features and benefits include:
| \* Arduino Mega-compatible form factor

-  Two Pmod™-compatible connectors
-  ARM Cortex-M4 Ultra Efficient Microcontroller with integrated Bluetooth 5.2 LE
-  WiFi connectivity
-  Long-range, single-pair 10BASE-T1L Ethernet interface
-  Built-in security for root-of-trust, mutual authentication, data confidentiality and integrity, secure boot, and secure communications
-  Open-source software stack

|image1| |image2|

--------------

Specifications
--------------

+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Computing Resources |                                                                                                                                                |
+=====================+================================================================================================================================================+
| CPU                 | :adi:`MAX32690` Ultralow Power ARM Cortex-M4 with FPU-Based Microcontroller (MCU) with 3 MB Flash and 1 MB SRAM                                |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Memory              | 1 Gb RAM                                                                                                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Storage             | 64 Mb QSPI Flash                                                                                                                               |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Security            | :adi:`MAXQ1065` Ultralow Power Cryptographic Controller with ChipDNA\ :sup:`TM`                                                                |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Connectivity        |                                                                                                                                                |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Ethernet            | :adi:`ADIN1110` Robust, Industrial, Low Power 10BASE-T1L Ethernet MAC-PHY                                                                      |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| WiFi                | NINA-W102 - IEEE 802.11b, IEEE 802.11g, IEEE 802.11n                                                                                           |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Bluetooth           | Bluetooth 5.2 LE Radio                                                                                                                         |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| USB                 | USB 2.0                                                                                                                                        |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Power supply        |                                                                                                                                                |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| External power      | 5V DC to 28V DC                                                                                                                                |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| USB-C               | 5 V at 3 A, without power negotiation                                                                                                          |
+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   **Hardware design files:**

   
   -  `Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/02-073637-01-c.pdf>`_
   -  `Layout <https://wiki.analog.com/_media/resources/eval/user-guides/08_073637c.zip>`_
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/05-073637-01-c.zip>`_
   


--------------

System Setup & Evaluation
-------------------------

The development kit is delivered with a set of accessories required to put the system together and get it up and running in no time.

This is what you'll find in the development kit box:

-  1 x AD-APARD32690-SL board
-  1 x :doc:`AD-T1LUSB2.0-EBZ </wiki-migration/resources/eval/user-guides/ad-t1lusb-ebz>` 10BASE-T1L to USB adapter board
-  1 x PROFIBUS (1x2x18AWG) cable for Single Pair Ethernet (SPE) connectivity
-  1 x USB 2.0 cable

.. note::

   :doc:`Getting the system up and running </wiki-migration/resources/eval/user-guides/ad-apard32690-sl/software>`


--------------

Application Development
-----------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/sw_block_diagram.png
   :align: right
   :width: 250px

The :adi:`AD-APARD32690-SL` firmware is based on ADI's open-source no-OS framework. It includes the bare-metal device drivers for all the components in the system as well as example applications enabling connectivity via the 10BASE-T1L interface for system configuration and data transfer.

.. admonition:: Download
   :class: download

   :git-no-OS:`AD-APARD32690-SL Firmware source code and user guide <projects/apard32690>`


--------------

Help and Support
----------------

For questions and more information please contact us on the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-max32690-ardz_angle.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-apard32690-sl-fbl.png
   :width: 400px
