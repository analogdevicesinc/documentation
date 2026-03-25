.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0551

.. _eval-cn0551-ebz:

EVAL-CN0551-EBZ
================

USB-Powered 433 MHz RF Power Amplifier.

Overview
--------

The EVAL-CN0551-EBZ is a four-layer printed circuit board (PCB) that allows
evaluation of the :adi:`CN0551` USB-powered, 433.92 MHz RF power amplifier
circuit. The board is fabricated with a 2 oz./2 oz. copper cladding and
IPC-4101 (or IPC-4103) laminates and bonding materials.

Designed to be used with the :adi:`ADALM-PLUTO`, the EVAL-CN0551-EBZ features
a small form-factor with dimensions of 25.40 mm x 60.25 mm x 1.57 mm (PCB
only). The evaluation board uses standard 50 Ohm SMA coaxial connectors for
its RF signal path for easy integration with RF systems; a male connector is
used for the RF input and a female connector is used for the RF output.
Coplanar waveguides are used for the RF traces on the board, which have a
characteristic impedance of 50 Ohm. A micro-USB connector is used for the
input power, allowing the evaluation board to use most +5 V wall-wart power
supplies available in the market.

.. admonition:: Evaluation Kit Contents

   - EVAL-CN0551-EBZ circuit evaluation board

Required Equipment
------------------

- EVAL-CN0551-EBZ evaluation board
- :adi:`ADALM-PLUTO` RF platform
- +5 V power supply via Micro-USB (minimum 0.5 A recommended)
- RF signal source (max -3 dBm input)
- RF load (antenna or 50 Ohm termination rated for up to +27 dBm output)
- SMA coaxial cables (50 Ohm)

Evaluation Board Hardware
--------------------------

Primary Side
~~~~~~~~~~~~

.. figure:: eval-cn0551-ebz-top.png
   :align: center

   Top View of EVAL-CN0551-EBZ

RFIN Plug (J1)
^^^^^^^^^^^^^^

.. figure:: eval-cn0551-ebz-rfin.png
   :align: right
   :width: 150px

   RFIN Port

The RF input to the evaluation board must be connected to the male SMA
connector **J1**.

.. warning::

   The maximum RF input to the EVAL-CN0551-EBZ is -3 dBm. Do not use a higher
   input level to avoid damaging the circuit.

RFOUT Port (J2)
^^^^^^^^^^^^^^^

.. figure:: eval-cn0551-ebz-rfout.png
   :align: right
   :width: 150px

   RFOUT Port

The RF output of the evaluation board must be connected to the female SMA
connector **J2**.

.. warning::

   The maximum RF output of the EVAL-CN0551-EBZ is +27 dBm. Ensure that the
   RF load to be driven can handle the amplified RF signal. Use an RF
   attenuator if necessary to avoid damage.

LED Indicators (POWER and TOVER)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: eval-cn0551-ebz-led.png
   :align: right
   :width: 100px

   LED Indicators

The evaluation board uses two LEDs to indicate its current status. The green
LED (POWER) lights up when power is present on the board; the red LED (TOVER)
lights up when the amplifier circuit is disabled due to the board temperature
exceeding the temperature switch trip point.

.. list-table:: LED Indications of Board Status
   :header-rows: 1

   * - POWER
     - TOVER
     - Board Status
   * - Off
     - Off
     - No power
   * - On
     - Off
     - Normal operation
   * - On
     - On
     - Overtemperature (:adi:`ADL5324` is disabled)

Power Supply Connector (P1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: eval-cn0551-ebz-usb.png
   :align: right
   :width: 150px

   Micro-USB Port

A +5 V power supply must be connected to the VCC line through the micro-USB
port **P1**.

.. note::

   The total typical supply current of the on-board RF amplifiers is 175 mA.
   However, this requirement increases at higher temperatures (refer to Page
   11, Figure 26 on the :adi:`ADL5324` data sheet and Page 12, Figure 34 on
   the :adi:`AD8353` data sheet for more information). As such, it is
   recommended to use a power supply with a maximum current rating of at
   least 0.5 A to ensure full functionality.

Secondary Side
~~~~~~~~~~~~~~

.. figure:: eval-cn0551-ebz-bottom.png
   :align: center

   Bottom View of EVAL-CN0551-EBZ

Changing the Temperature Switch Trip Point (JP1 and JP2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: eval-cn0551-ebz-jumpers.png
   :align: right
   :width: 100px

   ADT6401 Jumper Settings

The trip point of the temperature switch can be set using the solder jumpers
**JP1** and **JP2**, as shown in the table below. When the board temperature
reaches the trip point, the :adi:`ADT6401` will disable the supply voltage to
the amplifier stages.

.. list-table:: Selecting a Trip Point for the ADT6401
   :header-rows: 1

   * - JP1 Setting
     - JP2 Setting
     - Trip Point
     - Hysteresis
   * - B
     - B
     - +65 deg C
     - 10 deg C
   * - A
     - B
     - +75 deg C
     - 10 deg C
   * - No solder jumper
     - B
     - +85 deg C
     - 10 deg C
   * - B
     - A
     - +95 deg C
     - 10 deg C
   * - A
     - A
     - +105 deg C
     - 10 deg C
   * - No solder jumper
     - A
     - +115 deg C
     - 10 deg C
   * - B
     - No solder jumper
     - +5 deg C
     - 2 deg C
   * - A
     - No solder jumper
     - -5 deg C
     - 2 deg C
   * - No solder jumper
     - No solder jumper
     - -15 deg C
     - 2 deg C

.. important::

   Due to considerable thermal dissipation of the RF amplifiers, the last three
   options (trip points at +5 deg C, -5 deg C, and -15 deg C) should not be
   used.

Connecting the EVAL-CN0551-EBZ to the ADALM-PLUTO
---------------------------------------------------

.. figure:: cn0417.png
   :align: center
   :width: 400px

   Connecting the evaluation board to the ADALM-PLUTO

.. note::

   An EVAL-CN0417-EBZ is shown in this picture. However, the same connections
   also apply for the EVAL-CN0551-EBZ.

To properly operate the EVAL-CN0551-EBZ using the :adi:`ADALM-PLUTO`, follow
the steps below:

#. Connect the 5 V DC power source to the micro-USB port **P1**. Upon applying
   power to the board, the green LED indicator for POWER will light up.
#. Connect the Tx port of the :adi:`ADALM-PLUTO` to the RFIN plug **J1**. The
   RF signal will pass through an on-board SAW filter and will be AC-coupled to
   the RF amplifier input.
#. Connect the RF load (usually an antenna) to the female SMA connector **J2**.

.. warning::

   Do not directly connect the RFOUT port of the EVAL-CN0551-EBZ to the Rx
   port of the :adi:`ADALM-PLUTO`. The maximum RF input that the ADALM-PLUTO
   can safely handle is +2.5 dBm.

Documents
---------

- :adi:`CN0551 Circuit Note <CN0551>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0551-EBZ Design & Integration Files
   <https://www.analog.com/cn0551-designsupport>`__

   - Schematics
   - Bill of Materials
   - Gerber Files
   - Allegro Layout Files
   - Assembly Drawing

Additional Information
----------------------

- :adi:`ADL5324 Product Page <ADL5324>`
- :adi:`AD8353 Product Page <AD8353>`
- :adi:`ADT6401 Product Page <ADT6401>`
- :adi:`ADG901 Product Page <ADG901>`
- :adi:`ADP196 Product Page <ADP196>`
- :adi:`ADM7160 Product Page <ADM7160>`
- :adi:`LTM4693 Product Page <LTM4693>`
- :adi:`ADALM-PLUTO Product Page <ADALM-PLUTO>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
