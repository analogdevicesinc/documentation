.. _eval-cn0349-pmdz:

EVAL-CN0349-PMDZ
=================

Conductivity and Temperature Measurement System with Isolation.

Overview
--------

:adi:`CN0349` provides a robust and complete solution for processing
conductivity and temperature inputs into digital code. The design solution is
optimized for high precision and low cost measurement, using five active
devices, and has a total error less than 1% FSR after calibration. The output
of the circuit is fully isolated, and therefore ground-loop interference is
effectively reduced, making it ideal for industrial applications.

The circuit incorporates the :adi:`AD5934` 12-bit impedance converter,
:adi:`ADG715` octal SPST switch, :adi:`AD8606` rail-to-rail op-amp,
:adi:`ADuM5000` isolated DC-DC converter, and :adi:`ADuM1250` dual I2C
isolator to convert the conductivity and temperature inputs to digital code.

The circuit has an 8-pin Digilent Pmod I2C interface connector on board, which
can be used for connection to a microprocessor or FPGA.

The :adi:`CN0349` circuit note discusses the design steps needed to optimize
the circuit for a specific measuring range including accuracy analysis and
component selection considerations.

.. figure:: cn0349_hw_375.jpg
   :align: center
   :width: 400

   EVAL-CN0349-PMDZ Evaluation Board

.. figure:: cn0349_00_1024.gif
   :align: center

   CN0349 Functional Block Diagram

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` Controller Board (SDP-B Board)
- :adi:`EVAL-CN0349-PMDZ <CN0349>` Evaluation Board
- :adi:`EVAL-CFTL-6V-PWRZ` +6 V Power Supply or equivalent
- :adi:`SDP-PMD-IB1Z` SDP-to-PMOD Interposer Board
- Resistance decade box (e.g. IET RS-200) or real conductivity cell with
  integrated Pt100 sensor (e.g. Sensorex CS200TC-PT1)
- `CN0349 Evaluation Software
  <https://www.analog.com/CN0349>`__
- PC with USB type A port (Windows 7 64-bit or later)
- USB type A to USB type mini-B cable

General Setup
-------------

- The :adi:`EVAL-CFTL-6V-PWRZ` (+6 V DC Power Supply) powers the
  :adi:`SDP-PMD-IB1Z` (Interposer Board) via the DC barrel jack.
- The :adi:`SDP-PMD-IB1Z` (Interposer Board) connects to the
  :adi:`EVAL-SDP-CB1Z` (SDP-B Board) via the 120-pin connector A.
- The :adi:`EVAL-SDP-CB1Z` (SDP-B Board) connects to the PC via the USB cable.
- The EVAL-CN0349-PMDZ connects to the Interposer Board via the 8-pin header
  Digilent Pmod I2C interface connector (J2 on both boards).
- The resistance decade box or conductivity cell connects to the
  EVAL-CN0349-PMDZ via the terminal block J1.

.. figure:: cn0349_general_setup.png
   :align: center

   CN0349 General Test Setup

Connecting the Hardware
-----------------------

#. Connect the :adi:`EVAL-CFTL-6V-PWRZ` (+6 V DC Power Supply) to the barrel
   jack J1 of the :adi:`SDP-PMD-IB1Z` (Interposer Board). Make sure the jumper
   is positioned as shown below.

   .. figure:: cn0349_connecthw_1.png
      :align: center
      :width: 600

      Power supply connected to the Interposer Board

#. Connect the 120-pin connector on the :adi:`SDP-PMD-IB1Z` (Interposer Board)
   to the 120-pin connector marked **CON A** on the :adi:`EVAL-SDP-CB1Z`
   (SDP-B Board).

   .. figure:: cn0349_connecthw_2.png
      :align: center
      :width: 600

      Interposer Board connected to the SDP-B Board

#. Connect the USB cable supplied with the :adi:`EVAL-SDP-CB1Z` (SDP-B Board)
   to the USB port on the PC and the SDP Board.

   .. figure:: cn0349_connecthw_3.png
      :align: center
      :width: 600

      USB cable connected to the SDP-B Board

   .. note::

      Verify that the SDP drivers are loaded properly. Open the Device Manager
      and check if the SDP Board is recognized. If not, repeat the previous
      steps.

   .. figure:: cn0349_connecthw_3a.png
      :align: center

      Device Manager showing the SDP-B Board recognized

#. Connect the EVAL-CN0349-PMDZ (CN0349 Board) to the :adi:`SDP-PMD-IB1Z`
   (Interposer Board) via the 8-pin header Digilent Pmod I2C interface
   connector.

   .. figure:: cn0349_connecthw_4.png
      :align: center
      :width: 600

      EVAL-CN0349-PMDZ connected to the Interposer Board

#. Connect the resistance decade box or conductivity cell to **pin 4** and
   **pin 5** of the J1 terminal block on the EVAL-CN0349-PMDZ. If a
   conductivity cell with integrated Pt100 sensor is used, the sensor should be
   wired to **pin 3** and **pin 2** of J1. **Pin 1** can be used to wire the
   ground shield of the conductivity cell.

Hardware Interface
------------------

The EVAL-CN0349-PMDZ uses a standard Digilent Pmod 8-pin I2C connector
interface (J2) to communicate with the host.

.. list-table::
   :header-rows: 1

   * - J2 Pin
     - Pin Function
     - Mnemonic
   * - Pin 1
     - Serial Clock
     - SCL
   * - Pin 2
     - Serial Clock
     - SCL
   * - Pin 3
     - Serial Data
     - SDA
   * - Pin 4
     - Serial Data
     - SDA
   * - Pin 5
     - Digital Ground
     - DGND
   * - Pin 6
     - Digital Ground
     - DGND
   * - Pin 7
     - Digital Power
     - VDD
   * - Pin 8
     - Digital Power
     - VDD

The CN0349 board accepts both +3.3 V +/-10% or +5 V +/-10% power supplies.
The minimum current requirement is 300 mA.

.. important::

   The power supply for the CN0349 must provide the required current with
   minimum voltage drop. Please make sure the host has the same I/O level
   standard as the CN0349 board. Otherwise, permanent damage to the CN0349
   may occur.

Using the Evaluation Software
------------------------------

Establishing a USB Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Follow the instructions to properly install the software and connect the
   hardware as described in the previous sections.
#. Open the file named **CN0349.exe** in the installation directory or the
   shortcut in the Start menu.
#. The software should connect to the board automatically. If the hardware is
   not recognized by the PC, the Hardware Select window will appear, indicating
   that the software is waiting for a proper hardware connection. After
   connecting the hardware, the list in the window will populate. Choose the
   connected hardware and click **Select**.

   .. figure:: cn0349_establishing_connection_3a.png
      :align: center

      Hardware Select dialog waiting for SDP-B Board connection

#. Upon success, the **System Status String Indicator** will display
   *SDP Board Ready to Acquire Data*.

Software Controls
~~~~~~~~~~~~~~~~~

The CN0349 evaluation software provides the following controls and indicators:

.. figure:: cn0349_using_sw_1.png
   :align: center

   CN0349 Evaluation Software -- Main Tab

- **1 -- Measure Button** -- performs a measurement procedure and displays data
  in the measurement indicators.
- **2 -- Control Tabs** -- switches between the Main, Calibrate System,
  Register Value, and SDP Revision panels.
- **3 -- Impedance Indicator** -- displays the measured input impedance in
  ohms.
- **4 -- Conductivity Indicator** -- displays the measured conductivity in
  mS/cm. The result depends on the applied probe corrections (7) and (9).
- **5 -- Conductivity Temperature Compensated Indicator** -- displays
  temperature-compensated conductivity in mS/cm according to the chosen
  temperature coefficient (8).
- **6 -- Temperature Indicator** -- displays the measured temperature in
  degrees C using an external Pt100 RTD sensor.
- **7 -- Cell Constant Control** -- applies the cell constant for the
  conductivity probe.
- **8 -- Temperature Coefficient Control** -- applies the temperature
  coefficient of the solution.
- **9 -- Offset Control** -- applies offset correction to the measured
  conductivity. If offset correction is not needed, leave this control at
  0 mS/cm.
- **10 -- Measurement Range Radio Buttons** -- selects the input measurement
  range.
- **11 -- Measurement Range Indicator** -- shows the limits of the chosen input
  measurement range.
- **12 -- System Status String Indicator** -- displays a message to the user
  detailing the current state of the software.
- **13 -- System Status LED Indicator** -- displays the current state of the
  software in the form of an LED (Inactive, Busy, Error, or Waiting for user
  action).

.. figure:: cn0349_using_sw_2.png
   :align: center

   CN0349 Evaluation Software -- Calibrate System Tab

- **14 -- Calibrate Button** -- initiates board calibration.
- **15 -- Calibration Resistances Controls** -- sets the values for the three
  on-board calibration resistances (R3, R4, R7). Change these values only if
  different calibration resistances are populated on the board.

Calibrating the Board
~~~~~~~~~~~~~~~~~~~~~

#. Establish a USB connection.
#. Click the **Calibrate System** tab.
#. Press the **Calibrate** button.
#. Wait for calibration to finish; a pop-up window indicates progress.

   .. figure:: cn0349_cal_procedure_steps_5.png
      :align: center

      Calibration in progress

#. Click **OK** when calibration is complete.

   .. figure:: cn0349_cal_procedure_steps_5a.png
      :align: center

      Calibration finished

Measuring Data
~~~~~~~~~~~~~~

#. Establish a USB connection.
#. Choose the appropriate **Probe Corrections** settings.
#. Select the **Measurement Range**.
#. Click the **Measure** button.
#. Wait for the measurement to complete and click **OK**.
#. After clicking **OK**, the indicators will present the measured data.

Software Recommendations
-------------------------

.. warning::

   There are several important restrictions that must be addressed when
   developing custom application code using the EVAL-CN0349-PMDZ. If you do
   not follow these requirements, your results will likely be incorrect or
   erroneous.

When developing custom application code with the EVAL-CN0349-PMDZ, the
following requirements must be adhered to:

Digital Communication
~~~~~~~~~~~~~~~~~~~~~

The I2C communication protocol must be designed carefully. The maximum I2C
speed and timing is limited by the :adi:`ADG715` and the :adi:`AD5934`. The
maximum I2C clock speed for both parts is 400 kHz. The host I2C timing and
speed must meet the requirements of both the ADG715 and AD5934.

.. note::

   On the EVAL-CN0349-PMDZ evaluation board, the ADG715 I2C address is set to
   **0x48**, and the AD5934 I2C address is **0x0D**. Make sure the host I2C bus
   has no devices that share these addresses.

Input Signal Setting
~~~~~~~~~~~~~~~~~~~~

The :adi:`AD5934` excitation voltage and PGA must use the following settings:

.. list-table::
   :header-rows: 1

   * - Part
     - I2C Address
     - Register Address
     - Register Data
     - Description
   * - AD5934
     - 0x0D
     - 0x80
     - 0x01
     - Excitation Voltage 2.0 Vp-p, Internal PGA=1

System Calibration
~~~~~~~~~~~~~~~~~~

The :adi:`ADG715` controls the conductivity calibration. At least one of the
following calibration settings must be used. Two calibration points per range
is recommended:

.. list-table::
   :header-rows: 1

   * - I2C Data
     - Function
     - Description
   * - 0x09
     - High Range Cal 1
     - Rfb=R9=100 ohm, Rcal=R3=100 ohm
   * - 0x11
     - High Range Cal 2
     - Rfb=R9=100 ohm, Rcal=R4=1 kohm
   * - 0x12
     - Low Range Cal 1
     - Rfb=R8=1 kohm, Rcal=R4=1 kohm
   * - 0x22
     - Low Range Cal 2
     - Rfb=R8=1 kohm, Rcal=R7=10 kohm

.. important::

   The hardware limitations in the CN0349 board need to be considered carefully
   when writing the software. If other settings for AD5934 and ADG715 outside
   the limits described above are used, the AD5934 ADC input must not be
   saturated. The AD5934 ADC reference is AVDD2=3.3 V which determines the
   input range.

Measurement Ranges
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Range
     - Conductivity Value
   * - Low Range
     - 1 uS to 1 mS
   * - High Range
     - 1 mS to 1 S

.. note::

   The board must be calibrated before measurement. Calibration theory and
   calculations are described in the :adi:`CN0349` circuit note.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `CN0349 Design & Integration Files <https://www.analog.com/CN0349>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD5934 Product Page <AD5934>`
- :adi:`ADG715 Product Page <ADG715>`
- :adi:`AD8606 Product Page <AD8606>`
- :adi:`ADuM5000 Product Page <ADUM5000>`
- :adi:`ADuM1250 Product Page <ADUM1250>`
- :adi:`CN0349 Circuit Note <CN0349>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
