.. _ad-pqmon-sl:

AD-PQMON-SL
============

Power Quality Analyzer
""""""""""""""""""""""

.. figure:: ade9430_angle.jpg
   :width: 400px
   :align: left

   AD-PQMON-SL Board

Overview
--------

Power quality monitoring is becoming important to keep power grids clean
despite the harmonics introduced by inverter-based resources. Such activity
improves the stability and reliability of the grid and improves equipment
health by preventing flickering or blackouts.

The :adi:`AD-PQMON-SL` is a power quality monitoring solution based on the
:adi:`ADE9430`, which is a high performance, polyphase energy and
Class S power quality monitoring and energy metering device.

This reference design also has an on-board processor, the
:adi:`MAX32650` an ultralow power Arm Cortex-M4 with FPU-Based
microcontroller (MCU) with 3MB flash and 1MB SRAM.

.. figure:: ad-pqmon-sl_block_diagram.png
   :width: 800px

   AD-PQMON-SL Block Diagram

Features
--------

- Allows prototyping of high performance, polyphase energy meters
- Modular hardware design:
  - Metering & compute base board
  - Add-on board for COMMS and HMI
- The base board offers flexibility in input/output (I/O) interfacing through
  custom add-on boards
- Industrial connectivity: 10BASE-T1L (ADIN1110), RS-485 (ADM2587E), Ethernet
  (WIZ82)
- Long time data logging (SD card)
- Standalone interface (display, LEDs, buttons)
- I/O prototyping area (external control signals, GPS / GNSS)
- Publicly available software for evaluation and prototyping
- no-OS open-source embedded software stack
- Embedded processing implementing the complete IEC 61000-4-30 class S power
  quality standard (using ADI proprietary ADSW-PQ-CLS library)
- Open-source GUI (Scopy – Cross-platform Qt application)
- Fully isolated design for safe operation
- Industry standard form factor compatible with DIN rail mounts

Applications
------------

- Energy and power monitoring
- Standards compliant power quality monitoring
- Protective devices
- Smart power distribution units
- Polyphase energy meters
- Intelligent buildings

.. tip::

   For more information about the hardware see the
   :ref:`ad-pqmon-sl hardware-guide`.

System Setup & Evaluation
-------------------------

The solution is delivered with a set of accessories required to put the system
together and get it up and running.

This is what you’ll find in the development kit box:

- 1x :adi:`AD-PQMON-SL` board with enclosure
- 1x `AD-T1LUSB2.0-EBZ <ad-t1lusb20-ebz>` 10BASE-T1L to USB adapter board
- 1x PROFIBUS (1x2x18AWG) cable for Single Pair Ethernet (SPE) connectivity

The :adi:`AD-PQMON-SL` comes with pre-programmed firmware
enabling the system to interface with a PC application for system configuration,
control, and data acquisition.

Application Development
-----------------------

The :adi:`AD-PQMON-SL` firmware is based on ADI’s open-source
no-OS framework. It includes the baremetal device drivers for all the
components in the system as well as an example application enabling evaluation
of the power quality features. <WRAP center round download 100%>

- :git-no-OS:`Github resources <projects/eval-pqmon>`

It is recommended to update the firmware to the latest version as indicated
:ref:`here <ad-pqmon-sl software-guide firmware-update>`.

- `latest hex file <https://swdownloads.analog.com/cse/scopy/ad-pqmon-sl/eval-pqmon.hex>`__
- `Scopy 2 download link <https://swdownloads.analog.com/cse/scopy/ad-pqmon-sl/scopy-windows-x86_64-setup-7797088.zip>`__

User Guides
-----------

.. toctree::
   :titlesonly:
   :glob:

   */index

Helpful Documents
-----------------

- :adi:`ADE9430 Data Sheet <ade9430>`
- :dokuwiki:`ADE9430 Technical Reference Manual </resources/eval/user-guides/ade9430>`
- :adi:`ADSW-PQ-CLS Power Quality Library - Software Request <srf>`
- :external+scopy:doc:`Scopy plugin for PQMON <plugins/pqm/index>`

Additional Resources
---------------------

- :adi:`ADE9430 Product Page <ADE9430>`
- :adi:`MAX32650 Product Page <MAX32650>`
- :adi:`ADuM6424 Product Page <ADUM6424>`
- :adi:`ADuM4152 Product Page <ADUM4152>`
- :adi:`MAX31343 Product Page <MAX31343>`
- :adi:`MAX40203 Product Page <MAX40203>`
- :adi:`LTC3306 Product Page <LTC3306>`
- :adi:`ADM2587 Product Page <ADM2587>`
- :adi:`ADP225 Product Page <ADP225>`
- :adi:`ADIN1110 Product Page <ADIN1110>`

Design and Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

    :download:`AD-PQMON-SL Design Support Package <ad-pqmon-sl-designsupport.zip>`

    - Schematic
    - PCB Layout
    - Bill of Materials
    - Allegro Project

Support
-------

Analog Devices will provide **limited** online support for anyone using the
reference design with Analog Devices components via the
:ez:`EngineerZone reference designs <reference-designs>` forum.

It should be noted that the older the tools’ versions and release branches are,
the lower the chances to receive support from ADI engineers.
