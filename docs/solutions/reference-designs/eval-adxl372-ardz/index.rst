.. _eval-adxl372-ardz:

EVAL-ADXL372-ARDZ
==================

Ultralow Power, +/-200 g, 3-Axis MEMS Accelerometer Arduino Shield.

Overview
--------

The :adi:`EVAL-ADXL372-ARDZ` is an Arduino shield evaluation board for the
:adi:`ADXL372` ultralow power, 3-axis, +/-200 g MEMS accelerometer. The
ADXL372 consumes only 22 uA at a 3200 Hz output data rate (ODR) and is
designed for IoT applications such as:

- Impact and shock detection
- Asset health assessment
- Portable Internet of Things (IoT) edge nodes
- Concussion and head trauma detection

In addition to its ultralow power consumption, the ADXL372 has many features
to enable impact detection while providing system-level power reduction. The
device includes a deep multimode output FIFO, several activity detection
modes, and a method for capturing only the peak acceleration of
over-threshold events.

Two additional lower power modes with interrupt-driven wake-up features are
available for monitoring motion during periods of inactivity. In **wake-up
mode**, acceleration data can be averaged to obtain a low enough output noise
to trigger on low-g thresholds. In **instant-on mode**, the ADXL372 consumes
only 1.4 uA while continuously monitoring the environment for impacts. When
an impact event that exceeds the internally set threshold is detected, the
device switches to normal operating mode fast enough to record the event.

The EVAL-ADXL372-ARDZ shield is designed in Arduino Uno R3 form factor,
making it compatible with the :ref:`EVAL-ADICUP3029 <eval-adicup3029>`
development platform as well as standard Arduino Uno R3 base boards.

.. figure:: top_adxl_int_together.png
   :align: center

   EVAL-ADXL372-ARDZ shield with EVAL-ADXL372Z-PIN assembled together.

Connectors and Jumper Configuration
-------------------------------------

The EVAL-ADXL372-ARDZ shield has four jumpers (P10, P11, P12, P13) to
increase flexibility when stacking systems together. Each jumper and its
purpose is described below.

.. figure:: eval-adxl-ardz-int_jumper_select.png
   :align: center

   EVAL-ADXL372-ARDZ jumper locations.

ADXL_CS_SELECT (P10)
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Configuration
     - Function
   * - Pin 1-2
     - Routes ADXL372 CS pin to CS_1
   * - Pin 2-3
     - Routes ADXL372 CS pin to CS_2

ADXL_INT1_SELECT (P11)
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Configuration
     - Function
   * - Pin 1-2
     - Connects ADXL372 INT1 pin to INT1_A
   * - Pin 2-3
     - Connects ADXL372 INT1 pin to INT1_B

ADXL_INT2_SELECT (P12)
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Configuration
     - Function
   * - Pin 1-2
     - Connects ADXL372 INT2 pin to INT2_A
   * - Pin 2-3
     - Connects ADXL372 INT2 pin to INT2_B

VOLTAGE TRANSLATOR VDDIO SELECT (P13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Configuration
     - Function
   * - Pin 1-2
     - Connects ADXL VDDIO to the 3.3V Arduino pin
   * - Pin 2-3
     - Connects ADXL VDDIO to the IOREF Arduino pin

Connecting/Mounting the ADXL372
---------------------------------

Direct Mounting (P5 and P2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connectors P5 and P2 are designed to be directly interfaced with the
EVAL-ADXL372Z-PIN evaluation board. This creates a mechanically strong
connection and allows for the Arduino shield to directly include the ADXL372
sensor. Be careful when connecting the EVAL-ADXL372Z-PIN with the
EVAL-ADXL-ARDZ-INT to make sure that all the signals go to the correct pin
of connectors P5 and P2.

.. figure:: eval-adxl-ardz-int_direct_connection.png
   :align: center

   EVAL-ADXL372-ARDZ direct mounting connector locations (P5 and P2).

.. list-table:: Direct Mounting Connector Pinout
   :header-rows: 1
   :widths: 30 35 35

   * - Pin Number
     - P5 Signal Name
     - P2 Signal Name
   * - PIN 1
     - DGND
     - +3.3V
   * - PIN 2
     - SCLK
     - IOREF
   * - PIN 3
     - MOSI
     - DGND
   * - PIN 4
     - MISO
     - INT2
   * - PIN 5
     - CS
     - INT1

.. figure:: top_adxl_int_separate.png
   :align: center

   EVAL-ADXL372-ARDZ shield and EVAL-ADXL372Z-PIN board separated.

Ribbon Cable Connection (P7 and P1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connectors P7 and P1 are designed to interface with the EVAL-ADXL372Z-PIN
via a ribbon cable. This allows for remotely mounting the sensor when you
cannot have the rest of the electronics on the unit being sensed. Because
this is a cabled option, you could also use other digital-output accelerometer
devices with the EVAL-ADXL-ARDZ-INT such as the ADXL346/46 or the ADXL355/57.

.. figure:: eval-adxl-ardz-int_cable_connection.png
   :align: center

   EVAL-ADXL372-ARDZ ribbon cable connector locations (P7 and P1).

.. list-table:: Ribbon Cable Connector Pinout
   :header-rows: 1
   :widths: 30 35 35

   * - Pin Number
     - P7 Signal Name
     - P1 Signal Name
   * - PIN 1
     - SCLK
     - +3.3V
   * - PIN 2
     - MOSI
     - IOREF
   * - PIN 3
     - MISO
     - DGND
   * - PIN 4
     - CS
     - DATA_RDY
   * - PIN 5
     - SDA
     - INT1
   * - PIN 6
     - SCL
     - INT2

Design and Integration Files
------------------------------

`EVAL-ADXL372-ARDZ Design & Integration Files <https://www.analog.com/media/en/evaluation-documentation/evaluation-design-files/eval-adxl372-ardz-designsupport.zip>`__

- Schematic
- PCB Layout
- Bill of Materials
- Allegro Project

ADICUP3029 High Impact Detection Demo (Bluetooth)
---------------------------------------------------

This demo uses the EVAL-ADXL372-ARDZ along with the
:ref:`EVAL-ADICUP3029 <eval-adicup3029>` to create an impact measurement
application. The ADXL372 is configured to operate in "Instant On" mode, which
means that the device is powered down until the sensor records an impact event
that triggers a threshold. Once that level is surpassed, the ADXL372
automatically goes into measurement mode to capture the rest of the impact
event.

The EVAL-ADICUP3029 is designed for IoT applications and comes with an
on-board **Bluetooth 5.0** module. The ADuCM3029 is placed in "Flexi" mode to
optimize its ultra-low power consumption and can only be woken up from an
external interrupt that comes from the ADXL372 impact sensor. At that point
the ADuCM3029 is placed into full power mode to perform the necessary
application tasks, before being placed back into "Flexi" mode.

The data is sent via Bluetooth 5.0 to an iOS smart device, where all the max
impact data can be read.

Both boards and all components are used in their respective low power modes
to optimize the solution's battery life.

Demo Requirements
~~~~~~~~~~~~~~~~~~

Hardware:

- :ref:`EVAL-ADICUP3029 <eval-adicup3029>`
- EVAL-ADXL372-ARDZ
- Micro-USB to USB cable
- PC or laptop with a USB port
- iOS smart phone/tablet (optional, for Bluetooth display)

Software:

- ADuCM3029_Asset_Health demo software
- CrossCore Embedded Studio (2.6.0 or higher)
- ADuCM302x DFP (2.0.0 or higher)
- ADICUP3029 BSP (1.0.0 or higher)
- iOS IoTNode App (optional)
- Serial terminal program such as PuTTY or Tera Term (optional, for UART
  output)

Setting Up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~~

1. Set switch **S2** to **USB Arduino** function in order to view data over
   UART. The UART baud rate is **9600** baud.

.. figure:: adicup3029_s2_switch.jpg
   :align: center

   EVAL-ADICUP3029 S2 switch set to USB Arduino position.

2. Place the **EVAL-ADXL372-ARDZ-INT** on top of the **EVAL-ADICUP3029**.
3. Make sure the jumpers **P10, P11, P12** are configured as follows:

   - P10 -- Pin 1-2
   - P11 -- Pin 1-2
   - P12 -- Pin 1-2

.. figure:: eval_adxl_ardz_int_jumpers.jpg
   :align: center

   EVAL-ADXL372-ARDZ jumper configuration for the ADICUP3029 demo.

4. Plug in the micro-USB cable into the (P10) USB port on the EVAL-ADICUP3029,
   and the other end into the PC or laptop.

Obtaining the Software
~~~~~~~~~~~~~~~~~~~~~~~

There are two basic ways to program the ADICUP3029 with the software for
the ADXL372:

1. **Drag and Drop** -- Drag the prebuilt ``.hex`` file to the DAPLink drive.
   This is the easiest way to get started with the reference design.
2. **Build and Debug** -- Import the project into CrossCore Embedded Studio
   to customize the software parameters.

- `ADuCM3029_Asset_Health.hex (prebuilt) <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_Asset_Health.hex>`__
- `ADuCM3029_Asset_Health Source Code <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_Asset_Health>`__

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~~~

To establish connection over UART, a micro-USB cable connected to the board
and a serial console program like `PuTTY <http://www.putty.org/>`__ are
required. The UART configuration is:

.. code-block:: none

   COM Port: <Select your COM port>
   Baud rate: 9600
   Data: 8 bit
   Parity: none
   Stop: 1 bit
   Flow Control: none

.. figure:: serial_terminal_capture.png
   :align: center

   ADXL372 serial terminal output showing impact data.

Smart Device Output
~~~~~~~~~~~~~~~~~~~~

Open up the IoTNode app on your iOS smart phone or tablet:

.. figure:: iotnode_app_main.png
   :align: center
   :width: 400

   IoTNode application main screen.

1. Press the **Scan** button on the bottom left corner for the app to start
   searching for Bluetooth devices.

.. figure:: iotnode_app_scan.png
   :align: center
   :width: 400

   IoTNode application scanning for Bluetooth devices.

2. Once the device is visible, press **Connect** to access the information
   provided over Bluetooth.

.. figure:: iotnode_app_connected.png
   :align: center
   :width: 400

   IoTNode application displaying impact acceleration data.

3. After connecting and generating enough acceleration (minimum of **10 g**
   on any axis), information will be displayed on the application. To generate
   this high value of acceleration, tap the board against your hand (do not
   apply excessive force to avoid damaging the device).

Project Structure
~~~~~~~~~~~~~~~~~~

.. figure:: adxl372_project_structure.png
   :align: center

   ADXL372 demo project structure diagram.

The project is structured in 3 layers:

- **Hardware layer** -- ADXL372
- **Communication layer** -- SPI interface between sensor and MCU
- **Application layer** -- ADuCM3029 and EM9304 BLE

The ADXL372 transmits data to the ADuCM3029 controller through the
Communication layer. The data is processed and sent over BLE to a mobile
device.

Documents
---------

- :adi:`ADXL372 Datasheet <ADXL372>`

Additional Information
----------------------

- :adi:`ADXL372 Product Page <ADXL372>`
- :adi:`EVAL-ADXL372-ARDZ Product Page <EVAL-ADXL372-ARDZ>`
- `EVAL-ADICUP3029 GitHub Repository <https://github.com/analogdevicesinc/EVAL-ADICUP3029>`__

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
