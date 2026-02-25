.. _eval-cn0326-sdpz software:

ADICUP360/ADICUP3029 pH Monitor Demo
======================================

The EVAL-CN0326-PMDZ can also be used with the EVAL-ADICUP360 and
EVAL-ADICUP3029 development platforms to create a standalone pH monitor with
automatic temperature compensation.

Overview
--------

The **ADuCM360_demo_cn0326** (for ADICUP360) and **ADuCM3029_demo_cn0326**
(for ADICUP3029) are pH monitor demo projects with automatic temperature
compensation. The ADICUP360 project uses the GNU ARM Eclipse Plug-ins in
Eclipse environment, while the ADICUP3029 project uses CrossCore Embedded Studio
with the GNU ARM compiler.

These projects demonstrate how to use the EVAL-ADICUP360 or EVAL-ADICUP3029
base boards in different combinations with PMOD boards, expanding the list of
possible applications.

.. figure:: cn0326_hw_connected.jpg

   EVAL-ADICUP360 board with EVAL-CN0326-PMDZ connected

The CN0326 circuit provides a complete solution for pH sensors with internal
resistance between 1 MOhm and several GOhm. It consists of a pH probe buffer,
Pt1000 RTD for temperature compensation, and 24-bit ADC with 3 differential
analog inputs.

Theory of Operation
~~~~~~~~~~~~~~~~~~~~

The pH probe consists of a glass measuring electrode and a reference electrode,
which is analogous to a battery. When the probe is placed in a solution, the
measuring electrode generates a voltage depending on the hydrogen activity of
the solution, which is compared to the potential of the reference electrode.

- As the solution becomes more **acidic** (pH < 7), the potential of the glass
  electrode becomes more positive (+mV).
- As the solution becomes more **alkaline** (pH > 7), the potential of the
  glass electrode becomes more negative (-mV).

Temperature affects the hydrogen ion activity: heating increases the potential
difference, while cooling decreases it. Electrodes are designed to produce 0 V
when placed in a buffer solution with a pH of 7 (neutral pH).

ADC Code Formula
~~~~~~~~~~~~~~~~~

The project uses the following formula to determine the output ADC code for an
input voltage on either channel:

.. figure:: cn0326_demo_2_1.png

   ADC code formula

Where:

- **AIN** -- analog input voltage
- **GAIN** -- gain value in the in-amp setting
- **N** -- ADC resolution (24)

Temperature Calculation
~~~~~~~~~~~~~~~~~~~~~~~~

The temperature value is calculated using RTD resistance value, which varies
from 0 deg C (1000 Ohm) to 100 deg C (1385 Ohm):

.. figure:: cn0326_demo_2_2.png

   Temperature calculation formula

Where:

- **Rrtd** -- RTD resistance at T deg C
- **Rmin** -- RTD resistance at 0 deg C
- **alpha** -- temperature coefficient (0.00385 Ohm/Ohm/deg C)

pH Calculation (Nernst Equation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To calculate pH value, the Nernst equation is used:

.. figure:: cn0326_demo_2_3.png

   Nernst equation for pH calculation

Where:

- **E** -- voltage of the hydrogen electrode with unknown activity
- **alpha** -- zero point tolerance (+/-30 mV)
- **T** -- ambient temperature in deg C
- **n** -- valence, number of charges on ion (1 at 25 deg C)
- **F** -- Faraday constant (96485 coulombs/mol)
- **R** -- Avogadro's number (8314 mV-coulombs/deg K mol)
- **pHiso** -- reference hydrogen ion concentration (7)

EVAL-ADICUP360 Demo
---------------------

Demo Requirements
~~~~~~~~~~~~~~~~~~

**Hardware:**

- EVAL-ADICUP360 base board
- EVAL-CN0326-PMDZ
- pH probe
- PT100 temperature probe
- Micro USB to USB cable
- PC or laptop with a USB port

**Software:**

- ADuCM360_demo_cn0326 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM36x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)
- Serial terminal program (such as PuTTY or Tera Term)

Setting Up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~~

#. Set the jumpers/switches on the EVAL-ADICUP360 board for programming mode.
#. Connect the **EVAL-CN0326-PMDZ** to the SPI PMOD connector **P4** of the
   **EVAL-ADICUP360** board.
#. Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB (P14).

Obtaining the Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways to program the ADICUP360 with the CN0326 software:

#. **Drag and Drop** -- Drag and drop the .bin file to the MBED drive. This is
   the easiest way to get started with the reference design.
#. **Build, Compile, and Debug using CCES** -- Import the project into
   CrossCore to change parameters and customize the software.

.. admonition:: Download

   Prebuilt CN0326 Bin File:

   - `ADuCM360_demo_cn0326.bin
     <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0326.bin>`__

   Complete CN0326 Source Files:

   - `ADuCM360_demo_cn0326 Source Code
     <https://github.com/analogdevicesinc/EVAL-ADICUP360/tree/master/projects/ADuCM360_demo_cn0326>`__

Configuring Software Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **ADC gain** -- ``AD7793_GAIN`` -- set gain value for :adi:`AD7793` converter
  (``AD7793.h``):

  .. code-block:: c

     #define AD7793_GAIN    AD7793_GAIN_1

- **Excitation current** -- ``USE_IOUT2`` -- select whether to use bias current
  from the AIN3 channel (YES) or use internal excitation current, 210 uA (NO)
  (``CN0326.h``):

  .. code-block:: c

     #define USE_IOUT2      NO

- **Zero point tolerance** -- ``TOLERANCE`` -- tolerance used in Nernst
  equation (``CN0326.h``):

  .. code-block:: c

     #define TOLERANCE      0

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~~~

The application uses a UART interface (9600 baud rate, 8-bit data length) as a
command line interpreter to send results to a terminal window.

To start the command line interpreter, press the ENTER key and type ``help`` to
see available commands.

.. note::

   The ``calibrate`` command performs an internal zero and full scale calibration
   of the selected channel(s).

Available commands:

- ``temperature`` -- Display temperature value
- ``ph`` -- Display pH value
- ``help`` -- Show available commands
- ``calibrate`` -- Calibrate selected channel(s)
- ``reset`` -- Reset ADC

.. figure:: cn0326_demo_5.png

   Serial terminal output example

EVAL-ADICUP3029 Demo
----------------------

The **ADuCM3029_demo_cn0326** project is the ADICUP3029 version of the pH
monitor demo. It uses the same EVAL-CN0326-PMDZ PMOD and provides identical
functionality to the ADICUP360 version.

Demo Requirements
~~~~~~~~~~~~~~~~~~

**Hardware:**

- EVAL-ADICUP3029 base board
- EVAL-CN0326-PMDZ
- pH probe
- PT100 temperature probe
- Micro USB to USB cable
- PC or laptop with a USB port

**Software:**

- ADuCM3029_demo_cn0326 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM302x DFP (3.2.0 or higher)
- Serial terminal program (such as PuTTY or Tera Term)

The serial terminal interface and available commands are the same as the
ADICUP360 version described above.

.. admonition:: Download

   `ADuCM3029_demo_cn0326 Source Code
   <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_cn0326>`__
