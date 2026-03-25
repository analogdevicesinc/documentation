.. _eval-cn0411-ardz-software:

Software Demo
=============

The **ADuCM360_demo_cn0411** is a Total Dissolved Solids (TDS) measurements
demo project for the EVAL-ADICUP360 base board with the EVAL-CN0411-ARDZ
shield, created using the GNU ARM Eclipse Plug-ins in Eclipse environment.

General Description
-------------------

The ADuCM360_demo_cn0411 project uses the EVAL-CN0411-ARDZ shield which is a
single supply, low power, high precision complete solution for Total Dissolved
Solids measurements, including temperature compensation. The circuit is
optimized for conductivity measurements used to determine TDS values, using
conductivity cells with BNC plug.

The circuit is divided into three independent measurement front ends: TDS,
conductivity and temperature. After signal conditioning, the three channels
share an :adi:`AD7124-8`, 24-bit sigma-delta ADC.

.. figure:: cn0411_demo_4.jpg
   :align: center
   :width: 500

   EVAL-CN0411-ARDZ with EVAL-ADICUP360 test setup

The ADuCM360_demo_cn0411 application processes ADC outputs for all 5 channels
(RTD, Vpeak+, Vpeak-, VDAC, VR20S, VR200S), calculates conductivity and TDS
values using RTD temperature and peak-to-peak voltage. Data is sent to serial
interface using UART communication (115200 baud rate, 8-bit data length). The
24-bit ADC data are received using the SPI interface of the EVAL-ADICUP360
board.

Measurement Formulas
~~~~~~~~~~~~~~~~~~~~

**Temperature** is calculated based on the RTD resistance:

.. code-block:: none

   Rrtd = (CODE * Rref) / (2^24 - 1)

Where:

- ``CODE`` -- ADC output
- ``Rref`` -- Reference resistor (4.02 kohm)

**Premeasurement Procedure** -- Before computing TDS, the system runs an
auto-ranging procedure to select the proper gain resistance. The multiplexer is
set to the highest gain resistance (20 Mohm) and the DAC output is set to a
user-defined value (initially 400 mV). The positive and negative input voltages
are captured via ADC channels 1 and 2. If the following condition is met:

.. code-block:: none

   Vp + Vn > 0.3 * 2 * Vexc

The excitation voltage is adjusted to:

.. code-block:: none

   Vexc = 0.4 * Vexc / (Vp + Vn)

Otherwise, the gain resistor is dropped by one decade and the process repeats.

**Peak-to-peak current** is computed as:

.. code-block:: none

   Ipp = (2 * Vexc - (Vp + Vn)) / Rgain

**Electrical conductance** is computed as:

.. code-block:: none

   g = Ipp / ((Vp + Vn) - (Ipp * Roff))

Where ``Roff`` is the offset resistance (obtained via the ``refres`` command).

**Electrical conductivity** (temperature compensated):

.. code-block:: none

   s = k * g
   s_cal = s / (1 + temp_coeff * (temp - t_cal))

Where ``k`` is the cell constant, ``temp_coeff`` is the solution temperature
coefficient, and ``t_cal`` is the reference temperature (25 C).

**Total dissolved solids**:

.. code-block:: none

   tds = k_e * s_cal

Where ``k_e`` is the TDS factor corresponding to the solution type.

Demo Requirements
-----------------

Hardware
~~~~~~~~

- EVAL-ADICUP360
- EVAL-CN0411-ARDZ
- Conductivity cell with BNC connector
- PT100/PT1000 RTD probe
- Micro USB to USB cable
- PC or laptop with a USB port

Software
~~~~~~~~

- ADuCM360_demo_cn0411 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM36x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)
- Serial Terminal Program (such as PuTTY or Tera Term)

Setting up the Hardware
-----------------------

#. To program the base board, set the jumpers and switches on the EVAL-ADICUP360
   as required for programming mode.
#. Connect the **EVAL-CN0411-ARDZ** shield to the Arduino connectors **P2**,
   **P5**, **P6**, **P7**, **P8** of the **EVAL-ADICUP360** board.
#. Connect the conductivity cell to the **J1** connector of the
   EVAL-CN0411-ARDZ.
#. Connect the RTD sensor to the **P3** connector of the EVAL-CN0411-ARDZ.
#. Connect **PIN1** and **PIN2** on **P5** connector and **PIN1** and **PIN2**
   on **P6** connector to read data from the conductivity cell.
#. Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB (P14).

Obtaining the Source Code
-------------------------

There are two ways to program the ADICUP360 with the CN0411 software:

#. Dragging and dropping the ``.bin`` file to the MBED drive.
#. Building, compiling, and debugging using CCES.

The drag-and-drop method uses a prebuilt binary for testing and evaluation. This
is the easiest way to get started.

Importing the project into CrossCore allows you to change parameters and
customize the software, but requires the CrossCore toolchain.

.. admonition:: Download

   `ADuCM360_demo_cn0411.bin (prebuilt)
   <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0411.bin>`__

   `ADuCM360_demo_cn0411 Source Code
   <https://github.com/analogdevicesinc/EVAL-ADICUP360/tree/master/projects/ADuCM360_demo_cn0411>`__

Configuring the Software Parameters
------------------------------------

The following parameters can be configured in **CN0411.h**:

- **DAC_OUT_DEFAULT_VAL** -- Default output voltage for the DAC:

  .. code-block:: c

     #define DAC_OUT_DEFAULT_VAL     0.4

- **TDS_KCL** -- TDS factor for KCl solution:

  .. code-block:: c

     #define TDS_KCL                 0.5

- **TDS_NACL** -- TDS factor for NaCl solution:

  .. code-block:: c

     #define TDS_NACL                0.47

- **TEMP_COEFF_KCL** -- Temperature coefficient for KCl solution:

  .. code-block:: c

     #define TEMP_COEFF_KCL          1.88

- **TEMP_COEFF_NACL** -- Temperature coefficient for NaCl solution:

  .. code-block:: c

     #define TEMP_COEFF_NACL         2.14

Serial Terminal Output
----------------------

#. Flash the program to the EVAL-ADICUP360.
#. Switch the USB cable from the Debug USB (P14) to the User USB (P13).
#. Configure the serial terminal with the following UART settings:

   .. code-block:: none

      Select COM Port
      Baud rate: 115200
      Data: 8 bit
      Parity: none
      Stop: 1 bit
      Flow Control: none

#. Press the **<ENTER>** key to start the program.
#. Type ``help`` into the serial terminal to display the command menu.

.. figure:: cn0411_demo_1.png
   :align: center
   :width: 400

   Serial terminal output showing measurement data

Available Commands
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Command
     - Description
   * - ``help``
     - Display available commands
   * - ``syscal``
     - Perform ADC system zero-scale calibration. Short terminals 5 & 6 in
       jumper P5 before calibration.
   * - ``refres``
     - Perform referencing to precision resistance. Short terminals 3 & 4 in
       jumper P5 before referencing.
   * - ``convmod (sing/cont)``
     - Set single/continuous conversion mode for ADC
   * - ``autoset``
     - Autoset gain resistance
   * - ``setdac <val>``
     - Set DAC value (Volts)
   * - ``gainres <val>``
     - Set gain resistor value (ohm). Values: 20, 200, 2K, 20K, 200K, 2M, 20M
   * - ``rtdval <val>``
     - Set RTD value (ohm). Values: 100, 1000
   * - ``pwmfreq <val>``
     - Set PWM frequency value (Hz). Values: 94, 2400
   * - ``cellconst (low/normal/high/<val>)``
     - Set cell constant for conductivity types
   * - ``solution (kcl/nacl/<val_tmp_coeff,val_tds_factor>)``
     - Set parameters for specific solution
   * - ``temp``
     - Display temperature value
   * - ``vinput (pos/neg)``
     - Display positive/negative input voltage
   * - ``readdac``
     - Read DAC value (Volts)
   * - ``rdr20s``
     - Read voltage on R20S (Volts)
   * - ``rdr200s``
     - Read voltage on R200S (Volts)
   * - ``rdres``
     - Read input resistance (Volts)
   * - ``cond``
     - Display conductivity value
   * - ``tds``
     - Display TDS value

Project Structure
-----------------

The ADuCM360_demo_cn0411 is a C++ project that uses the ADuCM36x C/C++ project
structure.

The project contains: system initialization (disabling watchdog, setting system
clock, enabling clock for peripherals), port configuration for ADC, SPI
read/write, AD7124 configuration and reading, UART via P0.6/P0.7, UART
read/write functions, calibration and result display.

In the **src** and **include** folders you will find the source and header files
related to the CN0411 software application:

- **Communication.c** -- SPI and UART specific data
- **CN0411.c** -- Calculation and measurement logic
- **AD7124.c** -- ADC channel handling

.. figure:: cn0411_demo_3.png
   :align: center
   :width: 240

   Project file structure

The **RTE** folder contains device and system related files:

- **Device Folder** -- Low level drivers for ADuCM360 microcontroller
- **system.rteconfig** -- Peripheral component selection, startup, and ARM CMSIS
  files
