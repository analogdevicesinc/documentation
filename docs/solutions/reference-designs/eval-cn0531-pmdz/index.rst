.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0531

.. _eval-cn0531-pmdz:

EVAL-CN0531-PMDZ
=================

1 ppm, 20-Bit, Voltage Output DAC SPI Pmod Board.

Overview
--------

The :adi:`EVAL-CN0531-PMDZ <CN0531>` is a minimalist 1 ppm, 20-bit,
plus/minus 1 LSB INL, DAC SPI Pmod board suitable for medical instrumentation,
test and measurement equipment, industrial control, or high-end scientific and
aerospace instrumentation. This module is designed as a low-cost alternative to
the fully-featured :adi:`AD5791` evaluation board. Multiple voltage references
and power options are available to adapt this module depending on the
application.

With this module, the user can use the onboard positive voltage reference or
connect external references. It is also possible to connect an external buffer
if the onboard buffer does not suit the application. The EVAL-CN0531-PMDZ can
be powered internally or externally, depending on the needs. Additional control
signals can be connected to the digital interface to control this module.

.. figure:: cn0531_top.jpg
   :align: center
   :width: 600

   EVAL-CN0531-PMDZ Evaluation Board

About the AD5791
----------------

The :adi:`AD5791` is a single 20-bit, unbuffered voltage-output
digital-to-analog converter (DAC) that operates from a bipolar supply of up to
33 V. The AD5791 accepts a positive reference input in the range 5 V to
VDD - 2.5 V and a negative reference input in the range VSS + 2.5 V to 0 V.
The AD5791 offers a relative accuracy specification of plus/minus 1 LSB max
and operation is guaranteed monotonic with a plus/minus 1 LSB differential
nonlinearity (DNL) maximum specification.

The device uses a versatile 3-wire serial interface that operates at clock rates
up to 35 MHz and is compatible with standard SPI, QSPI, MICROWIRE, and DSP
interface standards. The device incorporates a power-on reset circuit that
ensures the DAC output powers up to 0 V in a known output impedance state.

Functional Block Diagram
-------------------------

.. figure:: cn0531_functional_block_diagram.jpg
   :align: center

   EVAL-CN0531-PMDZ Functional Block Diagram

Connectors and Configuration
-----------------------------

.. figure:: cn0531_bottom.jpg
   :align: center
   :width: 600

   EVAL-CN0531-PMDZ Board Bottom Side

Supply Options
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Solder Jumper
     - Default Position
     - Description
   * - P6
     - Shorted
     - Internal 3.3 V (connected at IOVDD and P1 pin 2)
   * - P7
     - Shorted
     - External 3.3 V (supply connected at P1 pin 3)
   * - P8
     - Open
     - External voltage supply (disconnected)
   * - P11
     - Shorted
     - External VDD supply (connected at P1 pin 6)
   * - P12
     - Shorted
     - External VSS supply (connected at P1 pin 5)

Voltage Reference Options
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Solder Jumper
     - Default Position
     - Description
   * - P9
     - Shorted
     - Positive reference (connected to onboard 5 V external reference and
       P4 pin 1)
   * - P10
     - Shorted
     - Negative reference (connected to GND and P4 pin 1)

Digital Interface Options
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Solder Jumper
     - Default Position
     - Description
   * - P14
     - Open
     - LDAC connection (disconnected)
   * - P15
     - Open
     - CLR connection (disconnected)
   * - P16
     - Open
     - RESET connection (disconnected)
   * - P13
     - Shorted
     - Output buffer (connected to onboard buffer)

Demo with EVAL-ADICUP3029
--------------------------

The ``ADuCM3029_demo_cn0531`` project provides a solution to control the
:adi:`AD5791` DAC Pmod using the :adi:`EVAL-ADICUP3029`. The AD5791 can be
controlled through a serial UART CLI connected to a host PC.

Demo Requirements
~~~~~~~~~~~~~~~~~

**Hardware**

- :adi:`EVAL-ADICUP3029`
- EVAL-CN0531-PMDZ
- Micro USB to USB cable
- PC or laptop with a USB port

**Software**

- `ADuCM3029_demo_cn0531 demo application
  <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_cn0531>`__
- CrossCore Embedded Studio (2.9.1 or higher)

Hardware Setup
~~~~~~~~~~~~~~

#. Connect the EVAL-CN0531-PMDZ board to the EVAL-ADICUP3029.
#. Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and
   connect it to a computer.

Available CLI Commands
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Command
     - Description
     - Example
   * - ``h``
     - Display available commands
     -
   * - ``drr <addr>``
     - Read a DAC register (address in hex)
     - ``drr 1`` -- read register 1
   * - ``drw <addr> <val>``
     - Write a DAC register (address and value in hex)
     - ``drw 1 18c`` -- set register 1 to 0x18C
   * - ``do <volt>``
     - Update the DAC output voltage (in volts)
     - ``do -2.3`` -- set DAC output to -2.3 V

The ``do`` command for setting the output voltage assumes the onboard 5 V
reference is used.

Obtaining the Software
~~~~~~~~~~~~~~~~~~~~~~

There are two ways to program the ADICUP3029 with the software for CN0531:

#. **Drag and drop** the prebuilt hex file to the DAPLINK drive:
   `ADuCM3029_demo_cn0531.hex
   <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0531.hex>`__

#. **Build from source** using CrossCore Embedded Studio:
   `ADuCM3029_demo_cn0531 source code
   <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_cn0531>`__

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `CN0531 Design and Integration Files
   <https://www.analog.com/cn0531-DesignSupport>`__

   - Schematics
   - Bill of Materials
   - Gerber Files
   - Assembly Drawings
   - Allegro Board File

Additional Information and Useful Links
----------------------------------------

- :adi:`AD5791 Product Page <AD5791>`
- :adi:`AD8675 Product Page <AD8675>`
- :adi:`AD8676 Product Page <AD8676>`
- :adi:`LTC6655 Product Page <LTC6655>`
- :adi:`LT3042 Product Page <LT3042>`
- :adi:`LT3093 Product Page <LT3093>`
- :adi:`LT3471 Product Page <LT3471>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the :ez:`/`.
