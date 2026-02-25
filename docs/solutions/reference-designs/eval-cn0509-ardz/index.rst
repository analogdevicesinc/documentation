.. _eval-cn0509-ardz:

EVAL-CN0509-EBZ
================

Wide Input Range (5 V to 100 V) USB Charger.

Overview
--------

:adi:`CN0509` is a wide input range (5 V to 100 V) USB charger capable of
providing up to 2 A at 5 V from a wide range of DC sources including solar
panels, fully charged or half-discharged car batteries, -48 V telecom backup
supplies, random stacks of alkaline cells, treadmill motors hacked to run as
generators, wind turbines, and more. The circuit uses a combination of the
wide-input :adi:`LTC7103` buck converter and an isolated :adi:`LT8302` flyback
converter.

The circuit accepts DC voltage from 5 V to 100 V and produces an isolated 5 V
supply via a standard USB connector. The outer case of many cell phones and
other portable electronics are often electrically connected to USB ground. As
such, isolation is necessary in situations in which the power source's
relationship to Earth ground is unknown.

The circuit will survive up to 100 V reverse connection to a power source, with
a green LED indicating correct input polarity and a red LED indicating reverse
polarity.

.. figure:: picture1.png
   :align: center
   :width: 500px

   EVAL-CN0509-EBZ board

Features
--------

- Wide input range: 5 V to 100 V
- Provides isolated and regulated 5 V output
- Provides up to 2 A output current
- Two USB output ports for convenience
- Survives 100 V reverse polarity connection
- Polarity indicator LEDs (green = correct, red = reversed)

Required Equipment
------------------

- EVAL-CN0509-EBZ circuit evaluation board
- DC power supply (any voltage, 5 V to 100 V), such as solar panels, car
  batteries, -48 V telecom backup supplies, alkaline cell stacks, generators,
  or wind turbines
- USB multimeter tester (or equivalent)
- USB Type-A to Micro-USB / Type-C / Lightning cable
- A device with USB charging capability (cell phone, tablet, or portable
  power pack) and a USB charging cable for the device

Board Layout
------------

.. figure:: block_dia.png
   :align: center
   :width: 600px

   EVAL-CN0509-EBZ block diagram

- **P1** -- Screw terminal block for input supply
- **P2** -- USB output connectors for load (two ports)
- **DS1** -- Green LED (correct polarity indicator)
- **DS2** -- Red LED (reverse polarity indicator)

Test Points
~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Test Point
     - Function
   * - TP1
     - :adi:`LTC7103` output voltage programming pin (VPRG2). Left floating
       to program 12 V fixed output.
   * - TP6
     - Voltage input to the :adi:`LTC7103`
   * - PGOOD
     - :adi:`LTC7103` open-drain power good output
   * - CLKOUT
     - :adi:`LTC7103` output clock signal
   * - IMON
     - Average output current monitor. Generates 0.4 V to 1.3 V
       corresponding to 0 A to 2.5 A average output current.
   * - ICTRL
     - :adi:`LTC7103` ICTRL pin. Programs average output current in constant
       current mode. Left floating to set average output current to 2.5 A and
       peak current limit to 3.7 A.
   * - 12V
     - 12 V output voltage of the :adi:`LTC7103`
   * - GND1
     - Ground relative to input supply
   * - VBUS
     - USB VBUS voltage (typically 5 V)
   * - D+
     - USB data+ signal
   * - D-
     - USB data- signal
   * - GND
     - Isolated ground relative to output

USB Output Connectors
~~~~~~~~~~~~~~~~~~~~~

.. figure:: usb_stack.png
   :align: center
   :width: 600px

   USB output connectors

The board provides a dual-port stacked USB Type-A connector:

- **Bottom receptacle** -- Includes a USB Dedicated Charging Port (DCP)
  controller that enables up to 2 A charging on devices from various
  manufacturers.
- **Top receptacle** -- For general-purpose charging, rated up to 500 mA.

Hardware Setup
--------------

.. figure:: setup_2.png
   :align: center
   :width: 850px

   Test setup

#. Connect the input DC supply to **P1** on the EVAL-CN0509-EBZ.

   .. warning::

      Ensure safe connection practices as the circuit may deal with input
      voltages up to 100 V.

#. Turn on the DC supply.
#. The circuit determines the input connection polarity through the LED
   indicators:

   - If **DS1** (green LED) turns on, polarity is correct and the circuit
     delivers up to 10 W on the **P2** USB output ports.
   - If **DS2** (red LED) illuminates, turn off the input supply, disconnect
     the power inputs, swap the power leads, and reconnect the supply outputs
     to **P1**.

#. Connect the USB multimeter tester to the lower USB port on the
   EVAL-CN0509-EBZ.
#. Connect a fast-charge capable device to the USB multimeter tester using the
   charging cable of the device.
#. Verify the USB multimeter tester shows the device pulling more than 500 mA
   but less than 2 A.
#. To test the upper port, connect the USB multimeter tester to the upper USB
   port. Verify the device pulls approximately 500 mA.

.. note::

   Each device has its own charge controller circuitry that may limit the
   charging current if the voltage on the load drops below a certain level.
   The maximum charging current on the P2 lower port that CN0509 can provide
   is available when the output voltage to the load is greater than 5 V.

.. figure:: max_curr.png
   :align: center
   :width: 200px

   Maximum charging current on P2 lower port

Documents
---------

- :adi:`CN0509 Circuit Note <CN0509>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0509-EBZ Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0509-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project
   - LTSpice Simulations

Additional Information
----------------------

- :adi:`LTC7103 Product Page <LTC7103>`
- :adi:`LT8302 Product Page <LT8302>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
