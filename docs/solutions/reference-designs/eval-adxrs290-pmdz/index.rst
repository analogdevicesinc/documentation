.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz

.. _eval-adxrs290-pmdz:

EVAL-ADXRS290-PMDZ
===================

MEMS Dual-Axis Gyroscope PMOD.

.. toctree::
   :hidden:

   software

Overview
--------

.. figure:: eval-adxrs290-pmdz.png
   :align: center
   :width: 200px

   EVAL-ADXRS290-PMDZ Evaluation Board

The :adi:`EVAL-ADXRS290-PMDZ` is a simple PMOD form-factor evaluation board for
the :adi:`ADXRS290`, a high-performance MEMS pitch-and-roll (dual-axis in-plane)
angular rate sensor (gyroscope) designed for use in stabilization applications.

The solution senses and digitizes the **X-axis** and **Y-axis** (also called
**roll** and **pitch**) angular rates, producing a positive reading for
clockwise rotation about the x-axis and y-axis.

.. figure:: roll_and_pitch.png
   :align: center
   :width: 200px

   Roll and Pitch Axes

The ADXRS290 provides an output full-scale range of +/-100 deg/s with a
sensitivity of 200 LSB/(deg/s). Its resonating disk sensor structure enables
angular rate measurement about the axes normal to the sides of the package
around an in-plane axis. Angular rate data is formatted as a 16-bit two's
complement and is accessible through an SPI digital interface. The ADXRS290
exhibits a low noise floor of 0.004 deg/s/sqrt(Hz) and features programmable
high-pass and low-pass filters.

The ADXRS290 communicates via 4-wire SPI and operates as a peripheral (slave)
device, with a maximum clock frequency of 12 MHz.

.. figure:: spi_comm.png
   :align: center
   :width: 300px

   SPI Communication Interface

Features
--------

- Pitch and roll rate gyroscope
- Ultralow noise: 0.004 deg/s/sqrt(Hz)
- High vibration rejection over a wide frequency range
- Power saving standby mode
- 80 uA current consumption in standby mode
- Fast startup time from standby mode: <100 ms
- Low delay of <0.5 ms for a 30 Hz input at the widest bandwidth setting
- Serial peripheral interface (SPI) digital output
- Programmable high-pass and low-pass filters
- 2000 g powered acceleration survivability
- 2.7 V to 5.0 V operation
- -25 deg C to +85 deg C operation
- PMOD form factor

Hardware
--------

Digital Interface (PMOD)
~~~~~~~~~~~~~~~~~~~~~~~~

Digital communication on the EVAL-ADXRS290-PMDZ is accomplished using a
standard expanded SPI PMOD port.

.. list-table:: Connector P1 Pinout
   :header-rows: 1

   * - Description
     - Pin(s)
   * - SS
     - 1
   * - MOSI
     - 2
   * - MISO
     - 3
   * - SCLK
     - 4
   * - GND
     - 5, 11
   * - IOVDD
     - 6, 12
   * - SYNC
     - 7

Device Driver Support
---------------------

Two example device driver solutions are provided for controlling the
EVAL-ADXRS290-PMDZ PMOD using the no-OS device driver on the EVAL-ADICUP3029
platform and Linux device driver on the Raspberry Pi platform.

**EVAL-ADICUP3029:**

The ADICUP3029 example application uses the ADXRS290 no-OS driver and emulates
the Linux IIO framework through the tinyiiod daemon library. The application
communicates with the host computer via the serial backend, over a USB-UART
physical connection. This facilitates rapid application development on a host
computer, independent from embedded code development.

**Raspberry Pi:**

The Linux driver uses the Industrial Input/Output (IIO) framework, greatly
simplifying the development of application code via the cross-platform Libiio
library, which is written in C and includes bindings for Python, MATLAB, C#,
and other languages. Application code can run directly on the platform board,
communicating with the device over the local backend, or from a remote host
over the network or USB backends.

Similarly, utility software (iio_info, IIO Oscilloscope, PyADI-IIO, etc.) can
be used for both the EVAL-ADXRS290-PMDZ on Raspberry Pi and on ADICUP3029.

System Setup Using ADICUP3029
-----------------------------

The :adi:`EVAL-ADXRS290-PMDZ` can be used with the :adi:`EVAL-ADICUP3029`.

.. figure:: adxrs290_architecture.png
   :align: center
   :width: 400px

   ADXRS290 ADICUP3029 System Architecture

Demo Requirements
~~~~~~~~~~~~~~~~~

Hardware:

- :adi:`EVAL-ADICUP3029`
- :adi:`EVAL-ADXRS290-PMDZ`
- Micro-USB to USB cable
- PC or laptop with USB port

Software:

- `Prebuilt ADXRS290 IIO Hex File <https://github.com/analogdevicesinc/no-OS/releases/download/Latest/adxrs290-pmdz.zip>`__
- `ADXRS290 tinyiiod project source for ADICUP3029 <https://github.com/analogdevicesinc/no-OS/tree/master/projects/adxrs290-pmdz>`__

There are two basic ways to program the ADICUP3029:

1. **Dragging and Dropping the .Hex to the DAPLINK drive** -- This is the
   easiest way to get started.
2. **Building, Compiling, and Debugging using CCES** -- Allows customization
   but requires downloading the CrossCore toolchain.

To build the project from source, follow the instructions in the
`no-OS wiki <https://github.com/analogdevicesinc/no-OS/wiki>`__.

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

1. Connect EVAL-ADXRS290-PMDZ board at connector **P8** of the EVAL-ADICUP3029.
2. Connect a micro-USB cable to the P10 connector of the EVAL-ADICUP3029 and
   connect it to a computer.

.. figure:: pmodtoadicup_v2.jpg
   :align: center
   :width: 900px

   EVAL-ADXRS290-PMDZ Connected to EVAL-ADICUP3029

Flashing the Firmware
~~~~~~~~~~~~~~~~~~~~~

.. figure:: adicup3029_settings.jpg
   :align: center
   :width: 600px

   EVAL-ADICUP3029 Switch Settings

1. Make sure the switches on the EVAL-ADICUP3029 are in the correct positions.
2. Connect the ADICUP3029 to the PC host via micro-USB cable.
3. From your PC, open My Computer and look for the DAPLINK drive.

   .. figure:: daplink_in_mycomputer.jpg
      :align: center
      :width: 200px

      DAPLINK Drive in My Computer

4. Extract the provided zip file. For this demo use the
   **adxrs290-pmdz_aducm3029_iio_uart.hex**. Drag and drop this Hex file to the
   DAPLINK drive. The DS2 (red) LED will blink rapidly.
5. The DS2 will stop blinking and will stay ON once the programming is done.

.. note::

   An alternative human-readable Command Line Interface (CLI) program is also
   available for the ADXRS290 Pmod on the EVAL-ADICUP3029. This CLI demo
   provides commands for reading gyroscope data, configuring filters, and
   controlling the device.

System Setup Using Raspberry Pi
-------------------------------

The :adi:`EVAL-ADXRS290-PMDZ` can be used with a Raspberry Pi.

Demo Requirements
~~~~~~~~~~~~~~~~~

Hardware:

- :adi:`EVAL-ADXRS290-PMDZ` Circuit Evaluation Board
- Raspberry Pi Zero, Zero W, 3B+, or 4
- 16 GB (or larger) Class 10 (or faster) micro-SD card
- 5 Vdc, 2.5 A power supply with micro-USB connector (USB-C for RPi 4)
- Electrical connection hardware (choose one):

  - 12x 15 cm socket-to-socket jumpers
  - `DesignSpark HAT to Pmod Adapter <https://reference.digilentinc.com/reference/add-ons/pmod-hat/start>`__

- User interface: HDMI monitor, keyboard, mouse, or host computer on same
  network

Software:

- ADI Kuiper Linux image

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~

In order to control the EVAL-ADXRS290-PMDZ from the Raspberry Pi, you will
need to install ADI Kuiper Linux on an SD card. Complete instructions, including
where to download the SD card image, how to write it to the SD card, and how to
configure the system are provided on the Kuiper Linux page. Write the image
and follow the system configuration procedure.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

Follow the Hardware Configuration procedure under **Preparing the Image:
Raspberry Pi** on the Kuiper Linux page, substituting the following line in
``config.txt``:

.. code-block:: none

   dtoverlay=rpi-adxrs290

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: rpi_pmod_con.jpg
   :align: center
   :width: 800px

   Raspberry Pi to PMOD Connection

.. important::

   The I/O pins of the Raspberry Pi board are only 3.3 V tolerant. Any
   peripheral to be attached should be powered by a source not exceeding 3.3 V.

1. Connect EVAL-ADXRS290-PMDZ board at the male header connector of the
   Raspberry Pi.
2. Burn the SD card with the proper ADI Kuiper Linux image. Insert the burned
   SD card on the designated slot on the RPi.
3. Connect the system to a monitor using an HDMI cable through the mini HDMI
   connector on the RPi.
4. Connect a USB keyboard and mouse to the RPi through the USB ports.
5. Power on the RPi board by plugging in a 5 V power supply with a micro-USB
   connector.

.. figure:: system_con.jpg
   :align: center
   :width: 600px

   Complete Raspberry Pi System Setup

Software and Demo
------------------

For detailed software setup instructions including IIO Oscilloscope, PyADI-IIO,
CLI demo, and IIO commands, see the :doc:`software` page.

Design Files
------------

- `EVAL-ADXRS290-PMDZ Design & Integration Files <https://www.analog.com/media/en/evaluation-documentation/evaluation-design-files/eval-adxrs290-pmdz-designsupport.zip>`__
  (Schematic, PCB Layout, Bill of Materials, Allegro Project)

Additional Information
----------------------

- :adi:`ADXRS290 Product Page <ADXRS290>`
- :adi:`EVAL-ADXRS290-PMDZ Product Page <EVAL-ADXRS290-PMDZ>`
- `ADXRS290 No-OS Build Instruction Guide <https://github.com/analogdevicesinc/no-OS/wiki>`__
- `ADXRS290 No-OS Drivers <https://github.com/analogdevicesinc/no-OS/tree/master/projects/adxrs290-pmdz>`__

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
