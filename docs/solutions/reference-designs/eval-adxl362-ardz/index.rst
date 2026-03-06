.. imported from: https://wiki.analog.com/resources/pmods/adxl362

.. _eval-adxl362-ardz:

EVAL-ADXL362-ARDZ
==================

Ultralow Power 3-Axis MEMS Accelerometer Arduino Shield.

Overview
--------

The :adi:`EVAL-ADXL362-ARDZ` is an Arduino shield evaluation board for the
:adi:`ADXL362` ultralow power, 3-axis MEMS accelerometer. The ADXL362 is
capable of measuring dynamic acceleration (resulting from motion or shock)
as well as static acceleration (gravity). It provides 12-bit output resolution
and has three operating ranges: +/-2 g, +/-4 g, and +/-8 g.

.. figure:: eval-adxl362-ardz.jpg
   :width: 400px
   :align: center

   EVAL-ADXL362-ARDZ shield board

Additional useful features include an on-chip 12-bit temperature sensor
accurate to +/-0.5 degrees Celsius, motion-triggered wake-up functionality,
and several activity detection modes which make it ideal for portable
low-power instruments. The sensor draws less than 2 uA at 100 Hz ODR.

The shield also includes an NHD-C12832A1Z-NSW-BBW 128x32 LCD display for
real-time data visualization of acceleration values and motion detection zones.

The EVAL-ADXL362-ARDZ shield is designed in Arduino Uno R3 format, making it
compatible with both the :ref:`EVAL-ADICUP360 <eval-adicup360>` and
:ref:`EVAL-ADICUP3029 <eval-adicup3029>` development platforms, as well as
standard Arduino Uno R3 base boards.

.. note::

   The EVAL-ADXL362-ARDZ board has a large capacitor (C18) that holds charge
   for the LCD screen. When power cycling the system, you must wait
   approximately 5 seconds to allow the capacitors on the board to fully
   discharge. This is a power requirement for the ADXL362, which notes in the
   datasheet that the power rail must come all the way back down to 0V before
   powering back up.

Connectors and Jumper Configuration
------------------------------------

The EVAL-ADXL362-ARDZ shield has four jumpers to increase flexibility when
stacking systems together. Each jumper and its purpose is described below.

.. figure:: eval-adxl362-ardz_silkscreen_w-jumper.png
   :width: 500px
   :align: center

   EVAL-ADXL362-ARDZ jumper locations

ADXL_CS_SEL
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Configuration
     - Function
   * - Pin 1-2
     - Routes ADXL362 CS pin to P0.3/IRQ0/CS1
   * - Pin 2-3
     - Routes ADXL362 CS pin to P0.4/RTS/IRQ1

LCD_CS_SEL
~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Configuration
     - Function
   * - Pin 1-2
     - Connects LCD CS pin to P2.2/BM
   * - Pin 2-3
     - Connects LCD CS pin to P1.4/PWM2/MISO0

ADXL_INT_SEL
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Configuration
     - Function
   * - Pin 1-2
     - Connects ADXL362 Interrupt pin 1 (INT1) to P1.0/IRQ3
   * - Pin 2-3
     - Connects ADXL362 Interrupt pin 2 (INT2) to P1.0/IRQ3

LCD_RST_SEL
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Configuration
     - Function
   * - Pin 1-2
     - Connects LCD Reset to IOREF
   * - Pin 2-3
     - Connects LCD Reset to pin P1.1/IRQ4

Design and Integration Files
-----------------------------

`EVAL-ADXL362-ARDZ Design & Integration Files <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/eval-adxl362-ardz-designsupport.zip>`__

- Schematics
- PCB Layout and Mounting Diagram
- Bill of Materials
- Allegro Project

ADICUP360 Accelerometer Demo
------------------------------

The **ADuCM360_demo_adxl362** is an accelerometer demo project for the
:ref:`EVAL-ADICUP360 <eval-adicup360>` base board with the EVAL-ADXL362-ARDZ
shield, created using CrossCore Embedded Studios IDE.

Demo Requirements
~~~~~~~~~~~~~~~~~~

Hardware:

- :ref:`EVAL-ADICUP360 <eval-adicup360>`
- EVAL-ADXL362-ARDZ
- Micro-USB to USB cable
- PC or laptop with a USB port

Software:

- ADuCM360_demo_adxl362 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM36x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)

Setting Up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~~

1. Configure jumpers on the EVAL-ADICUP360 base board per the reference
   configuration (see base board documentation for details).

2. Set the jumpers on the EVAL-ADXL362-ARDZ shield as shown in the figure
   below.

   .. figure:: eval-adxl362-ardz_default_software_config.png
      :width: 360px
      :align: center

      EVAL-ADXL362-ARDZ default jumper configuration

   .. note::

      It is recommended to select P1.4 pin for LCD_CS_SEL when using the
      ADXL362 shield with the ADICUP360 base board because P2.2 is also the
      BM pin and it can create problems in debug sessions.

3. Plug the EVAL-ADXL362-ARDZ shield into the EVAL-ADICUP360 base board.
4. Power the EVAL-ADICUP360 base board via the DEBUG USB port (P14).

Obtaining the Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways to program the ADICUP360 with the software for the ADXL362:

1. **Drag and Drop** -- Drag the prebuilt ``.bin`` file to the MBED drive.
   This is the easiest way to get started.
2. **Build and Debug** -- Import the project into CrossCore Embedded Studio
   to customize the software parameters.

The prebuilt binary and complete source code are available on GitHub:

- `ADuCM360_demo_adxl362.bin (prebuilt) <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_adxl362.bin>`__
- `ADuCM360_demo_adxl362 Source Code <https://github.com/analogdevicesinc/EVAL-ADICUP360/tree/master/projects/ADuCM360_demo_adxl362>`__

Configuring the Software Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the temperature units in ``ADXL362.h``:

.. code-block:: c

   #define TEMP_ADC        1        /* 0 for ADC units or 1 for Celsius degrees */

Configure the ADXL362 calibration values in ``ADXL362.h`` (values vary per
sensor; these are typical datasheet values):

.. code-block:: c

   #define ACC_TEMP_BIAS             (float)350
   #define ACC_TEMP_SENSITIVITY      (float)0.065

Set the accelerometer scan time in ``ADXL362.h`` (how often axis and temperature
data are read, in ms):

.. code-block:: c

   #define SCAN_SENSOR_TIME   500

Set the activity and inactivity thresholds in ``ADXL362.h`` (in mG):

.. code-block:: c

   #define ACT_VALUE          50
   #define INACT_VALUE        50

Set the activity and inactivity timers in ``ADXL362.h`` (in ms):

.. code-block:: c

   #define ACT_TIMER          50
   #define INACT_TIMER        50

Configure the chip select pin for the ADXL362 in ``Communication.h``:

.. code-block:: c

   #define ADXL_CS_SEL     CSACC_PIN_P0_4     /* CSACC_PIN_P0_3 or CSACC_PIN_P0_4 */

Configure the interrupt pin from the ADXL362 in ``Communication.h``:

.. code-block:: c

   #define ADXL_INT_SEL     INTACC_PIN_1    /* INTACC_PIN_1 or INTACC_PIN_2 */

Configure the chip select pin for the LCD screen in ``Communication.h``:

.. code-block:: c

   #define LCD_CS_SEL      CSLCD_PIN_P1_4     /* CSLCD_PIN_P2_2 or CSLCD_PIN_P1_4 */

Configure the reset pin for the LCD screen in ``Communication.h``:

.. code-block:: c

   #define LDC_RST_SEL     RSLCD_PIN_IOREF    /* RSLCD_PIN_IOREF or RSLCD_PIN_P1_1 */

Outputting Data
~~~~~~~~~~~~~~~~

The application reads the X, Y, and Z acceleration registers and the
temperature register every 500 ms. The acceleration in the 3 axes is displayed
in mG on the LCD, and the temperature can be displayed in both ADC codes or
degrees Celsius depending on software configuration.

There is a movement plane indicator on the right side of the LCD screen that
shows which direction the board is currently tilted (UP, DOWN, RIGHT, LEFT,
CENTER).

The software puts the LCD in a "sleep" mode after 10 seconds if no movement
of the boards is present. The system "wakes up" if the acceleration on any
axis is greater than 50 mG. The threshold values can be adjusted by the user
via the software parameters described above.

The temperature (Treal) is derived from the ADC readings (Tadc) using the
formula:

.. code-block:: none

   Treal = (Tadc + ACC_TEMP_BIAS) / (1 / ACC_TEMP_SENSITIVITY)

Each ADXL362 chip requires individual calibration, which can be done by
setting the ``ACC_TEMP_BIAS`` and ``ACC_TEMP_SENSITIVITY`` parameters.

Project Structure
~~~~~~~~~~~~~~~~~~

The ADuCM360_demo_adxl362 project uses basic ARM Cortex-M C/C++ project
structure. It contains:

- System initialization -- disabling watchdog, setting system clock, enabling
  clock for peripherals
- Port configuration for SPI1, accelerometer sensor, and LCD
- SPI read/write functions
- Sensor monitoring and LCD handling

In the **src** and **include** folders are the source and header files related
to the ADXL362 application:

- ``Communication.c/h`` -- SPI-specific data
- ``ADXL362.c/h`` -- accelerometer data
- ``Lcd.c/h`` -- LCD-related information

The **RTE** folder contains device and system related files:

- **Device Folder** -- low-level drivers for the ADuCM360 microcontroller
- **system.rteconfig** -- allows selection of peripheral components, startup,
  and ARM CMSIS files

ADICUP3029 Accelerometer Wi-Fi Demo
-------------------------------------

The **ADuCM3029_demo_esp8266** is a Wi-Fi demo project for the
:ref:`EVAL-ADICUP3029 <eval-adicup3029>` base board with the EVAL-ADXL362-ARDZ
shield, using the on-board ESP8266 Wi-Fi module and MQTT messaging protocol.

.. figure:: adxl362_project.jpg
   :width: 400px
   :align: center

   ADICUP3029 with ADXL362 shield and ESP8266 Wi-Fi module

Demo Requirements
~~~~~~~~~~~~~~~~~~

Hardware:

- :ref:`EVAL-ADICUP3029 <eval-adicup3029>`
- EVAL-ADXL362-ARDZ
- Micro-USB to USB cable
- PC or laptop with a USB port

Software:

- ADuCM3029_demo_esp8266 software
- CrossCore Embedded Studio (2.6.0 or higher)
- ADuCM302x DFP (2.0.0 or higher)
- ADICUP3029 BSP (1.1.0 or higher)
- Mosquitto MQTT Broker

Setting Up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~~

1. Move the **S2 switch** to the **WiFi** position on the EVAL-ADICUP3029.
2. The ESP8266 Enable Pin needs to be tied directly to 3.3V or pulled high via
   a 10K ohm resistor. On Rev B/C boards, solder a small fly wire from the
   3.3V pin to the enable pin.
3. Plug the ESP8266 into the P1 connector on the EVAL-ADICUP3029.
4. Plug the EVAL-ADXL362-ARDZ shield into the EVAL-ADICUP3029 base board.
5. Plug in the USB cable.

Obtaining the Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~

- `ADuCM3029_demo_esp8266.hex (prebuilt) <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_esp8266_.hex>`__
- `ADuCM3029_demo_esp8266 Source Code <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_esp8266>`__

Configuring the Software
~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the accelerometer scan interval in ``ADXL362.h``:

.. code-block:: c

   #define SCAN_SENSOR_TIME       500      // msecs

Configure activity and inactivity thresholds:

.. code-block:: c

   #define ACCEL_CFG_ACT_TRESH    50      // mG
   #define ACCEL_CFG_INACT_TRESH  50      // mG

Configure activity and inactivity timers:

.. code-block:: c

   #define ACCEL_CFG_ACT_TIMER   100      // msecs
   #define ACCEL_CFG_INACT_TIMER 10       // msecs

Configure network parameters in ``parameters.h``:

.. code-block:: c

   #define WIFI_SSID       "****"
   #define WIFI_PASS       "****"
   #define SERVER_ADDR     "****"

Using the MQTT Broker
~~~~~~~~~~~~~~~~~~~~~~

The program connects to a Wi-Fi network and to a TCP MQTT broker. After
receiving the SUBACK confirmation from the server, the program enters an
infinite loop where it waits for an ADXL362 interrupt triggered when the
acceleration on any axis exceeds 50 mG. The program then publishes the X, Y,
Z readings on the ``adxl`` topic. A subscriber to this topic can view the
data.

This example uses the `Eclipse Mosquitto <https://mosquitto.org>`__ open source
MQTT broker (EPL/EDL licensed), implementing MQTT protocol versions 3.1 and
3.1.1.

To set up data reception:

1. Install and run Mosquitto on your PC.
2. Run ``mosquitto.exe -v`` to start the broker in verbose mode.
3. Use ``ipconfig`` to get your local IP address.
4. Configure ``parameters.h`` with your Wi-Fi credentials and broker IP.
5. Subscribe to the ``adxl`` topic:
   ``mosquitto_sub -t adxl``

.. important::

   Make sure your PC is connected to the same network configured in
   ``parameters.h``. Mosquitto assumes you are running on the same network
   when the executable is launched.

Documents
---------

- :adi:`ADXL362 Datasheet <ADXL362>`

Additional Information
----------------------

- :adi:`ADXL362 Product Page <ADXL362>`
- :adi:`EVAL-ADXL362-ARDZ Product Page <EVAL-ADXL362-ARDZ>`
- `EVAL-ADICUP360 GitHub Repository <https://github.com/analogdevicesinc/EVAL-ADICUP360>`__
- `EVAL-ADICUP3029 GitHub Repository <https://github.com/analogdevicesinc/EVAL-ADICUP3029>`__

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
