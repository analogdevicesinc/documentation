.. _eval-cn0569-ardz:

EVAL-CN0569-ARDZ
================

Infrared Light Angle Sensor Module for Gesture Recognition.

.. figure:: eval-cn0569-pmdz-angle-web.gif
   :align: center

   EVAL-CN0569-PMDZ evaluation board.

Overview
--------

The :adi:`EVAL-CN0569-PMDZ <CN0569>` is a 4-layer printed circuit board (PCB)
that allows evaluation of the :adi:`CN0569 Circuit Note <CN0569>` infrared
light angle sensor module for gesture recognition. The board measures
2.7 in (68.58 mm) x 0.8 in (20.32 mm) x 0.062 in (1.5748 mm) and is
fabricated with 0.5 oz./1 oz. copper cladding (external layers overplated to
1.5 oz.).

The design uses the :adi:`ADPD1080` photometric front-end device with two
:adi:`ADPD2140` infrared photodetector sensors positioned 1 in (25.4 mm) apart,
enabling dual-axis gesture detection. The kit includes two 3D-printed optical
baffles for optimal sensor performance. The board uses a standard I2C Pmod
hardware interface for connection to controller platforms.

Features
~~~~~~~~

- I2C Pmod connector interface (1x6, 0.1-inch right-angle male header)
- :adi:`ADPD1080` photometric front-end
- Two :adi:`ADPD2140` sensors for dual-axis gesture detection
- Operates from Pmod VCC (3.3 V typical)
- Internal 1.8 V regulated supply for :adi:`ADPD1080`
- Breakaway line for custom sensor spacing configurations
- Supports four directional gestures (up, down, left, right)
- Multiple test points for GPIO, LED drivers, and photodiode inputs

Evaluation Board Hardware
-------------------------

.. figure:: eval-cn0569-pmdz-top-labels.png
   :align: center

   EVAL-CN0569-PMDZ top view with component labels.

I2C Pmod Connector (P1)
~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-CN0569-PMDZ uses a standard 1x6, 0.1-inch right-angle male header
for the I2C Pmod interface.

.. figure:: eval-cn0569-pmdz-i2c-pmod-connector.png
   :align: center

   I2C Pmod connector (P1) pinout.

.. list-table::
   :header-rows: 1

   * - Pin
     - Name
     - Function
   * - 1
     - INT
     - GPIO0 (function depends on :adi:`ADPD1080` configuration)
   * - 2
     - RESET
     - No connection
   * - 3
     - SCL
     - I2C Clock from controller to :adi:`ADPD1080`
   * - 4
     - SDA
     - I2C Data from controller to :adi:`ADPD1080`
   * - 5
     - GND
     - Ground
   * - 6
     - VCC
     - Pmod VCC input power

.. note::

   Version 1.0.0 of the Digilent Pmod Specification required 2x4 headers.
   The board works with older controllers (such as the
   :adi:`EVAL-ADICUP3029 <EVAL-ADICUP3029>`), but the INT pin requires
   manual wiring for GPIO0 access.

Test Points (Power, GPIO, and LED Driver Pins)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The board exposes multiple test points for advanced applications and external
component integration.

.. figure:: eval-cn0569-pmdz-io-led-test-points.png
   :align: center

   GPIO and LED driver test point locations.

.. list-table::
   :header-rows: 1

   * - Test Point
     - Hardware Pin
     - Function
   * - IO0
     - ADPD1080 GPIO0
     - General Purpose I/O 0
   * - IO1
     - ADPD1080 GPIO1
     - General Purpose I/O 1
   * - LED1
     - ADPD1080 LEDX1
     - LED Driver 1 (IR LED by default)
   * - LED2
     - ADPD1080 LEDX2
     - LED Driver 2 (unused, external capable)
   * - LED3
     - ADPD1080 LEDX3
     - LED Driver 3 (unused, external capable)
   * - 1V8
     - ADPD1080 AVDD/DVDD
     - 1.8 V regulated supply
   * - VCC
     - Pmod VCC
     - Input power
   * - VLED
     - LED Supply
     - IR LED supply (shorted to Pmod VCC by default)
   * - GND
     - Ground
     - Ground

.. note::

   - IO0 and IO1 operate at 1.8 V logic levels directly from the
     :adi:`ADPD1080` pins. Level shifting is required for non-1.8 V circuits.
   - GPIO0 is also available via the INT pin on the Pmod connector, using
     Pmod VCC logic level.
   - External LED maximum voltage is 3.6 V.
   - LED1 uses a zero-ohm resistor (R1); removal of R1 is required for
     external LED substitution.

Test Points (Photodiode Inputs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The board uses two :adi:`ADPD2140` sensors spaced 1 in (25.4 mm) apart by
default. The design enables custom spacing through the breakaway
functionality.

.. list-table::
   :header-rows: 1

   * - Test Point
     - Hardware Pin
     - Function
     - Paired Pin
   * - PD5
     - ADPD1080 PD5
     - Photodiode Input (Anode) 5
     - XR2
   * - PD6
     - ADPD1080 PD6
     - Photodiode Input (Anode) 6
     - XL2
   * - PD7
     - ADPD1080 PD7
     - Photodiode Input (Anode) 7
     - YB2
   * - PD8
     - ADPD1080 PD8
     - Photodiode Input (Anode) 8
     - YT2
   * - PDC
     - ADPD1080 PDC
     - Photodiode Common Cathode Bias
     - PDC

Breakaway Feature
~~~~~~~~~~~~~~~~~

.. figure:: eval-cn0569-pmdz-breakaway.png
   :align: center

   Breakaway line and photodiode test point locations.

The board features a breakaway line allowing users to separate the two
:adi:`ADPD2140` sensors and manually wire the test points at custom spacing
distances for tailored gesture recognition applications.

Software and Demo
-----------------

.. figure:: cn0569-gesture-directions.png
   :align: center

   Supported gesture directions (left, right, up, down).

A basic gesture sensing example application was developed using the
:adi:`EVAL-ADICUP3029 <EVAL-ADICUP3029>` platform. The demonstration
recognizes four directional gestures (left, right, up, down) using the dual
infrared sensor configuration.

Hardware Setup
~~~~~~~~~~~~~~

The following hardware is required for the gesture sensing demo:

- :adi:`EVAL-ADICUP3029 <EVAL-ADICUP3029>` motherboard
- EVAL-CN0569-PMDZ circuit board
- Micro-USB to USB cable
- PC or laptop with USB port

Connection instructions:

1. Connect CN0569 pins 3-6 to the EVAL-ADICUP3029 P9 Pmod connector
   (top row, leaving pins 1-2 unconnected toward center).
2. Connect CN0569 pin 1 via a breadboard wire to EVAL-ADICUP3029 P7 pin 5
   (GPIO0 interrupt connection for clock calibration).
3. Connect a Micro-USB cable to the EVAL-ADICUP3029 P10 connector.

Firmware
~~~~~~~~

The firmware is written in C and executes on the :adi:`EVAL-ADICUP3029 <EVAL-ADICUP3029>`
controller. It initializes the hardware and runs an IIO (Industrial I/O)
server for device communication with the host PC.

The firmware can be compiled using CrossCore Embedded Studio (version 2.10.1
or later) with the following support packages:

- ADuCM302x DFP (version 3.2.0 or later)
- ADICUP3029 BSP (version 1.1.0 or later)

Alternatively, a pre-built ``.hex`` file can be downloaded from the
:git-no-OS:`iio_adpd1080 GitHub releases <releases>` and loaded onto the
EVAL-ADICUP3029 by dragging and dropping to the DAPLINK drive.

The firmware source code is available at
:git-no-OS:`projects/iio_adpd1080`.

Python Application
~~~~~~~~~~~~~~~~~~

A Python application running on the host computer connects to the
EVAL-ADICUP3029 via USB serial, samples photodiode current data, and
implements gesture recognition algorithms.

To run the Python application:

1. Install the pyadi-iio library:

   .. code-block:: bash

      pip install pyadi-iio

2. Configure the correct COM port in the example file.

3. Execute the application:

   .. code-block:: bash

      python cn0569_theremin_module.py

The Python examples are available at
:git-pyadi-iio:`examples/cn0569`.

Alternatively, the `IIO Oscilloscope <https://github.com/analogdevicesinc/iio-oscilloscope>`__
tool can be used for device interaction.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

`EVAL-CN0569-PMDZ Design & Integration Files <https://www.analog.com/cn0569-designsupport>`__

- Schematics
- Gerber Files
- Assembly Drawings
- Bill of Materials

More Information and Useful Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`CN0569 Circuit Note Page <CN0569>`
- :adi:`ADPD1080 Product Page <ADPD1080>`
- :adi:`ADPD2140 Product Page <ADPD2140>`
- :adi:`EVAL-ADICUP3029 Product Page <EVAL-ADICUP3029>`

Help and Support
~~~~~~~~~~~~~~~~

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
