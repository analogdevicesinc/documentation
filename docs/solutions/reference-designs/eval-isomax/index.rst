EVAL-ISOMAX
===========

Low-cost Integrated BMS Monitor with On-board MCU and Dual isoSPI
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Overview
--------

.. figure:: eval-isomax_angle.jpg
   :align: right

   EVAL-ISOMAX Dual isoSPI Adapter

The :adi:`EVAL-ISOMAX` is an integrated dual isoSPI adapter and
microcontroller board featuring the :adi:`MAX32670`
high-reliability, ultra-low-power microcontroller and the
:adi:`ADBMS6822` dual isoSPI transceiver. This board allows
multiple ADBMS68xx battery monitors to be connected through daisy chain
configuration. The EVAL-ISOMAX also features reversible isoSPI, which enables a
redundant path to the peripheral units. The PCB components and DuraClik
connectors are optimized for low electromagnetic interference (EMI)
susceptibility and emissions.

Features
--------

* Low-cost integrated monitoring for BMS with on-board MCU and dual isoSPI chip
* Demonstrates SPI to isoSPI 2-wire datalinks
* Includes two isoSPi ports for reversible isoSPI support
* Configurable powering options for LPCM support isoSPI connections through
  simple DuraClik connectors
* Stackable and allows daisy chain of up to eight (8) ADBMS6830BMSW boards
* With PC-based software for control and data analysis using Broad Market
  Browser BMS GUI

Applications
----------------

* IOT Battery Management
* Industrial Machine Vision
* Power Tools
* Mobile Robotics Battery Management
* Industrial Equipment Battery Monitoring
* Adaptive Battery Type System Monitoring
* Portable Energy Storage Systems
* Electric 2-Wheelers (E2Ws) such as E-scooter, E-bikes
* Light Electric Vehicles (LEV)

What's Inside the Box?
----------------------

.. figure:: eval-isomax_package_contents.png
   :width: 400 px

   EVAL-ISOMAX Package Contents

System Architecture
-------------------

.. figure:: eval-isomax_block_diagram.png
   :width: 600 px

   EVAL-ISOMAX Simplified Block Diagram

Components and Connections
--------------------------

.. figure:: primary_side.png
   :width: 600 px

   EVAL-ISOMAX Hardware Components

Use Cases
---------

The EVAL-ISOMAX has an on-board ultralow-power Arm-Cortex M4-based MCU that is
suitable for broad market applications such as for IoT and industrial battery
management systems. The EVAL-ISOMAX board is recommended to be used with other
ADI broad market BMS boards such as the :adi:`EVAL-ADBMS6830BMSW` battery stack
monitor and the :adi:`EVAL-ADBMS2950-BASIC` pack monitor.

Users may also opt to use other microcontrollers for other applications
requiring more stringent timing, higher memory, or faster computing speed.
Other possible microcontrollers to be paired are the :adi:`SDP-K1` and :adi:`AD-APARD32690-SL` .

Option 1: Using the EVAL-ISOMAX as Standalone MCU with other ADI Broad Market BMS Boards
----------------------------------------------------------------------------------------

Sample Battery Monitoring Setup with the EVAL-ADBMS6830BMSW

.. figure:: using_isomax_with_other_adi_bm_boards.png
   :width: 600 px

   EVAL-ISOMAX with Other ADI Broadmarket BMS Boards

Option 2: Using the EVAL-ISOMAX as a Secondary Device to other MCU Boards
-------------------------------------------------------------------------

See below configuration using different MCUs:

Sample Cell Monitoring Setup using the AD-APARD32690-SL as Main Microcontroller Board and EVAL-ISOMAX as isoSPI Adapter

.. figure:: eval-isomax_with_ad-apard32690-sl.png
   :width: 600 px

   EVAL-ISOMAX as a Secondary Device to AD-APARD32690-SL Microcontroller Board

Sample Pack Monitoring Setup using the SDP-K1 as Main Microcontroller Board and EVAL-ISOMAX as isoSPI Adapter

.. figure:: adbms2950_with_isomax_and_sdp-k1.png
   :width: 600 px

   EVAL-ISOMAX as a Secondary Device to SDP-K1 Controller Board

Design and Integration Files
----------------------------

.. admonition:: Download

 :download:`EVAL-ISOMAX Design Support Package <EVAL-ISOMAX-design_support.zip>`

 * Schematic
 * PCB Layout
 * Bill of Materials
 * Allegro Project

User Guides
-----------

.. toctree::
   :titlesonly:
   :glob:

   */index

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`/`.
