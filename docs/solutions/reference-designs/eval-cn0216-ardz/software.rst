.. _eval-cn0216-ardz-software:

Software
========

Weigh Scale Measurement Demo (ADICUP360)
-----------------------------------------

The **ADuCM360_demo_cn0216** is a weigh scale measurement demo project for the
EVAL-ADICUP360 base board with the additional
:adi:`EVAL-CN0216-ARDZ <EVAL-CN0216-ARDZ>` shield, created using the CrossCore
Embedded Studios IDE.

General Description
~~~~~~~~~~~~~~~~~~~

This project demonstrates how to use the EVAL-ADICUP360 board in combination
with the EVAL-CN0216-ARDZ shield board, expanding the list of possible
applications for the base board.

The EVAL-CN0216-ARDZ shield is a precision weigh scale system using a 24-bit
sigma-delta converter and auto-zero amplifiers providing high gain for the
bridge sensor input.

.. figure:: cn0216_hw_stacked.jpg
   :align: center
   :width: 550

   EVAL-ADICUP360 with EVAL-CN0216-ARDZ Shield

The CN0216 circuit translates the resistance changes on the bridge into very
small voltages. The bridge is excited by a regulated 5 V and that determines
the full scale range of the bridge output. Those values are passed through very
low noise, auto-zero amplifiers to remove as many error sources as possible
before being gained up to levels that will be compatible with the ADC. The
24-bit ADC value is received via SPI interface of the EVAL-ADICUP360 board.

The **ADuCM360_demo_cn0216** application processes ADC output value and makes
all necessary conversions to provide the weight results. A UART interface
(9600 baud rate, 8-bit data length) is used to send the results to a terminal
window: ADC Data Register **codes**, ADC Input Voltage **volts**, and Sensor
Input Weight **grams** are the outputs provided.

Calibration Procedure
~~~~~~~~~~~~~~~~~~~~~

At the start of the project, a calibration of the upper and lower input range
of the weigh scale is taken to remove both offset and gain errors in the
circuit, providing the most accurate weigh scale measurements possible.

#. Open a serial terminal to your PC.
#. When the program starts, it will ask you to make the zero scale calibration.
   Press **<ENTER>** to begin the zero scale calibration (takes about
   5 seconds). Make sure there is NOTHING on the scale.
#. Once that calibration has taken place, the serial terminal will prompt you
   to add the calibration weight to the scale. Press **<ENTER>** to make the
   full scale calibration (again takes about 5 seconds).
#. Measurements are averaged over 100 samples and stored into memory as the
   upper and lower calibration coefficients.
#. Once calibration is complete, measurements of the output values (weights and
   conversion information) are displayed every time you press **<ENTER>**.
   Measurements should be between the lower and upper calibration limits.

Demo Requirements
~~~~~~~~~~~~~~~~~

Hardware:

- EVAL-ADICUP360
- EVAL-CN0216-ARDZ
- Precision weight set
- 4- or 6-wire Wheatstone bridge weigh scale
- Micro USB to USB cable
- PC or laptop with a USB port

Software:

- ADuCM360_demo_cn0216 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM36x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)
- Serial terminal program (e.g., PuTTY or Tera Term)

Setting Up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

#. Set the jumpers/switches on the EVAL-ADICUP360 as shown below. The important
   jumpers/switches are highlighted in red.

   .. figure:: cn0216_hw_config.png
      :align: center
      :width: 500

      EVAL-ADICUP360 Jumper Configuration for CN0216

#. Connect the EVAL-CN0216-ARDZ to the Arduino connectors **P2, P5, P6, P7,
   P8** of the EVAL-ADICUP360 board.
#. Connect your weigh scale to the EVAL-CN0216-ARDZ via the sensor connector.
   Pay attention to the pinout on the :ref:`hardware page <eval-cn0216-ardz-hardware>`.
#. Connect an acceptable 7 V to 12 V power supply into the **P11** barrel jack
   of the EVAL-ADICUP360.

   .. important::

      You must plug in an acceptable power supply to the barrel jack **P11**
      for the EVAL-CN0216-ARDZ. The boards will not work if you try only to
      power them from the DEBUG_USB or the USER_USB.

#. Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB (P14).

Obtaining the Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways to program the ADICUP360 with the software for CN0216:

#. **Drag and drop** the .bin file to the MBED drive (easiest method).
#. **Build, compile, and debug** using CrossCore Embedded Studios (CCES).

.. admonition:: Download

   Prebuilt CN0216 Bin File

   - `ADuCM360_demo_cn0216.bin
     <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0216.bin>`__

   Complete CN0216 Source Files

   - `ADuCM360_demo_cn0216 Source Code
     <https://github.com/analogdevicesinc/EVAL-ADICUP360/tree/master/projects/ADuCM360_demo_cn0216>`__

Configuring the Software Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the reference voltage in the ``AD7791.h`` file (in volts):

.. code-block:: c

   #define VREF       5         /* The board default value is 5V */

Configure the full scale calibration weight in the ``CN0216.h`` file
(in grams):

.. code-block:: c

   #define CAL_WEIGHT     1000

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

#. Flash the program to the EVAL-ADICUP360.
#. Switch the USB cable from the DEBUG USB (P14) to the USER USB (P13).
#. Configure the serial terminal program with the following settings:

.. code-block:: none

   Select COM Port
   Baud rate: 9600
   Data: 8 bit
   Parity: none
   Stop: 1 bit
   Flow Control: none

Project Structure
~~~~~~~~~~~~~~~~~

The **ADuCM360_demo_cn0216** project uses the ADuCM36x C/C++ project structure.

This project contains: system initialization (disabling watchdog, setting
system clock, enabling clock for peripherals), port configuration for SPI1,
UART via P0.6/P0.7, SPI and UART read/write functions, AD7791 control, and
weight conversions.

.. figure:: cn0216_project_window.png
   :align: center
   :width: 340

   CN0216 Project Window in CrossCore Embedded Studio

In the **src** and **include** folders you will find the source and header
files related to the CN0216 software application:

- ``Communication.c/h`` -- SPI and UART specific data
- ``AD7791.c/h`` -- ADC control data
- ``CN0216.c/h`` -- Calibration and measurements management

The **RTE** folder contains device and system related files:

- **Device Folder** -- Low level drivers for ADuCM360 microcontroller (do not
  edit these files).
- **system.rteconfig** -- Allows the user to select the peripheral components
  needed, along with the startup and ARM CMSIS files for the project.
