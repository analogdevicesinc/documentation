.. _eval-cn0398-ardz-software:

Software Demos
==============

The EVAL-CN0398-ARDZ shield is supported on both the EVAL-ADICUP360 and
EVAL-ADICUP3029 platforms.

.. contents::
   :local:
   :depth: 2

ADICUP360 Demo
--------------

The **ADuCM360_demo_cn0398** is a pH and moisture measurements demo project for
the EVAL-ADICUP360 base board with the EVAL-CN0398-ARDZ shield, created using
the GNU ARM Eclipse Plug-ins in Eclipse environment.

General Description
~~~~~~~~~~~~~~~~~~~

The ADuCM360_demo_cn0398 project uses the EVAL-CN0398-ARDZ shield which is a
single supply, low power, high precision complete solution for soil moisture and
pH measurements, including temperature compensation. The circuit is optimized
for capacitive soil moisture sensors that are insensitive to water salinity and
do not corrode over time.

The circuit is divided into three independent measurement front ends: pH, soil
moisture, and temperature. After signal conditioning, the three channels share
an :adi:`AD7124-8`, 24-bit sigma-delta ADC.

.. figure:: cn0398_adicup.png
   :align: center
   :width: 500

   EVAL-CN0398-ARDZ with EVAL-ADICUP360 setup

The board allows configuration of **Vin** supply voltage (**P10** connector)
for 5 V or 7 V to 12 V. The **P8** connector configures 3.3 V or 5 V supply
for the moisture sensor. The user can select one of three GPIOs for the ADC CS
pin using **P5** connector (default: 1-2 position).

For temperature compensation, a PT100 RTD sensor is used in 2-wire connection
(default), with 3-wire or 4-wire also available via the **P1** connector. The
VH400 sensor (**P2**) is used for moisture measurement and an Atlas Scientific
sensor (**J1**) for pH measurement.

The **DS1** LED is ON while pH value is being measured and calculated. The
**DS3** LED is ON while moisture value is being measured and calculated.

The ADuCM360_demo_cn0398 application processes ADC outputs for all 3 channels
(RTD, pH and moisture), calculates pH and moisture values using RTD temperature
as input. Data is sent using **UART** communication (115200 baud rate, 8-bit
data length). The 24-bit ADC data are received using the **SPI** interface.

Measurement Formulas
~~~~~~~~~~~~~~~~~~~~~

**Temperature** -- calculated based on RTD resistance:

.. code-block:: none

   Rrtd = ((CODE - 2^23) * Rref) / (GAIN * 2^23)

Where:

- ``CODE`` -- ADC output
- ``Rref`` -- Reference resistor (5 kohm)
- ``GAIN`` -- Gain for RTD channel (16)

**pH** -- can be calculated in two ways:

*Two-point calibration:*

.. code-block:: none

   pH = [m * (V - y2 + Voffset) + x2]
   m  = [(x2 - x1) / (y2 - y1)]

Where:

- ``y1``, ``y2`` -- measured voltage at calibration points for known pH
- ``x1``, ``x2`` -- known pH at calibration points
- ``V`` -- pH channel measured voltage
- ``Voffset`` -- Offset voltage

A default calibration package can be loaded by updating the
``default_calibration_ph`` array with known values before programming.

*Nernst equation:*

.. code-block:: none

   pH = PH_ISO - ((V - a) / (2.303 * AVOGADRO * (T + 273.1)))

Where:

- ``PH_ISO`` -- reference hydrogen ion concentration (7)
- ``V`` -- pH channel measured voltage
- ``a`` -- zero point tolerance (see ``ZERO_POINT_TOLERANCE`` parameter)
- ``AVOGADRO`` -- Avogadro's number (8.314)
- ``T`` -- RTD temperature

**Moisture** -- can be calculated in two ways:

*Piece-wise formulas (Vegetronix VH400):*

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Voltage Range
     - Equation
   * - 0 V -- 1.1 V
     - m = 10 * Vm - 1
   * - 1.1 V -- 1.3 V
     - m = 25 * Vm - 17.5
   * - 1.3 V -- 1.82 V
     - m = 48.08 * Vm - 47.5
   * - 1.82 V -- 2.2 V
     - m = 26.32 * Vm - 7.89

*Transfer function:*

.. code-block:: none

   m = -1.18467 + 21.5371*Vm - 110.996*Vm^2 + 397.025*Vm^3
       - 666.986*Vm^4 + 569.236*Vm^5 - 246.005*Vm^6
       + 49.4867*Vm^7 - 3.37077*Vm^8

ADICUP360 Demo Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware:

- EVAL-ADICUP360
- EVAL-CN0398-ARDZ
- pH probe with BNC connector
- Analog moisture sensor
- PT100 RTD probe
- 7 V to 12 V DC power supply
- Micro USB to USB cable
- PC or laptop with a USB port

Software:

- ADuCM360_demo_cn0398 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM36x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)
- Serial Terminal Program (such as PuTTY or Tera Term)

ADICUP360 Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~

#. To program the base board, set the jumpers/switches on the EVAL-ADICUP360 as
   required for programming mode.

   .. figure:: cn0398_adicup360_hw.jpg
      :align: center
      :width: 500

      EVAL-ADICUP360 jumper and switch settings for programming

#. Connect the **EVAL-CN0398-ARDZ** to the Arduino connectors **P2**, **P5**,
   **P6**, **P7**, **P8** of the **EVAL-ADICUP360** board.
#. Connect the pH sensor to the **J1** connector of the EVAL-CN0398-ARDZ.
#. Connect the RTD sensor to the **P1** connector of the EVAL-CN0398-ARDZ.
#. Connect the moisture sensor to the **P2** connector of the EVAL-CN0398-ARDZ.

.. important::

   It is extremely important to plug in an acceptable power supply to the barrel
   jack **P11** of the EVAL-ADICUP360 if you are using a moisture sensor that
   requires voltage excitation greater than 5 V on the EVAL-CN0398-ARDZ. Only
   moisture sensors using less than 3.3 V can run off the USB power option.

6. Set the jumpers on the EVAL-CN0398-ARDZ as required for your sensor
   configuration.
#. Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB (P14).

ADICUP360 Source Code
~~~~~~~~~~~~~~~~~~~~~~

There are two ways to program the ADICUP360 with the CN0398 software:

#. Dragging and dropping the ``.bin`` file to the MBED drive.
#. Building, compiling, and debugging using CCES.

.. admonition:: Download

   `ADuCM360_demo_cn0398.bin (prebuilt)
   <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0398.bin>`__

   `ADuCM360_demo_cn0398 Source Code
   <https://github.com/analogdevicesinc/EVAL-ADICUP360/tree/master/projects/ADuCM360_demo_cn0398>`__

ADICUP360 Software Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following parameters can be configured in **CN0398.h**:

- **ZERO_POINT_TOLERANCE** -- Used in Nernst equation, input voltage value in
  [V].
- **DISPLAY_REFRESH** -- How often to refresh output data, in [msec].
- **USE_MANUFACTURER_MOISTURE_EQ** -- Selects which moisture formula to use.
  Commented = transfer function; uncommented = manufacturer formulas.

ADICUP360 Serial Output
~~~~~~~~~~~~~~~~~~~~~~~~~

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

#. The software will ask if you want to perform a calibration, type **n** or
   **y**.
#. If **n** is selected, the software will ask whether to load the default
   configuration or use the Nernst equations.
#. The data output refreshes at the rate of the ``DISPLAY_REFRESH`` parameter.

.. figure:: cn0398_demo_output.png
   :align: center
   :width: 500

   Serial terminal output showing pH, moisture, and temperature data

ADICUP360 Project Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADuCM360_demo_cn0398 is a C++ project using the ADuCM36x C/C++ project
structure.

The project contains: system initialization (disabling watchdog, setting system
clock, enabling clock for peripherals), port configuration for ADC, SPI
read/write, AD7124 configuration and reading, UART via P0.6/P0.7, UART
read/write functions, calibration and result display.

.. figure:: cn0398_project_structure.png
   :align: center
   :width: 220

   Project file structure

In the **src** and **include** folders:

- **Communication.cpp/h** -- SPI and UART specific data
- **CN0398.cpp/h** -- Calculation logic for pH, moisture, and temperature
- **AD7124.c/h** -- ADC channel handling

pH calibration parameters are set at runtime. After initialization, the
terminal window displays information messages on how to perform calibration.

The **RTE** folder contains device and system related files:

- **Device Folder** -- Low level drivers for ADuCM360 microcontroller
- **system.rteconfig** -- Peripheral component selection, startup, and ARM CMSIS
  files

ADICUP3029 Wi-Fi Demo
---------------------

The **ADuCM3029_demo_cn0398** is a pH and moisture measurements demo project
for the EVAL-ADICUP3029 base board with the EVAL-CN0398-ARDZ shield and an
ESP8266 Wi-Fi module for cloud connectivity via MQTT.

General Description
~~~~~~~~~~~~~~~~~~~

This demo extends the CN0398 functionality with Wi-Fi connectivity using an
ESP8266 module. Sensor data is transmitted to the cloud by publishing to an
MQTT broker.

The measurement algorithms are the same as the ADICUP360 demo (temperature,
pH, and moisture calculations).

ADICUP3029 Demo Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware:

- EVAL-ADICUP3029
- EVAL-CN0398-ARDZ
- pH probe with BNC connector
- Analog moisture sensor
- PT100 RTD probe
- Micro USB to USB cable
- PC or laptop with a USB port
- ESP8266 Wi-Fi module

Software:

- ADuCM3029_demo_cn0398 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM302x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)
- MQTT broker (e.g., Mosquitto)

ADICUP3029 Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Set the **S2** switch on the board to position **3** (Wi-Fi).
#. Plug in the ESP8266 module to the **P1** connector.
#. The ESP8266 Enable Pin needs to be tied directly to 3.3 V or pulled high to
   the GPIO via a 10K ohm resistor. This requires a small fly wire from the
   3.3 V pin to the enable pin on Rev B or Rev C of the ADICUP3029.
#. Connect the **EVAL-CN0398-ARDZ** shield to the board.
#. Connect the pH sensor to the **J1** connector.
#. Connect the RTD sensor to the **P1** connector.
#. Connect the moisture sensor to the **P2** connector.
#. Set jumpers on the EVAL-CN0398-ARDZ: P8 SENSOR to 3.3 V, VIN SUPPLY to 5 V,
   P5 to 10 on DIG11.
#. Connect the board to the PC via Micro USB cable.

.. important::

   Plug in an acceptable power supply to the barrel jack **P2** of the
   EVAL-ADICUP3029 if using a moisture sensor that requires voltage excitation
   greater than 5 V.

ADICUP3029 Software Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In **ADuCM3029_demo_cn0398.h**, configure your Wi-Fi connection and MQTT
information:

.. code-block:: c

   /* SSID of the access point. */
   uint8_t aWifiSSID[] = "****";

   /* Password of the access point. */
   uint8_t aWifiPassword[] = "****";

   /* IP address of the broker to publish to. */
   uint8_t aMQTTBrokerIp[] = "****";

Using an MQTT Broker
~~~~~~~~~~~~~~~~~~~~~

The demo publishes sensor data to an MQTT broker. Mosquitto is recommended as
the broker software.

To install and configure Mosquitto:

#. Download and install `Mosquitto <https://mosquitto.org/download/>`__ for your
   platform.
#. Start the Mosquitto broker service.
#. Subscribe to the sensor data topic using the Mosquitto subscriber client to
   view the published data.

ADICUP3029 Source Code
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   `ADuCM3029_demo_cn0398 Source Code
   <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_cn0398>`__
