.. _eval-cn0337-pmdz-software:

Software Demo
=============

The **ADuCM360_demo_cn0337** is an RTD temperature measurement demo project for
the EVAL-ADICUP360 base board with the EVAL-CN0337-PMDZ PMOD, created using the
GNU ARM Eclipse Plug-ins in Eclipse environment.

General Description
-------------------

The ADuCM360_demo_cn0337 project uses the EVAL-CN0337-PMDZ PMOD which is a
completely isolated 12-bit, 300 kSPS RTD temperature measurement system (with
only three active devices) that processes the output of a Pt100 RTD and includes
an innovative circuit for lead-wire compensation using a standard 3-wire
connection.

.. figure:: cn0337_demo_overview.png
   :align: center
   :width: 500

   CN0337 demo system overview

The CN0337 circuit translates the RTD input resistance range (100 ohm to
212.05 ohm for a 0 C to 300 C temperature range) into voltage levels compatible
with the input range of the ADC (0 V to 2.5 V). The 12-bit ADC value is
received via the SPI interface of the EVAL-ADICUP360 board.

The EVAL-CN0337-PMDZ comes with evaluation software to help test and calibrate
the PMOD before using it with an RTD sensor.

.. figure:: cn0337_demo_formula.png
   :align: center
   :width: 500

   CN0337 measurement block diagram

The ADuCM360_demo_cn0337 application processes the ADC output value and performs
all necessary conversions to provide RTD measurement results. A UART interface
(9600 baud rate, 8-bit data length) sends results to a terminal window: RTD
temperature and resistance values, voltage calculation, and ADC code. If the
resistance and temperature values are out of range, an error message is
displayed indicating that settings need to be checked.

Output values are displayed when the ENTER key (CR) is pressed. The measurement
interval can be configured using the ``SCAN_TIME`` parameter.

RTD Resistance Calculation Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The project offers two methods to calculate RTD resistance:

**Method 1: Transfer Function**

Calculates RTD resistance based on voltage and circuit gain:

.. code-block:: none

   Rrtd = (Vout - Voffset) / Gain

**Method 2: Two-Point Calibration**

Uses ADC output values for two different measurements: first using
Rmin = 100 ohm (ADC1) precision resistor and second with Rmax = 212.05 ohm
(ADC2) resistor:

.. code-block:: none

   Rrtd = Rmin + [(Rmax - Rmin) / (ADC2 - ADC1)] * (ADCrtd - ADC1)

Piecewise Linear Approximation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because the transfer function of the RTD (resistance vs. temperature) is
nonlinear, software linearization is needed to eliminate the nonlinearity error
of the Pt100 sensor. This project uses the Piecewise Linear Approximation
method.

This method takes linear approximation further by conceptualizing multiple
linear segments strung together to better approximate the nonlinear RTD transfer
function. Generating this series of linear segments so that each segment's
endpoints meet those of neighboring segments results in a number of points
connected by straight lines.

These coefficients are calculated once to best match the RTD's nonlinear
transfer function and then stored permanently in a look-up table (see
``C_rtd[]`` table). From this table, the software performs simple linear
interpolation to determine temperature based on measured RTD resistance.

The look-up table can have as many coefficients as needed depending on the
desired accuracy. For this project, the RTD resistance range is separated into
100 linearization segments.

Demo Requirements
-----------------

Hardware
~~~~~~~~

- EVAL-ADICUP360
- EVAL-CN0337-PMDZ
- 3-Wire PT100 RTD
- Micro USB to USB cable
- PC or laptop with a USB port

Software
~~~~~~~~

- ADuCM360_demo_cn0337 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM36x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)
- Serial Terminal Program (such as PuTTY or Tera Term)

Setting up the Hardware
-----------------------

#. To program the base board, set the jumpers/switches on the EVAL-ADICUP360
   as required for programming mode.

   .. figure:: cn0337_demo_setup.png
      :align: center
      :width: 400

      EVAL-ADICUP360 jumper and switch settings for programming

#. Plug the EVAL-CN0337-PMDZ PMOD into the EVAL-ADICUP360 base board via the
   **PMOD_SPI** port (P4).
#. Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB (P14).

Obtaining the Source Code
-------------------------

There are two ways to program the ADICUP360 with the CN0337 software:

#. Dragging and dropping the ``.bin`` file to the MBED drive.
#. Building, compiling, and debugging using CCES.

The drag-and-drop method uses a prebuilt binary for testing and evaluation. This
is the easiest way to get started.

Importing the project into CrossCore allows you to change parameters and
customize the software, but requires the CrossCore toolchain.

.. admonition:: Download

   `ADuCM360_demo_cn0337.bin (prebuilt)
   <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0337.bin>`__

   `ADuCM360_demo_cn0337 Source Code
   <https://github.com/analogdevicesinc/EVAL-ADICUP360/tree/master/projects/ADuCM360_demo_cn0337>`__

Configuring the Software Parameters
------------------------------------

The following parameters can be configured:

- **SCAN_TIME** -- How often to refresh the output data (in milliseconds).
- **RTD calculation method** -- Transfer function or two-point calibration
  (selectable in code).
- **Linearization table** -- ``C_rtd[]`` look-up table with 100 segments for
  Pt100 linearization.

Serial Terminal Output
----------------------

#. Flash the program to the EVAL-ADICUP360.
#. Switch the USB cable from the Debug USB (P14) to the User USB (P13).
#. Configure the serial terminal with the following UART settings:

   .. code-block:: none

      Select COM Port
      Baud rate: 9600
      Data: 8 bit
      Parity: none
      Stop: 1 bit
      Flow Control: none

#. Press ENTER to display measurement results.

.. figure:: cn0337_demo_output.png
   :align: center
   :width: 500

   Serial terminal output showing RTD measurement data

Project Structure
-----------------

The ADuCM360_demo_cn0337 is a C project that uses the ADuCM36x C/C++ project
structure.

The project contains: system initialization (disabling watchdog, setting system
clock, enabling clock for peripherals), port configuration for ADC, SPI
read/write, AD7091R configuration and reading, UART read/write functions, and
calibration and calculation of RTD temperature.

In the **src** and **include** folders you will find the source and header files
related to the CN0337 software application:

- **Communication.c/h** -- SPI and UART specific data
- **CN0337.c/h** -- Calculation and RTD conversion logic
- **AD7091R.c/h** -- ADC channel handling

The **RTE** folder contains device and system related files:

- **Device Folder** -- Low level drivers for ADuCM360 microcontroller
- **system.rteconfig** -- Peripheral component selection, startup, and ARM CMSIS
  files
