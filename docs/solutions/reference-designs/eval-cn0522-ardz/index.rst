.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0522

.. _eval-cn0522-ardz:

EVAL-CN0522-ARDZ
=================

USB-Powered 915 MHz ISM Band RF Power Amplifier.

Overview
--------

The EVAL-CN0522-EBZ is a 6-layer printed circuit board (PCB) that allows
evaluation of the :adi:`CN0522` USB-powered, 915 MHz ISM Band RF power
amplifier circuit. The board is fabricated with 3 oz./3 oz. copper cladding and
IPC-4101 (or IPC-4103) laminates and bonding materials. To improve the thermal
performance, multiple plated vias are used in the design, which are filled with
conductive epoxy.

Designed to be used with the :adi:`ADALM-PLUTO`, the EVAL-CN0522-EBZ features
a small form factor with dimensions of 25.4 mm x 36.957 mm x 1.5748 mm (PCB
only). The evaluation board uses standard 50 Ohm SMA coaxial connectors for its
RF signal path -- a male connector is used for the RF input and a female
connector is used for the RF output. Coplanar waveguides are used for the RF
traces on the board, which have a characteristic impedance of 50 Ohm. A
micro-USB connector is used for the input power, allowing the evaluation board
to use most +5 V wall-wart power supplies available in the market.

**Evaluation Kit Contents:**

- EVAL-CN0522-EBZ circuit evaluation board

Required Equipment
------------------

- EVAL-CN0522-EBZ circuit evaluation board
- :adi:`ADALM-PLUTO` (for signal generation)
- +5 V DC power supply (recommended: 1 A minimum)
- RF load (antenna recommended)
- SMA coaxial cables

Evaluation Board Hardware
-------------------------

Primary Side
~~~~~~~~~~~~

.. figure:: cn0522_revb_primary_with_labels.png
   :width: 600px
   :align: center

   Top View of EVAL-CN0522-EBZ

RFIN Plug (J1)
^^^^^^^^^^^^^^

.. figure:: cn0522_j1.png
   :width: 200px
   :align: right

   RFIN Plug (J1)

The RF input to the evaluation board must be connected to the male SMA
connector **J1**.

.. warning::

   The maximum RF input to the EVAL-CN0522-EBZ is +15 dBm. Do not use a
   higher input level to avoid damaging the circuit.

RFOUT Port (J2)
^^^^^^^^^^^^^^^

.. figure:: cn0522_j2.png
   :width: 200px
   :align: right

   RFOUT Port (J2)

The RF output of the evaluation board is available at the female SMA connector
**J2**.

.. warning::

   The maximum RF output of the EVAL-CN0522-EBZ is +30 dBm. Ensure that the
   RF load to be driven can handle the amplified RF signal. Use an RF
   attenuator if necessary to avoid damage.

LED Indicators (DS1 and DS2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0522_ds1-ds2_led_.png
   :width: 200px
   :align: right

   LED Indicators (DS1 and DS2)

The evaluation board uses two LEDs to indicate its current status:

.. figure:: cn0522_ds1-ds2_table.png
   :width: 350px
   :align: center

   DS1 and DS2 LED Status Table

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - LED
     - Color
     - Description
   * - DS1
     - Green
     - Lights up when power is present on the board
   * - DS2
     - Red
     - Lights up when the amplifier is disabled due to the board temperature
       exceeding the temperature switch trip point

Secondary Side
~~~~~~~~~~~~~~

.. figure:: cn0522_revb_secondary_with_labels.png
   :width: 600px
   :align: center

   Bottom View of EVAL-CN0522-EBZ

Power Supply Connector (P1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0522_p1.png
   :width: 150px
   :align: right

   Power Supply Connector (P1)

A +5 V power supply must be connected to the VCC line through the micro-USB
port **P1**.

.. note::

   The typical supply current of the on-board RF amplifier is 307 mA. However,
   this requirement becomes much higher at higher output power values (refer to
   Page 12, Figure 29 on the :adi:`ADL5605` data sheet). As such, it is
   recommended to use a power supply with a maximum current rating of at least
   1 A for full functionality.

Changing the ADT6402 Trip Point (JP1 and JP2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0522_jp1-jp2_temp_switch_.png
   :width: 150px
   :align: right

   JP1 and JP2 Solder Jumpers

The evaluation board includes the :adi:`ADT6402` temperature switch to disable
the amplifier when the board temperature reaches a trip point. The trip point
can be set using the solder jumpers **JP1** and **JP2**, as shown in the table
below.

.. figure:: cn0522_jp1-jp2_table.png
   :width: 500px
   :align: center

   ADT6402 Trip Point Configuration Table

.. list-table::
   :header-rows: 1
   :widths: 15 15 30

   * - JP1
     - JP2
     - Trip Point
   * - Open
     - Open
     - 55 deg C
   * - Short
     - Open
     - 60 deg C
   * - Open
     - Short
     - 65 deg C
   * - Short
     - Short
     - 70 deg C

.. important::

   Due to the high thermal dissipation of RF amplifiers, the first three and
   last three temperature trip point options in the :adi:`ADT6402` data sheet
   should not be used. Only the 6 usable settings in the 55 deg C to 70 deg C
   range listed above are recommended.

Connecting the EVAL-CN0522-EBZ to the ADALM-PLUTO
---------------------------------------------------

.. figure:: cn0417.png
   :width: 400px
   :align: center

   EVAL-CN0522-EBZ Connected to the ADALM-PLUTO

To properly operate the EVAL-CN0522-EBZ using the :adi:`ADALM-PLUTO`, follow
the steps below:

#. Connect the +5 V DC power source to the micro-USB port **P1**. Upon
   applying power to the board, the green LED indicator **DS1** will light up.
#. Connect the Tx port of the :adi:`ADALM-PLUTO` to the RFIN plug **J1**. The
   RF signal will pass through an on-board SAW filter and be AC-coupled to the
   RF amplifier input.
#. Connect the RF load (usually an antenna) to the female SMA connector
   **J2**.

.. warning::

   Do NOT directly connect the RFOUT port of the EVAL-CN0522-EBZ to the Rx
   port of the :adi:`ADALM-PLUTO`. The maximum RF input that the ADALM-PLUTO
   can safely handle is +2.5 dBm.

Documents
---------

- :adi:`CN0522 Circuit Note <CN0522>`
- `ADL5605 Data Sheet
  <https://www.analog.com/media/en/technical-documentation/data-sheets/ADL5605.pdf>`__

Schematic, PCB Layout, Bill of Materials
----------------------------------------

Assembly Drawing
~~~~~~~~~~~~~~~~

.. figure:: cn0522_assembly_drawing.png
   :width: 400px
   :align: center

   EVAL-CN0522-EBZ Assembly Drawing

Board Dimensions
~~~~~~~~~~~~~~~~

.. figure:: cn0522_dimensions.png
   :width: 800px
   :align: center

   EVAL-CN0522-EBZ Board Dimensions

Design Files
~~~~~~~~~~~~

.. admonition:: Download

   `EVAL-CN0522-EBZ Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0522-DesignSupport.zip>`__

   - Schematics
   - Bill of Materials
   - Gerber Files
   - Allegro Layout
   - Assembly Drawing

Additional Information
----------------------

- :adi:`ADL5605 Product Page <ADL5605>`
- :adi:`LTM8045 Product Page <LTM8045>`
- :adi:`ADT6402 Product Page <ADT6402>`
- :adi:`ADALM-PLUTO Product Page <ADALM-PLUTO>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
