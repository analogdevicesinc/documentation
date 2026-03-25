.. _eval-cn0338-ardz software:

Software
========

This page describes the demo software for the :ref:`eval-cn0338-ardz` CO2 gas
measurement system running on the EVAL-ADICUP360 platform.

General Description
-------------------

The **ADuCM360_demo_cn0338** is a CO2 gas measurement demo project for the
EVAL-ADICUP360 base board with the EVAL-CN0338-ARDZ shield.

The application performs ADC reads, processes them, and makes all necessary
calculations to provide gas concentration. It also provides an interactive
**command line interpreter** which offers the user the ability to customize the
CN0338 shield. The UART interface (1 start bit, 8-bit data length, no parity
bits, and 2 stop bits) is used to send and receive data to and from a terminal
window. The default UART baud rate is **115200**, but it can be changed at
runtime from the command line.

To start the application, press the **ENTER** key. A welcome message will
appear, after which you can type ``help`` to see the available commands.

The project offers two calibration techniques based on the **Beer-Lambert Law**.

.. note::

   When using the CN0338 shield for the first time, all environment variables
   are set to default and the CN0338 requires calibration.

You can check current values of system variables using the ``printsettings``
command and reset system variables to default values using ``resetTodefault``.

.. note::

   The UART baud rate can be reset to default value using a terminal command or
   by pressing the RESET button on the EVAL-ADICUP360 board.

To start CN0338 measurements, use the ``run`` command. This displays:

- **CO2 concentration**
- **Temperature**
- Low, high, and diff voltage values for **REF** (peak-to-peak output of the
  reference detector), **ACT** (peak-to-peak output of the active detector),
  and **FA** (fractional absorbance)

From the command line you can set the following parameters:

- ADC sample frequency
- Serial port baud rate
- Falling and rising edge time for NDIR signal
- NDIR light source frequency

.. note::

   To abort any running command, use the ``Ctrl + c`` key combination.

Calibration Procedure
---------------------

The CN0338 must be calibrated before first use to achieve best performance.
There are two calibration algorithms available. For details about these
algorithms, refer to the :adi:`CN0338 Circuit Note <CN0338>`.

Beer-Lambert Law Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Input the command: ``sbllcalibrate``
2. Inject low concentration or zero gas (nitrogen) into the chamber. Ensure the
   gas is filling the chamber completely.
3. Wait for gas to disperse evenly.
4. Input the low concentration gas's concentration in the terminal.
5. Inject high concentration CO2 into the chamber. Ensure the gas is filling
   the chamber completely.
6. Wait for gas to disperse evenly.
7. Input the high concentration gas's concentration in the terminal.
8. Wait for the system to complete the calibration.

Modified Beer-Lambert Law Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Input the command: ``mbllcalibrate``
2. Input the constant parameter **b**.
3. Input the constant parameter **c**.
4. Inject low concentration or zero gas (nitrogen) into the chamber. Ensure the
   gas is filling the chamber completely.
5. Wait for gas to disperse evenly.
6. Input the low concentration gas's concentration in the terminal.
7. Inject high concentration CO2 into the chamber. Ensure the gas is filling
   the chamber completely.
8. Wait for gas to disperse evenly.
9. Input the high concentration gas's concentration in the terminal.
10. Wait for the system to complete the calibration.

After the above calibration procedure, the CN0338 is ready to use.

Demo Requirements
-----------------

Hardware
~~~~~~~~

- EVAL-ADICUP360
- EVAL-CN0338-ARDZ
- 7 V to 12 V DC power supply
- Micro USB to USB cable
- PC or laptop with a USB port

Software
~~~~~~~~

- ADuCM360_demo_cn0338 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM36x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)
- Serial terminal program (such as PuTTY or Tera Term)

Obtaining the Source Code
-------------------------

There are two ways to program the ADICUP360 with the CN0338 software:

1. **Drag and Drop** -- Drag and drop the .bin file to the MBED drive. This is
   the easiest way to get started.
2. **Build with CCES** -- Import the project into CrossCore Embedded Studio to
   build, compile, and debug. This allows parameter customization.

.. admonition:: Download

   Prebuilt CN0338 Bin File:

   - `ADuCM360_demo_cn0338.bin
     <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0338.bin>`__

   Complete CN0338 Source Files:

   - `ADuCM360_demo_cn0338 Source Code
     <https://github.com/analogdevicesinc/EVAL-ADICUP360/tree/master/projects/ADuCM360_demo_cn0338>`__

Configuring the Software Parameters
------------------------------------

The thermopile output data processing algorithm can be selected in ``ADC.h``:

.. code-block:: c

   #define ALGORITHM_PEAK2PEAK

- If **ALGORITHM_AVERAGE** is defined, the system uses the average value of all
  ADC sample points in half IR chop period as the input.
- If **ALGORITHM_PEAK2PEAK** is defined, the system uses the maximum value of
  all ADC sample points in IR high period and the minimum value of all ADC
  sample points in IR low period as the input.

Serial Terminal Output
----------------------

1. Flash the program to the EVAL-ADICUP360.
2. Switch the USB cable from the DEBUG USB (P14) to the USER USB (P13).
3. Configure the serial terminal with the following UART settings:

.. code-block:: none

   Select COM Port
   Baud rate: 115200
   Data: 8 bit
   Parity: none
   Start: 1 bit
   Stop: 2 bit
   Flow Control: none

4. Press **ENTER** to get the welcome message.
5. Type ``help`` to bring up the application menu.
6. Calibrate the application using one of the two calibration modes.
7. Type ``run`` to start measurements.

Project Structure
-----------------

The **ADuCM360_demo_cn0338** is a C++ project that uses the ADuCM36x C/C++
Project structure.

.. figure:: cn0338_demo_4.png
   :width: 310px

   CN0338 demo project structure.

The project contains:

- System initialization -- disabling watchdog, setting system clock, enabling
  clock for peripherals
- Port configuration for ADC, UART via P0.1/P0.2
- UART read/write functions
- Memory read/write functions
- NDIR calculations
- CO2 concentration and temperature conversions

In the **src** and **include** folders:

- ``Communication.cpp/h`` -- UART specific data
- ``CN0338.cpp/h`` -- Calculation part
- ``ADC.cpp/h`` -- ADC channels handling
- ``Flash.cpp/h`` -- Memory management
- ``Cmd.cpp/h``, ``Cmd_settings.cpp/h``, ``Cmd_calibrate.cpp/h`` -- Command
  line interpreter

The **RTE** folder contains device and system related files:

- **Device Folder** -- Low-level drivers for ADuCM360 microcontroller
- **system.rteconfig** -- Peripheral component selection, startup, and ARM
  CMSIS files
