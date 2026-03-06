.. imported from: https://wiki.analog.com/resources/tools-software/linux-software/cn0357_plugin

.. _eval-cn0357-ardz:

EVAL-CN0357-ARDZ
================

Single-Supply, Low Noise, Portable Gas Detector Using an Electrochemical
Sensor.

Overview
--------

:adi:`CN0357` is a single-supply, low noise, portable gas detector using an
electrochemical sensor. The Alphasense CO-AX Carbon Monoxide sensor is used
in this example. Electrochemical sensors offer several advantages for
instruments that detect or measure the concentration of many toxic gases.
Most sensors are gas specific and have usable resolutions under one part per
million (ppm) of gas concentration.

The circuit uses the :adi:`ADA4528-2` dual auto-zero amplifier, which has a
maximum offset voltage of 2.5 uV at room temperature and an industry-leading
5.6 uV/sqrt(Hz) of voltage noise density. In addition, the :adi:`AD5270`
programmable rheostat is used rather than a fixed transimpedance resistor,
allowing for rapid prototyping of different gas sensor systems without
changing the bill of materials.

The :adi:`ADR3412` precision, low noise, micropower reference establishes the
1.2 V common-mode, pseudo ground reference voltage with 0.1% accuracy and
8 ppm/degC drift. For applications where measuring fractions of ppm gas
concentration is important, using the :adi:`ADA4528-2` and the :adi:`ADR3412`
makes the circuit performance suitable for interfacing with a 16-bit ADC,
such as the :adi:`AD7790`.

.. figure:: cn0357-simplified_schematic.png
   :width: 800 px
   :align: center

   CN0357 Simplified Schematic

SDP-B Evaluation Setup
-----------------------

Required Equipment (SDP-B)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-SDP-CB1Z` Controller Board **(SDP-B Board)**
- :adi:`EVAL-CN0357-PMDZ` Evaluation Board **(CN0357 Board)**
- :adi:`SDP-PMD-IB1Z` Interposer Board **(SDP to Pmod Interposer Board)**
- :adi:`EVAL-CFTL-6V-PWRZ` **(+6 V Power Supply)** or equivalent
- CN0357 evaluation software
- PC with minimum requirements:

  - Windows XP Service Pack 2 (32-bit)
  - USB Type-A port
  - Processor rated at 1 GHz or faster
  - 512 MB RAM and 500 MB available hard disk space

- USB Type-A to USB Mini-B cable

General Setup (SDP-B)
~~~~~~~~~~~~~~~~~~~~~~

- The :adi:`EVAL-CN0357-PMDZ` **(CN0357 Board)** connects to the
  :adi:`SDP-PMD-IB1Z` **(SDP to Pmod Interposer Board)** via the 12-pin
  connector.
- The :adi:`SDP-PMD-IB1Z` **(SDP to Pmod Interposer Board)** connects to the
  :adi:`EVAL-SDP-CB1Z` **(SDP-B Board)** via the 120-pin connector.
- The :adi:`EVAL-CFTL-6V-PWRZ` **(+6 V DC Power Supply)** powers the
  SDP-PMD-IB1Z via the DC barrel jack.
- The :adi:`EVAL-SDP-CB1Z` **(SDP-B Board)** connects to the PC via the USB
  cable.

Connecting the Hardware (SDP-B)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the :adi:`EVAL-CN0357-PMDZ` **(CN0357 Board)** to the
   :adi:`SDP-PMD-IB1Z` **(SDP to Pmod Interposer Board)** and the
   :adi:`EVAL-SDP-CB1Z` **(SDP-B Board)** to the SDP-PMD-IB1Z as depicted
   below.

   .. figure:: cn0357-hardware1.jpg
      :width: 600 px
      :align: center

      Board Stack Assembly

#. Connect the :adi:`EVAL-CFTL-6V-PWRZ` **(+6 V DC Power Supply)** to the
   barrel jack at **J1** on the SDP-PMD-IB1Z.

   .. figure:: cn0357-hardware2.jpg
      :width: 600 px
      :align: center

      Power Supply Connection

#. Connect the USB cable to **J1** of the :adi:`EVAL-SDP-CB1Z` **(SDP-B
   Board)**.

   .. figure:: cn0357-hardware3.jpg
      :width: 600 px
      :align: center

      USB Cable Connection

Software Installation (SDP-B)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Extract **CN0357_Evaluation_Software.zip** and run **setup.exe**.

   .. note::

      It is recommended to install the CN0357 evaluation software to the
      default directory path ``C:\Program Files\Analog Devices\CN0357\`` and
      all National Instruments products to
      ``C:\Program Files\National Instruments\``.

#. Click **Next** to view the installation review page.
#. Click **Next** to start the installation.
#. Upon completion, the installer for the **ADI SDP Drivers** will execute.

   .. note::

      Close all other applications before clicking **Next** to allow updating
      relevant system files without rebooting.

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended to install the drivers to the default directory path
      ``C:\Program Files\Analog Devices\SDP\Drivers``.

#. Press **Next** to install the SDP Drivers and complete the installation.
   Click **Finish** when done.

Using the SDP-B Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software Controls and Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0357-software.png
   :width: 800 px
   :align: center

   CN0357 Evaluation Software -- Measure Concentration Tab

.. figure:: cn0357-software2.png
   :width: 800 px
   :align: center

   CN0357 Evaluation Software -- Configure System Tab

#. **Run Button** -- Starts collecting concentration data and presenting
   acquisitions in the chart.
#. **Stop Button** -- Stops data collection from the CN0357 Board.
#. **Save Data Button** -- Saves collected data to a tab-delimited ASCII
   spreadsheet file.
#. **Clear Data Button** -- Clears all collected data from the chart history.
#. **Control Tabs**:

   - *Measure Concentration* -- Data collection chart.
   - *Configure System* -- System configuration settings.
   - *SDP Board Information* -- SDP Board information.

#. **Concentration Numerical Indicator** -- Displays the current gas
   concentration measured by the system.
#. **Sensor Type Drop-down Menu**:

   - *Oxidation (sink)* -- Select if the sensor sinks current.
   - *Reduction (source)* -- Select if the sensor sources current.

#. **Max Sensor Sensitivity Numerical Control** -- Maximum current in nA the
   sensor sinks/sources per ppm. Influences the feedback resistance set by the
   rheostat (:adi:`AD5270`).
#. **Typical Sensor Sensitivity Drop-down Menu** -- Typical current in nA the
   sensor sinks/sources per ppm. Influences the LSB size in terms of ppm/mV
   and mV/ppm.
#. **Sensor Range Numerical Control** -- Maximum concentration the sensor can
   measure in ppm.
#. **Feedback Resistance Numerical Indicator** -- Feedback resistance of the
   transimpedance amplifier on the CN0357 Board (:adi:`ADA4528-2`). Can be set
   by the rheostat (:adi:`AD5270`) or a fixed resistor.
#. **ppm/mV Numerical Indicator** -- Parts per million concentration per
   millivolt.
#. **mV/ppm Numerical Indicator** -- Millivolts per parts per million
   concentration.
#. **ADC Conversion Numerical Indicator** -- Converted voltage seen by the ADC
   (:adi:`AD7790`).
#. **Chart Controls** -- Allow zooming in, zooming out, and panning through
   the collected data.
#. **System Status String Indicator** -- Displays a message detailing the
   current state of the software.
#. **System Status LED Indicator** -- Displays the current software state:

   - **Grey**: Inactive
   - **Yellow**: Busy
   - **Red**: Error

#. **Buffer Mode Radio Buttons**:

   - *Buffered Mode* -- Allows source impedance on the front end without
     contributing gain errors.
   - *Unbuffered Mode* -- Disables the buffers, lowering power consumption.

   .. note::

      Enabling the buffers also reduces the analog input range of the ADC.

#. **Mode Register Numerical Indicator** -- Used to configure the ADC for
   range, buffer mode, or power-down. See the AD7790 datasheet Table 9.
#. **Filter Register Numerical Indicator** -- Used to set the output word
   rate. See the AD7790 datasheet Table 12.

   .. note::

      The CN0357 evaluation software uses Single Conversion Mode.

#. **Reset ADC Button** -- Resets the serial interface by writing a series of
   1s on the DIN input, returning all registers to power-on values.
#. **Feedback Selector Radio Buttons**:

   - *Rheostat* -- Uses the rheostat for TIA feedback resistance.
   - *Fixed Resistor* -- Uses a fixed resistor at R7 for TIA feedback
     resistance.

#. **Fixed Resistor Numerical Control** -- Input the value of the resistor
   populated at R7 if not using the rheostat.
#. **RDAC Value Numerical Indicator** -- Value transmitted to the RDAC
   register of the rheostat in hexadecimal format.
#. **Rheostat Resistance Numerical Indicator** -- Equivalent resistance of the
   rheostat.
#. **Program Rheostat Button** -- Loads the current RDAC value to the 50-TP
   Memory Block of the digital rheostat.

   .. warning::

      Programming the current RDAC value to 50-TP can only occur 50 times.

Running the System (SDP-B)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Open **CN0357.exe** from the default installation location.
#. The software will connect to the board automatically.
#. Click the **Run** button.
#. Click the **Stop** button when acquisition is complete.

Saving Data to a Spreadsheet File (SDP-B)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Click the **Save Data** button.
#. Browse to the directory location where the spreadsheet file is to be saved.
#. Name the file.
#. Click **OK**.

.. note::

   The software saves the spreadsheet file as ASCII text with tab-separated
   columns.

EVAL-CN0357-ARDZ Arduino Shield
---------------------------------

The EVAL-CN0357-ARDZ is an Arduino-form-factor shield board for the CN0357
gas detector circuit.

Sensor Footprint
~~~~~~~~~~~~~~~~~

Three-electrode electrochemical toxic gas sensors can be used with the
EVAL-CN0357-ARDZ. The footprint accommodates three different sizes of sensors.
The Alphasense CO-AX electrochemical gas sensor was used during testing and
programming.

**Recommended PCB Sockets (for Alphasense Sensors):**

- A Series Sensors -- Mill-Max 0364-0-15-15-13-27-10-0
- B Series Sensors -- Mill-Max 0294-0-15-15-06-27-10-0
- D Series Sensors -- Mill-Max 0667-0-15-15-30-27-10-0

The sensor may be connected to the M1 footprint using the appropriate pin
sockets.

**Jumper P1 Settings:**

- "0" position -- Sensor output connected to ADC (default)
- "1" position -- Sensor output connected to A1 pin of ANALOG header, for
  connection to external ADCs

Chip Select Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The chip select jumpers allow changing the pin mapping of the AD7790 and AD5270
chip select lines to different Arduino digital pins.

**AD7790 CS Selection:**

.. figure:: cn0357-hdr-01.png
   :width: 100 px
   :align: center

   AD7790 CS Jumper Header

- Pin 1 shunted to Pin 2: CS connected to **Digital Pin 10**
- Pin 3 shunted to Pin 4: CS connected to **Digital Pin 9**
- Pin 5 shunted to Pin 6: CS connected to **Digital Pin 8**

**AD5270 CS Selection:**

.. figure:: cn0357-hdr-02.png
   :width: 100 px
   :align: center

   AD5270 CS Jumper Header

- Pin 1 shunted to Pin 2: CS connected to **Digital Pin 7**
- Pin 3 shunted to Pin 4: CS connected to **Digital Pin 6**
- Pin 5 shunted to Pin 6: CS connected to **Digital Pin 5**

ADICUP360 Demo
--------------

The **ADuCM360_demo_cn0357** is a toxic gas (CO) detector demo project for the
EVAL-ADICUP360 base board with the EVAL-CN0357-ARDZ shield, created using the
GNU ARM Eclipse Plug-ins in Eclipse environment.

The EVAL-CN0357-ARDZ shield provides a potentiostatic circuit for biasing the
electrochemical sensor, along with a programmable TIA and 16-bit Sigma-Delta
ADC. The TIA converts the small currents passing through the sensor to a
voltage readable by the ADC. The 16-bit ADC value is received via the SPI
interface of the EVAL-ADICUP360, where the gas concentration is computed.

The application configures the necessary components, processes ADC output
values, and performs all necessary conversions to provide the gas
concentration. A UART interface (9600 baud rate, 8-bit data length) outputs
results to a terminal window: ADC Data Register **codes**, ADC Input Voltage
**volts**, and Gas Concentration **Parts Per Million (PPM)**.

At startup, the software computes parameters and configures the digital
rheostat (AD5270) of the TIA. The required parameters (sensor sensitivity and
sensor range) can be modified by changing the ``SENSOR_SENSITIVITY`` and
``SENSOR_RANGE`` constants in ``CN0357.h``.

Demo Requirements (ADICUP360)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware:

- EVAL-ADICUP360
- EVAL-CN0357-ARDZ
- Electrochemical Gas Sensor (included with CN0357)
- Micro-USB to USB cable
- PC or laptop with a USB port

Software:

- ADuCM360_demo_cn0357 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM36x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)
- Serial terminal program (such as PuTTY or Tera Term)

Setting Up the Hardware (ADICUP360)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Set the jumpers/switches on the EVAL-ADICUP360 for programming mode.
#. Connect the **EVAL-CN0357-ARDZ** to the Arduino connectors **P2, P5, P6,
   P7, P8** of the **EVAL-ADICUP360** board.
#. Connect an acceptable 7 V to 12 V power supply to the P11 barrel jack of
   the EVAL-ADICUP360.

   .. warning::

      An external power supply to barrel jack **P11** is required to supply
      power for the EVAL-CN0357-ARDZ. The boards will not work if powered
      only from the DEBUG_USB or USER_USB.

#. Plug the USB cable from the PC to the EVAL-ADICUP360 via the Debug USB
   (P14).

Obtaining the Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways to program the ADICUP360:

#. **Drag and Drop** -- Drag the prebuilt ``.bin`` file to the MBED drive.
   This is the easiest way to get started.
#. **Build, Compile, and Debug using CCES** -- Allows parameter changes and
   software customization.

.. admonition:: Download

   Prebuilt CN0357 Bin File:

   - `ADuCM360_demo_cn0357.bin
     <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0357.bin>`__

   Complete CN0357 Source Files:

   - `ADuCM360_demo_cn0357 Source Code
     <https://github.com/analogdevicesinc/EVAL-ADICUP360/tree/master/projects/ADuCM360_demo_cn0357>`__

Configuring the Software Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Sensor Range** -- ``SENSOR_RANGE`` -- Maximum gas concentration (ppm)
  detectable by the electrochemical sensor (defined in ``CN0357.h``):

  .. code-block:: c

     #define SENSOR_RANGE     2000

- **Sensor Sensitivity** -- ``SENSOR_SENSITIVITY`` -- Sensitivity (nA/ppm) of
  the electrochemical sensor (defined in ``CN0357.h``):

  .. code-block:: c

     #define SENSOR_SENSITIVITY  65

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~~

#. Flash the program to the EVAL-ADICUP360.
#. Switch the USB cable from the DEBUG USB (P14) to the USER USB (P13).
#. Configure the serial terminal with the following UART settings:

   .. code-block:: none

      Select COM Port
      Baud rate: 9600
      Data: 8 bit
      Parity: none
      Stop: 1 bit
      Flow Control: none

#. Press the **<Enter>** key to receive new results.

Project Structure
~~~~~~~~~~~~~~~~~~

The project uses the ADuCM36x C/C++ Project structure and contains system
initialization (disabling watchdog, setting system clock, enabling peripheral
clocks), port configuration for SPI1, UART via P0.6/P0.7, SPI/UART
read/write functions, AD7790 control, AD5270 control, and gas concentration
computation.

In the **src** and **include** folders:

- ``Communication.c/h`` -- SPI and UART specific data
- ``AD7790.c/h`` -- ADC control
- ``AD5270.c/h`` -- Rheostat control
- ``CN0357.c/h`` -- Gas detector application configurations and computations

The **RTE** folder contains device and system related files:

- **Device Folder** -- Low-level drivers for ADuCM360 microcontroller
- **system.rteconfig** -- Peripheral component selection along with startup
  and ARM CMSIS files

Change Log (Rev B to Rev C)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Replaced R15, R16, R17, R19, and R20 with headers AD7790_CS and AD5270_CS
  for CS line selection.
- Connected ICSP SPI lines MOSI, MISO, and SCLK to DIGI1 headers (Arduino
  pins D11, D12, and D13 respectively).
- No longer requires an external 7 V to 12 V wall power supply -- board
  powered through the 5 V pin (Arduino POWER header).

Documents
---------

- :adi:`CN0357 Circuit Note <CN0357>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0357-ARDZ Design & Integration Files
   <https://www.analog.com/cn0357-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`ADA4528-2 Product Page <ADA4528-2>`
- :adi:`AD5270 Product Page <AD5270>`
- :adi:`ADR3412 Product Page <ADR3412>`
- :adi:`AD7790 Product Page <AD7790>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
