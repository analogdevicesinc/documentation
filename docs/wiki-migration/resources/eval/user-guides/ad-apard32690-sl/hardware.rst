AD-APARD32690-SL Hardware User Guide
====================================

Introduction
------------

The **AD-APARD32690-SL** is an Arduino and Pmod-compatible form factor development board based on the :adi:`MAX32690`, an ultralow power microcontroller system for processing, control, and connectivity. This platform includes Bluetooth LE, WiFi, and 10BASE-T1L single-pair Ethernet connectivity, and is intended for the following purposes:

-  Application development for the scalable sensing platform
-  As an upgrade path from the internally popular EVAL-ADICUP3029 development board
-  As a lesser degree, parallel path to the SDP-K1 and Linduino boards

The microcontroller system is based on an ARM® Cortex®-M4 processor, a collection of digital peripherals, embedded SRAM and flash memory, and an analog subsystem that provides clocking, reset, and power management capability in addition to an ADC subsystem. The platform has an Arduino Uno-compatible form factor and has two additional Pmod™-compatible connectors, and 2-wire JTAG connector for easier debugging. It is accompanied by an Eclipse-based development environment, which can be downloaded free of charge.

| The AD-APARD32690-SL supports several initial hardware and software example projects demonstrating connected systems, solutions for industrial sensing, control, and Internet of Things (IoT) applications.
| |image1|
| ----

Features
--------

-  Allows prototyping of intelligent, secure, and connected industrial field devices
-  Arduino Mega-compatible form factor
-  Two Pmod™-compatible connectors
-  ARM Cortex-M4 Ultra Efficient Microcontroller with integrated Bluetooth 5.2 LE
-  WiFi connectivity
-  Long-range, single-pair 10BASE-T1L Ethernet interface
-  Built-in security for root-of-trust, mutual authentication, data confidentiality and integrity, secure boot, and secure communications
-  Open-source software stack

Applications
------------

-  Factory automation
-  Process control
-  Intelligent buildings
-  Secure field instruments
-  Internet of Things

--------------

Hardware Setup
--------------

Requirements
~~~~~~~~~~~~

Hardware
^^^^^^^^

-  Boards and PMODs used
-  Cables and their type
-  1x SD card (at least 16 GB); follow :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
-  Power supplies
-  Other add-ons, etc.

Software
^^^^^^^^

-  :git-no-OS:`AD-APARD32690-SL Source Code <projects/apard32690>`
-  Unordered List Item

| 
| ===== Hardware Configuration =====

Block Assignments
~~~~~~~~~~~~~~~~~

| 
| <fc #ff0000>< insert board photo with pins/connector labels></fc>

============== ====================
Connector Name Function/Description
============== ====================
P1             
P2             
P3             
P4             
J1             
J2             
============== ====================

Power Supply
~~~~~~~~~~~~

| 

Digital Interface
~~~~~~~~~~~~~~~~~

|

Status Indicators
~~~~~~~~~~~~~~~~~

| 

Setting up the Hardware
-----------------------

| \*\* Upload a picture of what your setup looks like. \*\*
| Step-by-step instructions on how to set up the hardware

-  Ordered list
-  Ordered list
-  Ordered list
-  Ordered list
-  Ordered list

| 
|

.. tip::

   For Software Setup instructions, please check out the :doc:`AD-APARD32690-SL Software User Guide </wiki-migration/resources/eval/user-guides/ad-apard32690-sl/software>`


--------------

Test Results and Analysis
-------------------------

| Put in here important graph/s, tables, or data analysis from hardware testing.

--------------

Additional Information and Useful Links
---------------------------------------

-  :adi:`MAX32690 Product Page <MAX32690>`
-  :adi:`ADIN1110 Product Page <ADIN1110>`
-  :adi:`MAXQ1065 Product Page <MAXQ1065>`
-  :adi:`LT8692S Product Page <LT8692S>`
-  :adi:`LTC4415 Product Page <LTC4415>`
-  :adi:`LTC6655 Product Page <LTC6655>`
-  :adi:`LT3040 Product Page <LT3040>`
-  Links to parts' product pages (ADI products only)
-  Links to application notes, other relevant pages, etc.

--------------

Reference Demo and Software Resources
-------------------------------------

-  :git-no-OS:`AD-APARD32690-SL project source code <projects/apard32690>`
-  Links to the wiki documentation of the IPs that are used in this project (if applicable)
-  Links to drivers and devicetree source code and wiki documentation (if applicable)
-  Links to reference demo (if applicable)

--------------

Design and Integration Files
----------------------------

.. admonition:: Download
   :class: download

   :adi:`AD-APARD32690-SL Design & Integration Files <AD-APARD32690-SL-designsupport.zip>`

   
   -  Schematics
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   


--------------

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/AD-APARD32690-SL>`__ to receive all these great benefits and more!


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-max32690-ardz_angle.jpg
   :width: 600px
