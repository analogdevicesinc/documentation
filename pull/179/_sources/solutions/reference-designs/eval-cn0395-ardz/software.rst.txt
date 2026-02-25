.. _eval-cn0395-ardz software:

Software
========

This page describes the demo software for the :ref:`eval-cn0395-ardz` VOC
detector system running on the EVAL-ADICUP360 platform.

General Description
-------------------

The **ADuCM360_demo_cn0395** is a volatile organic compounds (VOC) detector
demo project for the EVAL-ADICUP360 base board with the EVAL-CN0395-ARDZ
shield.

The shield comes with a Figaro TGS8100 MOX sensor. The TGS8100 sensor requires
two voltage inputs: heater voltage (VH) and circuit voltage (VC). The heater
voltage is applied to the integrated heater to maintain the sensing element at
a specific temperature optimal for sensing. The CN0395 circuit provides the
heater voltage using the :adi:`ADN8810 <ADN8810>` IDAC as a programmable
current source. The default full-scale current is 9.94 mA and the default RSN
resistor value is 41.2 Ohm.

The hardware allows two main modes of operation: **heater mode** and **sensor
resistance measurement mode**. In heater mode, the :adi:`AD7988-1 <AD7988-1>`
ADC receives the heater voltage (VH) as input. In sensor mode, the input is
the voltage from the sense circuit (VRS). The switching is done using the
:adi:`ADG884 <ADG884>` analog switch. The full-scale voltage measured by the
ADC is 4.096 V.

The hardware includes a gain select circuit with overlapping ranges for sensor
resistance measurement. The :adi:`ADG758 <ADG758>` 8-channel multiplexer is
used for this purpose.

The TGS8100 sensor has temperature and humidity dependency, so temperature
compensation is performed using the on-board Sensirion SHT-30 sensor
(I2C bus).

The application uses a UART interface (9600 baud rate, 8-bit data length) as a
command line interpreter to send results to a terminal window.

Demo Requirements
-----------------

Hardware
~~~~~~~~

- EVAL-ADICUP360
- EVAL-CN0395-ARDZ
- Micro USB to USB cable
- PC or laptop with a USB port

Software
~~~~~~~~

- ADuCM360_demo_cn0395 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM36x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)
- Serial terminal program (such as PuTTY or Tera Term)

Obtaining the Source Code
-------------------------

There are two ways to program the ADICUP360 with the CN0395 software:

1. **Drag and Drop** -- Drag and drop the .bin file to the MBED drive. This is
   the easiest way to get started.
2. **Build with CCES** -- Import the project into CrossCore Embedded Studio to
   build, compile, and debug. This allows parameter customization.

.. admonition:: Download

   Prebuilt CN0395 Bin File:

   - `ADuCM360_demo_cn0395.bin
     <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0395.bin>`__

   Complete CN0395 Source Files:

   - `ADuCM360_demo_cn0395 Source Code
     <https://github.com/analogdevicesinc/EVAL-ADICUP360/tree/master/projects/ADuCM360_demo_cn0395>`__

Configuring the Software Parameters
------------------------------------

There are no compile-time configurations needed for this demo example. All
parameters are set at runtime via the command line interface.

Serial Terminal Output
----------------------

1. Flash the program to the EVAL-ADICUP360.
2. Switch the USB cable from the DEBUG USB (P14) to the USER USB (P13).
3. Configure the serial terminal with the following UART settings:

.. code-block:: none

   Select COM Port
   Baud rate: 9600
   Data: 8 bit
   Parity: none
   Stop: 1 bit
   Flow Control: none

The application allows the user to select between two modes of operation:

- Heater mode (RH)
- Sensor Resistance mode (RS)

Heater Mode (RH)
-----------------

The user can choose from the following subroutines which determine the heater
current (IH):

.. figure:: rh_mode.jpg
   :align: center

   Heater mode subroutine selection in serial terminal

**voltage** -- Sets the heater voltage to a constant voltage VH (default
VH = 1.8 V). The relationship between heater resistance RH and heater current
IH or heater voltage VH is nonlinear. The software runs several iterations in
the background to get VH to the desired accuracy with a 0.5% max error.

**resistance** -- Sets the heater resistance to a constant resistance RH
(default RH = 225 Ohm). For a heater resistance RH, set
IH = (RH - 110 Ohm) / 14375. Note: The slope of the RH vs. IH curve is
115 Ohm / 8 mA = 14375 Ohm/A. The software runs several iterations in the
background to get RH to the desired accuracy with a 0.5% max error.

**temperature** -- Sets the heater temperature to a constant temperature TH
(default TH = 360 degrees C). This is done in three steps:

1. The desired heater resistance RH_T is computed from:

   .. code-block:: none

      RH_T = RH_A * [1 + ALPHA * (RH_0 / RH_A) * (T - T_A)]

   Where:

   - RH_A = heater ambient temperature resistance (measured at power up)
   - RH_0 = default heater resistance (110 Ohm at 20 degrees C)
   - T = desired heater temperature (user input)
   - T_A = ambient temperature (measured at power up)
   - ALPHA = constant 0.003074

2. The resulting RH is used to calculate IH and VH with the constant resistance
   routine.
3. The resulting VH is further adjusted by using the constant heater voltage
   routine.

**current** -- Simply sets the IDAC to the desired current.

After the routine completes, the application displays the measured values:

- **RH_A** -- Ambient heater resistance
- **VH** -- Heater voltage
- **IH** -- Heater current
- **RH** -- Heater resistance
- **T_A** -- Ambient temperature
- **HUM** -- Ambient humidity
- **PH** -- Heater power consumption
- **TH** -- Heater temperature
- **ADC data** -- Raw data read from ADC (hex)
- **Ro** -- Sensor resistance measured in clean air

.. figure:: constant_voltage.jpg
   :align: center

   Constant voltage heater mode output in serial terminal

At power up, the application starts in constant current mode and sets the
default current to 8 mA. It is assumed that the measurement circuit is placed
in clean air, so the sensor resistance in clean air (Ro) is measured and
stored. After each heater measurement mode change, it is assumed the board is
in clean air and the Ro value is updated, because Ro is a function of heater
temperature.

.. figure:: power_up.jpg
   :align: center

   Power-up default output showing constant current mode at 8 mA

Sensor Resistance Mode (RS)
----------------------------

In this mode, sensor measurement is performed. The application can switch to
this mode at any time by pressing the **ENTER** key. The AD7988-1 ADC receives
the voltage from the sense circuit (VRS). The switching is done using the
ADG884.

In the background, the application runs the gain-ranging algorithm and
determines RS and the gas concentration (C) measured in PPM (parts per
million).

.. figure:: rs_mode_new.png
   :align: center

   Sensor resistance mode output with RS and gas concentration readings

RS reading can also be initiated by typing ``operation RS``, which performs the
same function as pressing the ENTER key.

Factory Calibration
-------------------

The IDAC current from the ADN8810 is 1% accurate; therefore, a factory
calibration must be performed. The routine loads code 4095 into ADN8810 and
reads the ADC. Ideally this should yield
9.94 mA x 71.5 Ohm = 0.71 V, or code [0.71/4.096] x 65535 = 11360. The gain
correction factor k1 = 11360 / CODEFS. This calibration should only be done
once.

Procedure:

1. Type ``calibrate w``
2. Connect jumper P2 between P2-1 and P2-2 (connects IOUT to the precision
   71.5 Ohm resistor).
3. Press ``c`` key when ready.
4. Power off then power on.

.. figure:: calibrate_w.jpg
   :align: center

   Factory calibration write procedure in serial terminal

From this point on, K1 is stored in permanent memory and applied to all
currents. To read the gain correction factor from memory, type ``calibrate r``.

.. figure:: calibrate_read.jpg
   :align: center

   Reading the gain correction factor from memory

Available Commands
------------------

Type ``help`` to see the available commands:

.. figure:: help.jpg
   :align: center

   Help command showing available serial terminal commands

Project Structure
-----------------

The **ADuCM360_demo_cn0395** project uses the ADuCM36x C/C++ Project
structure.

.. figure:: proj_struct.jpg
   :align: center
   :width: 340

   ADuCM360_demo_cn0395 project structure in CrossCore Embedded Studio

The project contains:

- System initialization -- disabling watchdog, setting system clock, enabling
  clock for peripherals
- Port configuration for SPI1, UART via P0.6/P0.7, I2C via P2.0/P2.1
- SPI, UART, I2C read/write functions
- Flash read/write functions
- AD7988 control, ADN8810 control, SHT30 control
- VOC concentration computation

In the **src** and **include** folders:

- ``Communication.c/h`` -- SPI, UART, and I2C specific data
- ``AD7988.c/h`` -- ADC control
- ``ADN8810.c/h`` -- IDAC control
- ``SHT30.c/h`` -- Temperature/humidity sensor control
- ``Flash.c/h`` -- Helper functions for permanent memory read/write
- ``CN0395.c/h`` -- Commands, configurations, and computations for the VOC
  detector application

The **RTE** folder contains device and system related files:

- **Device Folder** -- Low-level drivers for ADuCM360 microcontroller
- **system.rteconfig** -- Peripheral component selection, startup, and ARM
  CMSIS files
