.. _eval-cn0552-pmdz:

EVAL-CN0552-PMDZ
=================

High Resolution, Capacitance-to-Digital Converter PMOD Board.

Overview
--------

The :adi:`EVAL-CN0552-PMDZ <CN0552>` is a PMOD form-factor evaluation board for
the :adi:`AD7746`, a high resolution, sigma-delta capacitance-to-digital
converter (CDC). The architecture features inherent high resolution (24-bit no
missing codes, up to 21-bit effective resolution), high linearity
(plus/minus 0.01%), and high accuracy (plus/minus 4 fF factory calibrated).

.. figure:: actual_hardware.jpg
   :width: 200 px
   :align: center

   EVAL-CN0552-PMDZ

.. figure:: cn0552_block_diagram.png
   :width: 600 px
   :align: center

   CN0552 Block Diagram

The CN0552 has two capacitive inputs with each channel that can be configured
as single-ended or differential. The capacitance input range is plus/minus
4.096 pF at a maximum bulk capacitance of 17 pF but is capable of extending up
to plus/minus 50 pF with a maximum bulk capacitance of 200 pF which can be
balanced by a programmable on-chip, digital-to-capacitance converter (CAPDAC).

The output data rate is adjustable from 9.1 sps to 90.9 sps, with the 16.1 sps
setting providing strong rejection of both 50 Hz and 60 Hz power line noise.
The CDC also provides temperature measurement with a resolution of 0.1 degrees C
and accuracy of plus/minus 2 degrees C for temperature compensation and system
calibration.

The CN0552 is compatible with I2C PMOD platform boards, with an I/O voltage
from 2.7 V to 5.5 V.

.. figure:: i2c_con.png
   :width: 300 px
   :align: center

   I2C Connection

Features
~~~~~~~~

- Interfaces to single or differential floating sensors
- Resolution down to 4 aF (up to 21 ENOB)
- Accuracy: 4 fF
- Linearity: 0.01%
- Common mode (not changing) capacitance up to 17 pF
- Full-scale (changing) capacitance range: plus/minus 4 pF
- Tolerant of parasitic capacitance to ground up to 60 pF
- Update rate: 10 Hz to 90 Hz
- Simultaneous 50 Hz and 60 Hz rejection at 16 Hz

Connectors and Configuration
-----------------------------

By default, the EVAL-CN0552-PMDZ is configured to be controlled and powered
from the PMOD connector using standard connections.

CN0552 Inputs/Outputs Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All the analog and digital input/output pins available on the EVAL-CN0552-PMDZ
are brought out to two separate 8-row 0.1" through-hole connectors P8 and P13.

.. figure:: eval-cn0552-pmdztop-edited.png
   :width: 650 px
   :align: center

   EVAL-CN0552-PMDZ Board Layout with Connector Locations

.. list-table:: Connector P8
   :header-rows: 1

   * - Description
     - Pin(s)
   * - EXCA
     - 1
   * - EXCB
     - 2
   * - EXC_EXTENDED
     - 3
   * - REFIN_POS
     - 4
   * - REFIN_NEG
     - 5
   * - GND
     - 6
   * - CIN1_NEG
     - 7
   * - CIN1_POS
     - 8

.. list-table:: Connector P13
   :header-rows: 1

   * - Description
     - Pin(s)
   * - GND
     - 1
   * - VDD
     - 2
   * - GND
     - 3
   * - VIN_NEG
     - 4
   * - VIN_POS
     - 5
   * - GND
     - 6
   * - CIN2_NEG
     - 7
   * - CIN2_POS
     - 8

Digital Communications
~~~~~~~~~~~~~~~~~~~~~~

The digital communication on the EVAL-CN0552-PMDZ is accomplished using a
standard I2C PMOD port.

.. list-table:: Connector P2
   :header-rows: 1

   * - Description
     - Pin(s)
   * - INT
     - 6
   * - RST
     - 5
   * - SCL
     - 4
   * - SDA
     - 3
   * - GND
     - 2
   * - IOVDD
     - 1

Solder Jumpers
~~~~~~~~~~~~~~

Eight solder jumpers are available at the bottom of the board to change the
operating modes. See the schematic for more details.

.. figure:: eval-cn0552-pmdztop-web.png
   :width: 500 px
   :align: center

   EVAL-CN0552-PMDZ Solder Jumper Locations

.. list-table::
   :header-rows: 1
   :widths: 60 15 25

   * - Description and Default Connection
     - Solder Jumper
     - Default Position
   * - ADC SDA connection (pull-up SDA to VDD)
     - P1
     - Shorted
   * - ADC SCL connection (pull-up SCL to VDD)
     - P7
     - Shorted
   * - Extended Excitation Enable (connect A1 OUT to P8 pin 3)
     - P14
     - Shorted
   * - ADC REFIN(-) connection (connect GND and P8 pin 5)
     - P3
     - Open
   * - ADC REFIN(+) connection (connect GND and P8 pin 4)
     - P9
     - Open
   * - ADC CIN1(-) connection (connect GND to P8 pin 7)
     - P4
     - Open
   * - ADC CIN1(+) connection (connect GND to P8 pin 8)
     - P10
     - Open
   * - ADC CIN2(-) connection (connect GND to P13 pin 7)
     - P5
     - Open
   * - ADC CIN2(+) connection (connect GND to P13 pin 8)
     - P11
     - Open
   * - ADC VIN(-) connection (connect GND to P13 pin 4)
     - P6
     - Open
   * - ADC VIN(+) connection (connect GND to P13 pin 5)
     - P12
     - Open

Test Points
~~~~~~~~~~~

Four test points are available to probe the I2C interface.

Device Driver Support
---------------------

There are two device driver solutions provided for controlling the
EVAL-CN0552-PMDZ:

#. **EVAL-ADICUP3029** -- The ADICUP3029 example application uses the AD7746
   no-OS driver and emulates the Linux IIO framework through the tinyiiod
   daemon library. The application communicates with the host computer via the
   serial backend, over a USB-UART physical connection. This facilitates rapid
   application development on a host computer, independent from embedded code
   development.

#. **Raspberry Pi** -- The Linux driver uses the Industrial Input/Output (IIO)
   framework, greatly simplifying the development of application code via the
   cross-platform libiio library, which is written in C and includes bindings
   for Python, MATLAB, C#, and other languages. Application code can run
   directly on the platform board, communicating with the device over the local
   backend, or from a remote host over the network or USB backends.

Utility software such as ``iio_info``, IIO Oscilloscope, and PyADI-IIO can be
used with the EVAL-CN0552-PMDZ on both the Raspberry Pi and ADICUP3029
platforms.

Demo with EVAL-ADICUP3029
--------------------------

The EVAL-CN0552-PMDZ can be used with the :adi:`EVAL-ADICUP3029`.

Demo Requirements
~~~~~~~~~~~~~~~~~

**Hardware**

- :adi:`EVAL-ADICUP3029`
- :adi:`EVAL-CN0552-PMDZ <CN0552>`
- Two 2 pF ceramic capacitors
- Micro-USB to USB cable
- PC or laptop with a USB port

**Software**

There are two ways to program the ADICUP3029 with the CN0552 software:

#. **Drag and drop** the prebuilt hex file to the DAPLINK drive -- this is the
   easiest way to get started with the reference design:
   `ADuCM3029_demo_cn0552.hex
   <https://github.com/analogdevicesinc/no-OS/releases/download/last_commit/cn0552.zip>`__

#. **Build from source** using the no-OS build system. Import and compile the
   project following the instructions in the
   `no-OS wiki <https://github.com/analogdevicesinc/no-OS/wiki>`__:
   `CN0552 source code
   <https://github.com/analogdevicesinc/no-OS/tree/main/projects/cn0552>`__

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: pmod-toadicup.png
   :width: 900 px
   :align: center

   EVAL-CN0552-PMDZ Connected to EVAL-ADICUP3029

#. Connect the EVAL-CN0552-PMDZ board at connector P9 of the EVAL-ADICUP3029.
#. Connect a micro-USB cable to the P10 connector of the EVAL-ADICUP3029 and
   connect it to a computer.
#. Ensure the on-board switches of the EVAL-ADICUP3029 are configured as shown
   below.

   .. figure:: switch_config.png
      :width: 900 px
      :align: center

      EVAL-ADICUP3029 Switch Configuration

#. Open My Computer and look for the DAPLINK drive. If the drive appears, the
   drivers are installed correctly.

   .. figure:: daplink.jpg
      :width: 300 px
      :align: center

      DAPLINK Drive Detection

#. Extract the provided zip file and drag and drop the hex file to the DAPLINK
   drive. The DS2 (red) LED will blink rapidly during programming and will stay
   ON once programming is complete.
#. For demo purposes, place a 2 pF capacitor between the EXCA pin and the
   CIN1(+) pin on the PMOD board. This will be the first channel. Then, place
   another 2 pF capacitor between the EXCB pin and the CIN2(+) pin on the
   PMOD board. This will be the second channel.

Demo with Raspberry Pi
-----------------------

The EVAL-CN0552-PMDZ can also be used with a Raspberry Pi.

Demo Requirements
~~~~~~~~~~~~~~~~~

**Hardware**

- :adi:`EVAL-CN0552-PMDZ <CN0552>`
- PMOD to Raspberry Pi Adapter (:adi:`PMD-RPI-INTZ`)
- Raspberry Pi Zero, Zero W, 3B+, or 4
- 16 GB (or larger) Class 10 (or faster) micro-SD card
- 5 Vdc, 2.5 A power supply with micro-USB connector (USB-C power supply for
  Raspberry Pi 4)
- User interface setup (choose one):

  - HDMI monitor, keyboard, mouse plugged directly into the Raspberry Pi
  - Host Windows/Linux/Mac computer on the same network as the Raspberry Pi

**Software**

- ADI Kuiper Linux

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~

In order to control the EVAL-CN0552-PMDZ from the Raspberry Pi, ADI Kuiper
Linux must be installed on an SD card. Complete instructions, including where to
download the SD card image, how to write it to the SD card, and how to
configure the system are provided at :dokuwiki:`Kuiper Linux
</resources/tools-software/linux-software/kuiper-linux>`.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

Follow the Hardware Configuration procedure under Preparing the Image:
Raspberry Pi in the Kuiper Linux documentation, substituting the following
line in ``config.txt``:

.. code-block:: bash

   dtoverlay=rpi-cn0552

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: interposer.png
   :width: 500 px
   :align: center

   PMOD to Raspberry Pi Interposer Board

.. figure:: pmod-interposer.png
   :width: 300 px
   :align: center

   EVAL-CN0552-PMDZ Mounted on Interposer Board

#. Connect the P9 of the PMOD to Raspberry Pi Interposer board at the male
   header GPIO pin connector of the Raspberry Pi.
#. Connect the EVAL-CN0552-PMDZ on the PMOD to Raspberry Pi Interposer board
   via Port P3 or P4.
#. Burn the SD card with the proper ADI Kuiper Linux image. Insert the burned
   SD card on the designated slot on the Raspberry Pi.
#. Connect the system to a monitor using an HDMI cable through the mini HDMI
   connector on the Raspberry Pi.
#. Connect a USB keyboard and mouse to the Raspberry Pi through the USB ports.
#. Power on the Raspberry Pi board by plugging in a 5 V power supply with a
   micro-USB connector.

.. figure:: overall_setup.png
   :width: 600 px
   :align: center

   Complete Raspberry Pi System Setup

Software
--------

The following software tools apply to both the ADICUP3029 and Raspberry Pi
platforms.

Connection
~~~~~~~~~~

To connect to the device, the software must create a context. The context
creation depends on the backend used to connect to the device as well as the
platform where the EVAL-CN0552-PMDZ is attached.

The libiio library is used for interfacing with IIO devices. Install the
`libiio package <https://github.com/analogdevicesinc/libiio/releases>`__ on
your machine. The ``iio_info`` command is a part of the libiio package that
reports all IIO attributes.

**Raspberry Pi direct local access:**

.. code-block:: bash

   iio_info

**Windows machine connected to Raspberry Pi:**

.. code-block:: bash

   iio_info -u ip:<ip address of your Raspberry Pi>

For example, if your Raspberry Pi has the IP address 192.168.1.7, use:

.. code-block:: bash

   iio_info -u ip:192.168.1.7

The Windows machine and the Raspberry Pi board must be connected to the same
network for the machine to detect the device.

**Windows machine connected to ADICUP3029:**

.. code-block:: bash

   iio_info -u serial:<serial port>

For example:

- On Windows, check the port of the ADICUP3029 via Device Manager in the
  Ports (COM & LPT) section. If the device is on COM4, use
  ``iio_info -u serial:COM4``.
- On Unix-based systems, the device appears under ``/dev/`` as ``ttyUSBn``
  (where n is a number). If the device is ``ttyUSB0``, use
  ``iio_info -u serial:/dev/ttyUSB0``.

IIO Commands
~~~~~~~~~~~~

The ``iio_attr`` command reads and writes IIO attributes:

.. code-block:: bash

   iio_attr [OPTION]...

For example, to look at the context attributes:

.. code-block:: bash

   iio_attr -a -C

The ``iio_reg`` command reads or writes SPI or I2C registers in an IIO device.
This is generally not needed for end applications, but can be useful for
debugging drivers. A context must be specified using the ``-u`` qualifier when
not directly accessing the device via the Raspberry Pi or when using the
ADICUP3029 platform:

.. code-block:: bash

   iio_reg -u <context> <device> <register> [<value>]

For example, to read the device ID (register 0x02) of an AD7746 interfaced via
the Raspberry Pi from a Windows machine:

.. code-block:: bash

   iio_reg -u ip:<ip address> ad7746 0x02

IIO Oscilloscope
~~~~~~~~~~~~~~~~

Download or update to the latest version of
`IIO Oscilloscope <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`__.

#. Open the IIO Oscilloscope application and supply the URI for context
   creation (see the Connection section above).
#. Press **Refresh** to display available IIO devices.
#. Once ``ad7746`` appears, press **Connect**.

.. figure:: osc.png
   :width: 200 px
   :align: center

   IIO Oscilloscope AD7746 Configuration

**Debug Panel** -- The Debug panel of AD7746 provides direct access to the
device attributes.

.. figure:: debug_panel.png
   :width: 400 px
   :align: center

   AD7746 Debug Panel

**DMM Panel** -- The DMM panel displays instantaneous readings of the input
capacitances and the device temperature.

.. figure:: dmm_readings.png
   :width: 400 px
   :align: center

   AD7746 DMM Panel Readings

PyADI-IIO
~~~~~~~~~~

PyADI-IIO is a Python abstraction module for ADI hardware with IIO drivers to
make them easier to use. This module provides device-specific APIs built on
top of the current libiio Python bindings. These interfaces try to match the
driver naming as much as possible without the need to understand the
complexities of libiio and IIO.

Follow the step-by-step procedure for how to install, configure, and set up
PyADI-IIO by referring to the :dokuwiki:`PyADI-IIO documentation
</resources/tools-software/linux-software/pyadi-iio>`.

Running the Example
^^^^^^^^^^^^^^^^^^^

After installing and configuring PyADI-IIO, run the ``ad7746.py`` script found
in the examples folder:

.. code-block:: bash

   python examples/ad7746.py

This will print capacitance and temperature readings to the console.

.. figure:: python_script.png
   :width: 500 px
   :align: center

   PyADI-IIO AD7746 Example Output

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `CN0552 Design & Integration Files
   <https://www.analog.com/cn0552-DesignSupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information and Useful Links
----------------------------------------

- :adi:`AD7746 Product Page <AD7746>`
- :adi:`CN0552 Circuit Note <CN0552>`
- `AN-1585 Application Note
  <https://www.analog.com/media/en/technical-documentation/application-notes/AN-1585.pdf>`__

Reference Demos & Software
----------------------------

- `CN0552 No-OS Source Code
  <https://github.com/analogdevicesinc/no-OS/tree/main/projects/cn0552>`__
- `CN0552 No-OS Build Instructions
  <https://github.com/analogdevicesinc/no-OS/wiki>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`EngineerZone <ez/reference-designs>`.
