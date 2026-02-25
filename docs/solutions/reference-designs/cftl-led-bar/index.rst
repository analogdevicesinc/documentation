.. _cftl-led-bar:

CFTL-LED-BAR
=============

RGB LED Light Bar.

Description
-----------

The :adi:`CFTL-LED-BAR <CftL-LED-Bar>` is a board that contains LEDs with 3
different spectral outputs (627 nm, 530 nm and 470 nm). Each of the three
channels contains a string of four LEDs in series able to handle currents of
up to 1 A.

.. figure:: cftl-led-bar.jpg
   :align: center

   CFTL-LED-BAR board

**Recommended LEDs:**

- Lumileds Red LED -- **LXM5-PD01**
- Lumileds Green LED -- **LXML-PM01-0080**
- Lumileds Blue LED -- **LXML-PB02**
- `Lumileds Datasheet <https://www.lumileds.com/uploads/265/DS68-pdf>`__

Connectors
----------

Screw Terminals
~~~~~~~~~~~~~~~

Screw terminals P1, P5 and P9 are connectors for the anode and cathode for each
of the red, green and blue channels of the CFTL-LED-BAR. Pin 1 is the anode
and is to be connected to the positive terminal of the source while pin 2 is
the cathode and is to be connected to the negative terminal of the source.

3-Pin Headers
~~~~~~~~~~~~~

The 3-pin header is used to add LEDs to the series string of each channel.
Placing a shunt on +XLEDN, where X is for the channel to be controlled and N
refers to the LED number, adds the next LED on the string and placing the
shunt on GND position terminates the string, connecting the last LED to the
negative terminal.

.. figure:: cftl-led-bar_silkscreen.jpg
   :align: center

   CFTL-LED-BAR board silkscreen showing 3-pin header layout

LED Ratings
-----------

Red Channel
~~~~~~~~~~~

Each LED on this string has a typical forward voltage of 2.9 V and is tested
with 500 mA of current. Adding LEDs to the string of LEDs in series will
result in a higher forward voltage. Please see the table below for reference:

.. list-table:: Red Channel Forward Voltage
   :header-rows: 1
   :widths: 20 30

   * - No. of LEDs
     - Minimum Forward Voltage Required
   * - 1
     - 2.9 V
   * - 2
     - 5.8 V
   * - 3
     - 8.7 V
   * - 4
     - 11.6 V

Green Channel
~~~~~~~~~~~~~

Each LED on this string has a typical forward voltage of 3.21 V and is tested
with 500 mA of current. Adding LEDs to the string of LEDs in series will
result in a higher forward voltage. Please see the table below for reference:

.. list-table:: Green Channel Forward Voltage
   :header-rows: 1
   :widths: 20 30

   * - No. of LEDs
     - Minimum Forward Voltage Required
   * - 1
     - 3.21 V
   * - 2
     - 6.42 V
   * - 3
     - 9.63 V
   * - 4
     - 12.84 V

Blue Channel
~~~~~~~~~~~~

Each LED on this string has a typical forward voltage of 2.95 V and is tested
with 500 mA of current. Adding LEDs to the string of LEDs in series will
result in a higher forward voltage. Please see the table below for reference:

.. list-table:: Blue Channel Forward Voltage
   :header-rows: 1
   :widths: 20 30

   * - No. of LEDs
     - Minimum Forward Voltage Required
   * - 1
     - 2.95 V
   * - 2
     - 5.90 V
   * - 3
     - 8.85 V
   * - 4
     - 11.80 V

Schematic, PCB Layout, Bill of Materials
-----------------------------------------

`CFTL-LED-BAR Design & Integration Files <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/cftl-led-bar-designsupport.zip>`__

- Schematic
- PCB Layout
- Bill of Materials
- Allegro Project

Related Hardware
-----------------

- :ref:`EVAL-CN0410-ARDZ LED Driver <eval-cn0410-ardz>` -- CN0410 3-Channel LED
  Driver

.. note::

   This is a hardware-only device with no evaluation software. Use with the
   :ref:`EVAL-CN0410-ARDZ <eval-cn0410-ardz>` 3-channel LED driver for
   programmable control.

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
