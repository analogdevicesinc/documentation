.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0508

.. _eval-cn0508-rpiz:

EVAL-CN0508-RPIZ
=================

Single-Channel 75 W Bench Power Supply with Raspberry Pi Control.

Overview
--------

:adi:`CN0508` provides a single-channel, 75 W bench power supply featuring an
adjustable output voltage of 0 V to 27.5 V, and constant current limiting of
0 A to 3 A using the combination of parallel :adi:`LT3081` linear regulators,
a synchronous step-down :adi:`LT8612`, a :adi:`LT3092` current source, and a
tiny :adi:`LTC1983` negative supply.

The output voltage can be set manually using a potentiometer or digitally via
Raspberry Pi with a :adi:`AD5683R` DAC, through the "analog-AND" function
circuit. A :adi:`AD7124-4` 24-bit sigma-delta ADC provides measurement
readings of output voltage and output current as well as other diagnostic
parameters.

The circuit features low output ripple with low output capacitance, excellent
transient response, remains in regulation during short-circuit, and stays cool
with no bulky heat sinks. It can be coupled with an AC/DC converter or powered
from a DC source.

.. figure:: dsc04840.png
   :width: 500px
   :align: center

   EVAL-CN0508-RPIZ Circuit Evaluation Board

Features
--------

- Single 0--27.5 V DC adjustable output with manual and software control via
  Raspberry Pi
- 0--3 A constant current limit
- Supports both HDMI displays and local touchscreens (TFT screens)
- Low output ripple with low output capacitance
- Excellent transient response
- Stays cool with no bulky heat sinks

.. video:: https://www.youtube.com/watch?v=FEnbV_-a7qc

Required Equipment
------------------

**Hardware**

- EVAL-CN0508-RPIZ circuit evaluation board
- Raspberry Pi Zero W
- 75 W to 120 W offline power supply or bench power supply
  (Globtek TR9CR3000T00-IM(R6B))
- Various power resistors, dummy load, or test circuits
- 40-pin ribbon cable (optional)
- Monitor with HDMI display
- Mini HDMI to HDMI adapter
- HDMI cable
- 16 GB or larger SD card
- Micro-USB dongle
- USB keyboard and mouse
- USB hub

**Software**

- :doc:`ADI Kuiper Linux </linux/kuiper/index>` image

Board Layout
------------

.. figure:: top1.png
   :width: 550px
   :align: center

   EVAL-CN0508-RPIZ Circuit Evaluation Board Top View

.. figure:: side1.png
   :width: 450px
   :align: center

   EVAL-CN0508-RPIZ Circuit Evaluation Board Side View

- **P1** -- Screw terminal block for input supply
- **P2** -- 5.5 mm x 2.5 mm barrel jack for input supply
- **P3** -- 40-pin connector for Raspberry Pi
- **P7** -- Positive output jack
- **P8** -- Ground output jack
- **R43** -- Manual output voltage potentiometer
- **R14** -- Manual output current limit potentiometer
- **P12** -- Fan control output header

Running the System
------------------

.. figure:: bd_1.png
   :width: 500px
   :align: center

   Test Setup Functional Block Diagram

#. Set solder jumpers for the desired settings.
#. Complete the hardware setup. Ensure the input supply, Raspberry Pi, load,
   and fan are properly connected.
#. Burn the SD card with the latest ADI Kuiper Linux image. Insert the flashed
   SD card into the Raspberry Pi.
#. Turn on the input supply. Wait for the Raspberry Pi to boot.
#. Open the terminal and configure the device tree overlay file (see
   `Software Setup`_). Reboot the Raspberry Pi after saving **config.txt**.
#. Wait for boot to complete. Open IIO Oscilloscope and select the CN0508 tab.
#. Change output voltage and view measurements (current, temperature,
   potentiometer readings).
#. For manual control, rotate the knob of R43. The output follows the lower
   voltage between the potentiometer and DAC.
#. Change current limit by turning the knob of R14.
#. The Raspberry Pi must be powered down properly to prevent eventual corruption
   of the SD card. Press **S1** and wait for the green heartbeat LED to stop
   blinking. At that point, power is safe to be removed.
#. Alternatively, click the ADI logo, scroll to the bottom, click power off, and
   wait for the heartbeat LED to stop blinking before removing power.

Solder Jumper Configuration
----------------------------

.. figure:: assembly_top6.png
   :width: 1000px
   :align: center

   EVAL-CN0508-RPIZ Evaluation Board Solder Jumper Guide

-VCC: Negative VCC Supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Selects the negative supply of the :adi:`LT6015` amplifiers. By default, the
shunt is placed connecting pin 1 and 2 to source supply from the -5 V output of
:adi:`LTC1983`.

.. list-table::
   :header-rows: 1

   * - Shunt Position
     - Negative Supply
   * - 1 and 2 (default)
     - -5 V (from :adi:`LTC1983`)
   * - 2 and 3
     - Ground

- Connecting pins 1 and 2 connects the LT6015 V- to -5 V, allowing operation at
  ground.
- Connecting pins 2 and 3 connects the LT6015 V- to ground.

CS_ADC: ADC Chip Select Mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Selects the mapping of the :adi:`AD7124-4` ADC chip select to RPi. By default,
the shunt connects pin 1 and 2 which selects GPIO27.

.. list-table::
   :header-rows: 1

   * - Shunt Position
     - CS_ADC Mapping to RPi
   * - 1 and 2 (default)
     - GPIO27 (Pin 13)
   * - 2 and 3
     - CS0 (Pin 24)

CS_DAC: DAC Chip Select Mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Selects the mapping of the :adi:`AD5683R` DAC chip select to RPi. By default,
the shunt connects pin 1 and 2 which selects GPIO22.

.. list-table::
   :header-rows: 1

   * - Shunt Position
     - CS_DAC Mapping to RPi
   * - 1 and 2 (default)
     - GPIO22 (Pin 15)
   * - 2 and 3
     - CS1 (Pin 26)

ADC_INT: ADC Interrupt Mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Selects the mapping of the :adi:`AD7124-4` interrupt from its DOUT/RDY pin to
RPi. By default, the shunt connects pin 1 and 2 which selects GPIO23.

.. list-table::
   :header-rows: 1

   * - Shunt Position
     - ADC_INT Mapping to RPi
   * - 1 and 2 (default)
     - GPIO23 (Pin 16)
   * - 2 and 3
     - GPIO25 (Pin 22)

VCTRL: Output Voltage Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enables users to choose how to control the output voltage between electronic and
manual mode (chooses the lower setting between the two) versus exclusively manual
mode. Output can be controlled electronically through the DAC and manually
through the potentiometer knob. By default, the shunt connects pin 1 and 2 which
enables both electronic and manual control.

.. list-table::
   :header-rows: 1

   * - Shunt Position
     - Control Mode
   * - 1 and 2 (default)
     - Electronic and knob control
   * - 2 and 3
     - Knob control only

.. note::

   Even in purely knob control mode, the RPi must remain connected. The 3.3 V
   from the RPi supplies the ADC and DAC circuitry.

EEPROM_ID: EEPROM Address Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sets the EEPROM I2C address via P4, P5, P6 solder jumpers connected to A2, A1,
A0 pins of U7. The default address configuration is "111". This EEPROM I2C
address is configurable from 0x51 to 0x57. It cannot be set to 0x50 since U4
already uses this address for RPi HAT identification.

.. list-table::
   :header-rows: 1

   * - A0
     - A1
     - A2
     - Address
   * - 0
     - 0
     - 1
     - 0x51
   * - 0
     - 1
     - 0
     - 0x52
   * - 0
     - 1
     - 1
     - 0x53
   * - 1
     - 0
     - 0
     - 0x54
   * - 1
     - 0
     - 1
     - 0x55
   * - 1
     - 1
     - 0
     - 0x56
   * - 1
     - 1
     - 1
     - 0x57 (default)

Hardware Setup
--------------

Raspberry Pi Connection
~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect a mini HDMI to HDMI adapter on the Raspberry Pi Zero W and connect
   to an external monitor.

   .. figure:: hdmi_2.png
      :width: 300px
      :align: center

      Hardware connection of Raspberry Pi to Monitor Display

#. Connect a micro-USB to USB Type-A female adapter on the RPi USB port. Attach
   a USB hub with keyboard and mouse.

   .. figure:: micro.png
      :width: 300px
      :align: center

      Hardware connection of Input Devices to Raspberry Pi

#. Connect the Raspberry Pi to EVAL-CN0508-RPIZ through **P3** (40-pin
   connector), either directly on the bottom side or via a ribbon cable.

   .. figure:: rpi3.png
      :width: 600px
      :align: center

      Hardware connection of EVAL-CN0508-RPIZ and Raspberry Pi Zero W

Input Supply
~~~~~~~~~~~~

Connect power through **P1** (screw terminal) or **P2** (barrel jack). Use only
one input. Maximum input rating: 40 V, 3 A (120 W).

.. figure:: supply1.png
   :width: 700px
   :align: center

   Hardware Connection of Input Power Supply to EVAL-CN0508-RPIZ

Output Connections
~~~~~~~~~~~~~~~~~~

Connect a resistive load, electronic load, or multimeter to output banana jacks
**P7** (positive) and **P8** (ground). Ensure the load's power consumption will
not cause overheating.

.. figure:: out1.png
   :width: 400px
   :align: center

   EVAL-CN0508-RPIZ Evaluation Board Output Connections

.. figure:: load1.png
   :width: 550px
   :align: center

   EVAL-CN0508-RPIZ Evaluation Board Connected to a Load

Fan Connection
~~~~~~~~~~~~~~

If either regulator's temperature reaches 60 °C or above, the 5 V fan output on
**P12** turns on.

.. figure:: fan1.png
   :width: 600px
   :align: center

   Hardware Connection of EVAL-CN0508-RPIZ to a Fan

Software Setup
--------------

Loading the SD Card
~~~~~~~~~~~~~~~~~~~~

Install :doc:`ADI Kuiper Linux </linux/kuiper/index>` on an SD card following the
instructions on the Kuiper Linux page.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the Raspberry Pi hardware configuration procedure in the Kuiper Linux
documentation, substituting the following lines in **config.txt**:

.. code-block:: none

   dtoverlay=rpi-cn0508,rotate=270,speed=64000000,fps=30
   hdmi_cvt=720 480 60 1 0 0 0
   dtparam=spi=on
   dtparam=i2c1=on
   dtparam=i2c_arm=on
   dtoverlay=gpio-shutdown,gpio_pin=17,active_low=1,gpiopull=up
   dtparam=act_led_gpio=13
   dtparam=act_led_trigger=heartbeat

The lines below ``dtoverlay`` enable a heartbeat LED (DS3, green) and a shutdown
button (S1) for safe power-down.

.. tip::

   Ensure you have the latest version of
   :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`.

IIO Oscilloscope Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~

EVAL-CN0508-RPIZ allows electronic control of the output voltage and display of
diagnostics through the :adi:`AD7124-4` ADC, all accessible via the CN0508
plugin in IIO Oscilloscope.

.. figure:: iioscope_508_032021.jpg
   :width: 500px
   :align: center

   Graphical User Interface (GUI) window of ADI IIO Oscilloscope

- **DAC output** -- Set a value from 0 to 65535 to vary the DAC output voltage.
- **Temperature Monitor** -- Shows temperature readings of the two :adi:`LT3081`
  regulators.
- **DC Supply** -- Displays output voltage and output current. The output
  voltage is set to the lower of the DAC and potentiometer setpoints.
- **Potentiometers** -- Shows the position of the voltage and current limit
  potentiometers. An indicator flag is raised if the output current reaches 95%
  of the current limit setpoint or if the measured output voltage falls more than
  0.5 V below the lower of the DAC setpoint and the potentiometer setpoint.
- **Input Supply** -- Displays the input voltage on P1 or P2 connectors.

Documents
---------

- :adi:`CN0508 Circuit Note <CN0508>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0508-RPIZ Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0508-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project
   - LTSpice Simulations

Additional Information
----------------------

- :adi:`LT8612 Product Page <LT8612>`
- :adi:`LT3081 Product Page <LT3081>`
- :adi:`LT8609 Product Page <LT8609>`
- :adi:`LTC1983 Product Page <LTC1983>`
- :adi:`AD5683R Product Page <AD5683R>`
- :adi:`LT6015 Product Page <LT6015>`
- :adi:`AD7124-4 Product Page <AD7124-4>`
- :adi:`ADCMP392 Product Page <ADCMP392>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
