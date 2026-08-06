.. _eval-adin1320fmcz:

EVAL-ADIN1320FMCZ
=================

ADIN1320 PHY Evaluation Board.

.. figure:: eval-adin1320fmcz.jpeg
   :align: right
   :width: 300

The :adi:`EVAL-ADIN1320FMCZ` evaluation board enables quick and easy evaluation
of Analog Devices' :adi:`ADIN1320`, a low power, single port, multi-speed
industrial Ethernet transceiver supporting RMII/MII to Copper or Fiber
operation.

The ADIN1320 combines an Energy Efficient Ethernet PHY core with all associated
analog circuitry, clock buffering, management interface, and MAC interface
control logic. The PHY supports MII, RGMII (including internal delay variants),
and RMII host interfaces, and can operate over either a standard copper (RJ45)
or fiber (SFP) medium.

Overview
--------

The following carriers are supported, followed by the target firmware:

.. list-table::

   * - Carrier
     - Linux
   * - Zedboard (Zynq-7000)
     - ✓

Features
~~~~~~~~

* Single port 10/100/1000 Mb industrial Ethernet transceiver
* MII, RMII, RGMII (with optional internal RX/TX delay) host interfaces
* Selectable copper (RJ45) or fiber (1000BASE-X, 1000BASE-KX, 100BASE-FX) media
* PHY address and operating mode (line and MAC interface selection) configured via on-board hardware strapping

Evaluation board kit contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ADIN1320EBZ-U1 evaluation board
* LPC FMC to GPIO converter

Equipment needed
~~~~~~~~~~~~~~~~~

* Zedboard - Zynq-7000 development board
* Cat5+ Ethernet cable or a 1000BASE-X capable SFP module
* SD card

User Guides
-----------

.. toctree::
   :titlesonly:
   :glob:

   user-guide/*

Developers
-----------

Drivers
~~~~~~~

.. list-table::

   * - Firmware
     - Source code
     - Documentation
   * - Linux
     - :git-linux:`drivers/net/phy/adin.c`
     - :git-linux:`Documentation/devicetree/bindings/net/adi,adin.yaml`

.. note::

   The ADIN1320 is supported by the mainline ``adin`` PHY driver, shared with
   the ADIN1200/ADIN1300 family. No ADIN1320-specific driver changes are
   required.

Help and Support
-----------------

For questions and more information, please visit:

* :ez:`EngineerZone Support Community <reference-designs>`
* :adi:`ADIN1320 Product Page <ADIN1320>`

.. esd-warning::
