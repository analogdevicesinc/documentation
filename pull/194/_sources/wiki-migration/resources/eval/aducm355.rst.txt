ADuCM355 Reference Design User Guide.
=====================================

Introduction
============

The ADuCM355 reference design is a gas sensing platform which allows a user to build a flexible gas sensing measurement and evaluation system showcasing the ADuCM355. This as a reference design to showcase the ADuCM355 but is not aimed to be an off-the-shelf product.

The reference design provides a modular plug in approach enabling gas measurements from EC (Electrochemical) based sensors supplied by a 3rd party, along with support for the most common PM sensors on the market. It is compatible with most 4-series EC sensors on the market. The system allows for up to four EC sensors to be connected at one time. This is to mimic a typical gas sensing instrument, where CO, H2S, O2, LEL gases are monitored.It is also applicable for Outdoor Air Quality measurement, by using a different suite (CO, O3, SO2, NO2) of 4-series sensors. The measurements are sent to a PC GUI via USB cable, where they are displayed on a GUI.

Hardware
========

The hardware is broken into modules. The motherboard consists of 4 connectors to connect up to sensor daughterboards. It has the ADuCM3029 Cortex M3 acting as the host MCU. It's function is to communicate with the sensors, and send the collected data to a PC GUI.

.. image:: https://wiki.analog.com/_media/resources/eval/img_1515.jpg
   :align: center
   :width: 600px

There are two different daughterboard designs. Each plugs into the motherboard. Up to 4 daughter boards can be connected at once. The Gas Sensor daughterboard consists of an ADuCM355 and socket for almost any 2,3 or 4 lead 4-series sensors. The Water Sensor daughterboard consists of an ADuCM355 and BNC socket for off-the-shelf pH probes and sondes.

.. image:: https://wiki.analog.com/_media/resources/eval/img_2143.jpg
   :align: center
   :width: 600px

Software
========

The GUI is available to download from here. The latest version is Rev 0.1. Before starting, check out the tutorial on how the GUI works.


|image1|

.. image:: https://wiki.analog.com/_media/resources/eval/gui_capture2.jpg
   :width: 400px

Outdoor Air Quality Reference Design
====================================

The system supports the four main EPA gases

Expansion and further evaluation
================================

The kit consists of the motherboard and one sensor daughterboard. More daughterboards can be ordered separately.

An emulator board is available. It can be ordered separately. It allows the user to re-program both the ADuCM355 daughter board and the ADuCM3029 host MCU on the motherboard. This is recommended for deeper development activity, after initial evaluation of the basic reference design system.

.. image:: https://wiki.analog.com/_media/resources/eval/img_2139.jpg
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/img_2140.jpg
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/img_2141.jpg
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/img_2142.jpg
   :align: center
   :width: 400px

Related Material
----------------

Water Quality Reference Design
==============================

The system can also be used to evaluate the ADuCM355 for Water Quality Analysis applications. The same motherboard is used, but the daughterboard used is the water quality daughterboard. This is optimized for use with standard water quality probes such as pH probes, and includes a BNC connector for easy setup.

.. image:: https://wiki.analog.com/_media/resources/eval/img_2143.jpg
   :align: center
   :width: 600px

Schematics
----------

Download the schematics, layout and gerber files for each of the hardware pieces here: 4Gas Motherboard

ADuCM355 Daughterboard

Water Quality Daughterboard

Emulator board

Firmware
--------

The latest firmware revision is 0.1. It was released on XX/XX/20XX. Download it here.

GUI
---

The latest GUI revision is 0.1. It was released on XX/XX/20XX. Download it here.

Stay tuned for further updates.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/gui_capture1.jpg
   :width: 400px
