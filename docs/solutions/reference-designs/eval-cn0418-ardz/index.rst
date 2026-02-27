.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/hardware/cn0418

.. _eval-cn0418-ardz:

EVAL-CN0418-ARDZ
=================

PLC/DCS Quad-Channel Analog Output with HART.

Overview
--------

:adi:`CN0418` is an Arduino-compatible shield that provides a complete, fully
isolated and highly flexible, 4-channel analog output system suitable for
programmable logic controllers (PLCs) and distributed control system (DCS)
applications that require +/-5 V, +/-10 V voltage and 4 mA to 20 mA current
output with HART compatibility. All outputs are protected from transients and
are suitable for the most harsh industrial environments.

The HART compatibility of this module provides a complete field communications
solution that is simple to use, low cost, and extremely reliable.

The circuit is powered from a standard 24 V bus supply, with on-board filtering
and protection circuitry. This module can be powered from standard supplies
ranging from 12 VDC to 28 VDC.

The :adi:`EVAL-CN0418-ARDZ <CN0418>` includes the :adi:`AD5755-1` quad-channel
voltage and current output DAC with dynamic power control, and the
:adi:`AD5700-1` HART modem, providing a completely isolated multiplexed HART
analog output solution. The :adi:`ADuM3482` and :adi:`ADuM3151` provide digital
isolation, the :adi:`ADP2441` provides the dc-to-dc regulation, and the
:adi:`ADG704` provides HART channel multiplexing. The :adi:`LT8301` generates
the isolated supply.

.. figure:: images/cn0418_board.png
   :align: center
   :width: 500

   EVAL-CN0418-ARDZ Evaluation Board

.. figure:: images/cn0418_docked.jpg
   :align: center
   :width: 500

   EVAL-CN0418-ARDZ Attached to EVAL-ADICUP3029

Simplified Functional Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/cn0418_block_diagram.png
   :align: center
   :width: 600

   CN0418 Simplified Functional Block Diagram

.. toctree::

   hardware
   software

Documents
---------

- :adi:`CN0418 Circuit Note <CN0418>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0418-ARDZ Design & Integration Files
   <https://www.analog.com/cn0418-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information
----------------------

- :adi:`AD5755-1 Product Page <AD5755-1>`
- :adi:`AD5700-1 Product Page <AD5700-1>`
- :adi:`ADuM3482 Product Page <ADUM3482>`
- :adi:`ADuM3151 Product Page <ADUM3151>`
- :adi:`ADP2441 Product Page <ADP2441>`
- :adi:`ADG704 Product Page <ADG704>`
- :adi:`LT8301 Product Page <LT8301>`
- :adi:`EVAL-ADICUP3029 Product Page <EVAL-ADICUP3029>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
