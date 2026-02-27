.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/hardware/cn0414

.. _eval-cn0414-ardz:

EVAL-CN0414-ARDZ
=================

PLC/DCS Quad-Channel Analog Input with HART.

Overview
--------

:adi:`CN0414` is an Arduino-compatible shield that provides a complete, fully
isolated, highly flexible, quad-channel analog input system suitable for
programmable logic controllers (PLCs) and distributed control system (DCS)
applications that require multiple voltage inputs and 4 mA to 20 mA current
inputs. Additionally, the 4--20 mA inputs provide HART communication to remote
field devices.

The circuit uses the :adi:`AD4111`, a low power, low noise, 24-bit,
sigma-delta analog-to-digital converter (ADC) that integrates an analog front
end (AFE) for fully differential or single-ended, rail-to-rail, bipolar,
+/-10 V voltage inputs and 0 mA to 20 mA current inputs. The :adi:`AD5700-1`
is the industry's lowest power and smallest footprint HART-compliant modem, used
in conjunction with the current input channels to form a HART-compatible,
4 mA to 20 mA receiver solution. The :adi:`ADG704` multiplexer provides HART
connectivity to the multiple current input channels. The :adi:`ADuM5411` and
:adi:`ADuM3151` provide digital line and power isolation. The :adi:`ADP2441`
36 V step-down dc-to-dc regulator accepts an industrial standard 24 V supply
(with wide tolerance on the input voltage) and steps it down to 7.5 V for the
system.

This user guide describes how to use the :adi:`EVAL-ADICUP3029` and evaluation
software to configure and collect data from the EVAL-CN0414-ARDZ evaluation
board.

.. figure:: images/cn0414_board.png
   :align: center
   :width: 500

   EVAL-CN0414-ARDZ Evaluation Board

Simplified Functional Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/cn0414_simplified_block_diagram.png
   :align: center
   :width: 600

   CN0414 Simplified Functional Block Diagram

.. toctree::

   hardware
   software

Documents
---------

- :adi:`CN0414 Circuit Note <CN0414>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0414-ARDZ Design & Integration Files
   <https://www.analog.com/cn0414-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information
----------------------

- :adi:`AD4111 Product Page <AD4111>`
- :adi:`AD5700-1 Product Page <AD5700-1>`
- :adi:`ADuM5411 Product Page <ADUM5411>`
- :adi:`ADuM3151 Product Page <ADUM3151>`
- :adi:`ADP2441 Product Page <ADP2441>`
- :adi:`ADG704 Product Page <ADG704>`
- :adi:`EVAL-ADICUP3029 Product Page <EVAL-ADICUP3029>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
