.. _eval-cn0552-ebz:

EVAL-CN0552-PMDZ
=================

Capacitance-to-Digital Converter.

Overview
--------

The :adi:`EVAL-CN0552-PMDZ <CN0552>` is a
`PMOD <https://reference.digilentinc.com/pmod/start>`__ form-factor evaluation
board for the :adi:`AD7746`, a high resolution, sigma-delta capacitance-to-digital
converter (CDC). The architecture features inherent high resolution (24-bit no
missing codes, up to 21-bit effective resolution), high linearity (±0.01%),
and high accuracy (±4 fF factory calibrated).

.. figure:: actual_hardware.jpg
   :width: 400px
   :align: center

   EVAL-CN0552-PMDZ

The :adi:`CN0552 Circuit Note <CN0552>` has two capacitive inputs with each
channel configurable as single-ended or differential. The capacitance input
range is ±4.096 pF at a maximum bulk capacitance of 17 pF but is capable of
extending up to ±50 pF with a maximum bulk capacitance of 200 pF which can be
balanced by a programmable on-chip, digital-to-capacitance converter (CAPDAC).

.. figure:: cn0552_block_diagram.png
   :width: 500px
   :align: center

   CN0552 Block Diagram

The output data rate is adjustable from 9.1 SPS to 90.9 SPS, with the 16.1 SPS
setting providing strong rejection of both 50 Hz and 60 Hz power line noise.
The CDC also provides temperature measurement with a resolution of 0.1 deg C
and accuracy of ±2 deg C for temperature compensation and system calibration.

The CN0552 is compatible with I2C PMOD platform boards, with an I/O voltage
from 2.7 V to 5.5 V.

.. figure:: i2c_con.png
   :width: 300px
   :align: center

   I2C Connection

Features
--------

- Interfaces to single or differential floating sensors
- Resolution down to 4 aF (up to 21 ENOB)
- Accuracy: 4 fF
- Linearity: 0.01%
- Common mode (not changing) capacitance up to 17 pF
- Full-scale (changing) capacitance range: ±4 pF
- Tolerant of parasitic capacitance to ground up to 60 pF
- Update rate: 10 Hz to 90 Hz
- Simultaneous 50 Hz and 60 Hz rejection at 16 Hz

Connectors and Configuration
-----------------------------

By default, the EVAL-CN0552-PMDZ is configured to be controlled and powered
from the PMOD connector using standard connections.

.. figure:: eval-cn0552-pmdztop-edited.png
   :width: 650px
   :align: center

   EVAL-CN0552-PMDZ Connector Layout

Input/Output Connections
^^^^^^^^^^^^^^^^^^^^^^^^

All the analog and digital input/output pins available on the EVAL-CN0552-PMDZ
are brought out to two separate 8-row 0.1" through-hole connectors P8 and P13.

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
^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^

Eight solder jumpers are available at the bottom of the board to change the
operating modes. See the schematic for more details.

.. figure:: eval-cn0552-pmdztop-web.png
   :width: 500px
   :align: center

   EVAL-CN0552-PMDZ Solder Jumpers

.. list-table:: Solder Jumper Configuration
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
^^^^^^^^^^^^

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

Similarly, utility software such as iio_info, IIO Oscilloscope, and PyADI-IIO
can be used for both the EVAL-CN0552-PMDZ on Raspberry Pi and on ADICUP3029.

General Setup Using ADICUP3029
-------------------------------

The EVAL-CN0552-PMDZ can be used with the EVAL-ADICUP3029.

Demo Requirements
^^^^^^^^^^^^^^^^^

**Hardware:**

- :adi:`EVAL-ADICUP3029 <EVAL-ADICUP3029>`
- :adi:`EVAL-CN0552-PMDZ <CN0552>`
- Two 2 pF ceramic capacitors
- Micro-USB to USB cable
- PC or laptop with USB port

**Software:**

There are two ways to program the ADICUP3029 with the software for the CN0552:

#. Dragging and dropping the .hex file to the DAPLINK drive
#. Building, compiling, and debugging using CCES

Using the drag and drop method, the software will be a version that Analog
Devices creates for testing and evaluation purposes. This is the easiest way to
get started with the reference design.

Importing the project into CrossCore allows you to change parameters and
customize the software to fit your needs, but will be more advanced and will
require you to download the CrossCore toolchain.

The software for the ADICUP3029_CN0552 demo can be found here:

- Prebuilt CN0552 Hex File:
  :git-no-OS:`ADuCM3029_demo_cn0552.hex <releases/download/last_commit/cn0552.zip>`
- Complete CN0552 Source Files:
  :git-no-OS:`ADuCM3029_demo_cn0552 Source Code <projects/cn0552>`

To build the project from the source, follow the instructions in the
`no-OS wiki <https://github.com/analogdevicesinc/no-OS/wiki>`__.

Setting up the Hardware
^^^^^^^^^^^^^^^^^^^^^^^

#. Connect the EVAL-CN0552-PMDZ board at connector **P9** of the
   EVAL-ADICUP3029.
#. Connect a micro-USB cable to the P10 connector of the EVAL-ADICUP3029
   and connect it to a computer. The final setup should look similar to the
   picture below.

   .. figure:: pmod-toadicup.png
      :width: 500px
      :align: center

      Hardware Setup (ADICUP3029)

#. Make sure the following switches are configured as shown in the table below.

   .. figure:: switch_config.png
      :width: 400px
      :align: center

      Switch Configuration

#. From your PC, open My Computer and look for the DAPLINK drive. If you see
   this then the drivers are complete and correct.

   .. figure:: daplink.jpg
      :width: 300px
      :align: center

      DAPLINK Drive

#. Simply extract the provided zip file. Once extracted, you will see the
   pre-built hex file for the CN0552 demo. Then drag and drop this hex file to
   the DAPLINK drive and your ADICUP3029 board will be programmed. The DS2
   (red) LED will blink rapidly.
#. The DS2 will stop blinking and will stay ON once the programming is done.
#. For demo purposes, place a 2 pF capacitor between the EXCA pin and the
   CIN1(+) pin on the PMOD board. This will be your first channel. Then, place
   another 2 pF capacitor between EXCB pin and the CIN2(+) pin on the PMOD
   board. This will be your second channel.

General Setup Using Raspberry Pi
---------------------------------

The EVAL-CN0552-PMDZ can be used with a Raspberry Pi.

Demo Requirements
^^^^^^^^^^^^^^^^^

**Hardware:**

- :adi:`EVAL-CN0552-PMDZ <CN0552>`
- :adi:`PMOD to Raspberry Pi Adapter (PMD-RPI-INTZ) <PMD-RPI-INTZ>`
- Raspberry Pi Zero, Zero W, 3B+, or 4
- 16 GB (or larger) Class 10 (or faster) micro-SD card
- 5 Vdc, 2.5 A power supply with micro USB connector (USB-C power supply for
  Raspberry Pi 4)
- User interface setup (choose one):

  - HDMI monitor, keyboard, mouse plugged directly into Raspberry Pi
  - Host Windows/Linux/Mac computer on the same network as Raspberry Pi

**Software:**

- ADI Kuiper Linux

Loading Image on SD Card
^^^^^^^^^^^^^^^^^^^^^^^^^

In order to control the EVAL-CN0552-PMDZ from the Raspberry Pi, you will need
to install ADI Kuiper Linux on an SD card. Complete instructions, including
where to download the SD card image, how to write it to the SD card, and how to
configure the system are provided in the Kuiper Linux documentation.

Write the image and follow the system configuration procedure.

Configuring the SD Card
^^^^^^^^^^^^^^^^^^^^^^^^

Follow the Hardware Configuration procedure under **Preparing the Image:
Raspberry Pi** in the Kuiper Linux documentation, substituting the following
line in ``config.txt``:

.. code-block:: bash

   dtoverlay=rpi-cn0552

Setting up the Hardware
^^^^^^^^^^^^^^^^^^^^^^^^

To set up the circuit for evaluation, consider the following steps:

#. Connect P9 of the **PMOD to Raspberry Pi Interposer** board at the male
   header GPIO pin connector of the Raspberry Pi as shown below.

   .. figure:: interposer.png
      :width: 500px
      :align: center

      PMOD to Raspberry Pi Interposer Connection

#. Connect the EVAL-CN0552-PMDZ on the PMOD to Raspberry Pi Interposer board
   either via Port P3 or P4.

   .. figure:: pmod-interposer.png
      :width: 500px
      :align: center

      EVAL-CN0552-PMDZ on Interposer Board

#. Burn the SD card with the proper ADI Kuiper Linux image. Insert the burned
   SD card on the designated slot on the Raspberry Pi.
#. Connect the system to a monitor using an HDMI cable through the mini HDMI
   connector on the Raspberry Pi.
#. Connect a USB keyboard and mouse to the Raspberry Pi through the USB ports.
#. Power on the Raspberry Pi board by plugging in a 5 V power supply with a
   micro-USB connector. The final setup should look similar to the picture
   below.

   .. figure:: overall_setup.png
      :width: 600px
      :align: center

      Overall Setup (Raspberry Pi)

Software (ADICUP3029 and Raspberry Pi)
---------------------------------------

Connection
^^^^^^^^^^

To connect your device, the software must create a context. The context
creation depends on the backend used and the platform where the
EVAL-CN0552-PMDZ is attached. Two platforms are currently supported: Raspberry
Pi using ADI Kuiper Linux and the ADICUP3029 running the no-OS AD7746 demo
project. The user needs to supply a URI which will be used in the context
creation.

The libiio library is used for interfacing with IIO devices. Install the
`libiio package <https://github.com/analogdevicesinc/libiio/releases>`__ on
your machine.

The ``iio_info`` command is part of the libiio package and reports all IIO
attributes. Upon installation, enter the command on the terminal to access it.

**For Raspberry Pi direct local access:**

.. code-block:: bash

   iio_info

**For Windows machine connected to Raspberry Pi:**

.. code-block:: bash

   iio_info -u ip:<ip address of your rpi>

**For Windows machine connected to ADICUP3029:**

.. code-block:: bash

   iio_info -u serial:<serial port>

.. note::

   - For Raspberry Pi: The Windows machine and the Raspberry Pi board should
     be connected to the same network.
   - For ADICUP3029 on Windows: Check the port via Device Manager in the
     Ports (COM & LPT) section (e.g., ``iio_info -u serial:COM4``).
   - For ADICUP3029 on Linux: Check the ``/dev/`` directory for the device
     (e.g., ``iio_info -u serial:/dev/ttyUSB0``).

IIO Commands
^^^^^^^^^^^^

The ``iio_attr`` command reads and writes IIO attributes:

.. code-block:: bash

   iio_attr [OPTION]...

To look at the context attributes:

.. code-block:: bash

   iio_attr -a -C

The ``iio_reg`` command reads or writes SPI or I2C registers in an IIO device.
This is generally not needed for end applications, but can be useful in
debugging drivers. Note that you need to specify a context using the ``-u``
qualifier when not directly accessing the device via Raspberry Pi or when using
the ADICUP3029 platform.

.. code-block:: bash

   iio_reg -u <context> <device> <register> [<value>]

To read the device ID (register 0x02) of an AD7746 interfaced via Raspberry Pi
from a Windows machine:

.. code-block:: bash

   iio_reg -u ip:<ip address> ad7746 0x02

IIO Oscilloscope
^^^^^^^^^^^^^^^^

Make sure to download/update to the latest version of
`IIO Oscilloscope <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`__.

#. Once done with the installation or update, open the application. Supply a
   URI for context creation (see the Connection section above).
#. Press refresh to display available IIO devices. Once ``ad7746`` appears,
   press connect.

   .. figure:: osc.png
      :width: 500px
      :align: center

      AD7746 IIO Oscilloscope Configuration

Debug Panel
~~~~~~~~~~~

Below is the Debug panel of AD7746 where you can directly access the attributes
of the device.

.. figure:: debug_panel.png
   :width: 400px
   :align: center

   AD7746 Debug Panel

DMM Panel
~~~~~~~~~

Access the DMM panel to see the instantaneous reading of the input capacitances
and the device temperature.

.. figure:: dmm_readings.png
   :width: 400px
   :align: center

   AD7746 DMM Panel

PyADI-IIO
^^^^^^^^^^

PyADI-IIO is a Python abstraction module for ADI hardware with IIO drivers to
make them easier to use. This module provides device-specific APIs built on top
of the current libiio Python bindings. These interfaces try to match the driver
naming as much as possible without the need to understand the complexities of
libiio and IIO.

Running the Example
~~~~~~~~~~~~~~~~~~~

After installing and configuring PyADI-IIO on your machine, you are ready to
run Python script examples. Run the ``ad7746.py`` found in the examples folder.

.. figure:: python_script.png
   :width: 500px
   :align: center

   PyADI-IIO Example Output

Schematic, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download

   `EVAL-CN0552-PMDZ Design & Integration Files
   <https://www.analog.com/cn0552-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Documents
---------

- :adi:`CN0552 Circuit Note <CN0552>`
- `AN-1585 Application Note
  <https://www.analog.com/media/en/technical-documentation/application-notes/AN-1585.pdf>`__

Reference Demos and Software
-----------------------------

- `CN0552 no-OS Build Instruction Guide <https://github.com/analogdevicesinc/no-OS/wiki>`__
- :git-no-OS:`CN0552 no-OS Device Drivers <projects/cn0552>`

Additional Information
-----------------------

- :adi:`AD7746 Product Page <AD7746>`

Help and Support
-----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
