.. _eval-cn0397-ardz-software:

Software Demos
==============

The EVAL-CN0397-ARDZ shield is supported on both the EVAL-ADICUP360 and
EVAL-ADICUP3029 platforms.

.. contents::
   :local:
   :depth: 2

ADICUP360 Demo
--------------

The **ADuCM360_demo_cn0397** is an RGB light detection demo project for the
EVAL-ADICUP360 base board with the EVAL-CN0397-ARDZ shield, created using the
GNU ARM Eclipse Plug-ins in Eclipse environment.

General Description
~~~~~~~~~~~~~~~~~~~

The ADuCM360_demo_cn0397 project uses the EVAL-CN0397-ARDZ shield which is a
single-supply, low power, low noise, 16-bit light detector utilizing wavelength
specific photodiodes. The photodiodes are sensitive at different wavelengths to
read light intensity levels over the visible light spectrum where plants are
photosynthetically active.

.. figure:: cn0397_adicup.png
   :align: center
   :width: 500

   EVAL-CN0397-ARDZ with EVAL-ADICUP360 setup

The ADuCM360_demo_cn0397 application performs ADC readings for all 3 channels,
processes them and performs all necessary calculations to provide light
intensity and light concentration for each color.

The 16-bit ADC data are received using the **SPI interface** of the
EVAL-ADICUP360 board. The **UART interface** (115200 baud rate, 8-bit data
length) is used to send and receive data to/from a terminal window.

**Light Intensity** [Lux] is calculated using the ADC output value for the
selected channel and a constant value for each color:

.. code-block:: none

   Light Intensity = CODE * Light Intensity Constant

**Light Concentration** [%] is calculated based on the light intensity and
optimal level for each color:

.. code-block:: none

   Light Concentration = Intensity * 100 / Optimal Level

Besides light intensity and light concentration values, for each channel a
colored bar in [0%, 100%] format is displayed for light concentration
representation. It informs the user when the concentration for a specific
channel reaches 100%.

The application offers the possibility to perform a system offset calibration
for each RGB channel. All calculations use data specific to each color of the
photodiodes used:

.. figure:: cn0397_demo_1.png
   :align: center
   :width: 500

   LED specifications used for calculations

ADICUP360 Demo Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware:

- EVAL-ADICUP360
- EVAL-CN0397-ARDZ
- Micro USB to USB cable
- PC or laptop with a USB port

Software:

- ADuCM360_demo_cn0397 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM36x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)
- Serial Terminal Program (such as PuTTY or Tera Term)

ADICUP360 Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~

#. To program the base board, set the jumpers/switches on the EVAL-ADICUP360 as
   required for programming mode.

   .. figure:: cn0397_switch.jpg
      :align: center
      :width: 500

      EVAL-ADICUP360 jumper and switch settings

#. Connect the **EVAL-CN0397-ARDZ** to the Arduino connectors **P2**, **P5**,
   **P6**, **P7**, **P8** of the **EVAL-ADICUP360** board.
#. Configure the chip select jumper (**P1**) on the EVAL-CN0397-ARDZ to the
   1-2 position.
#. Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB (P14).

ADICUP360 Source Code
~~~~~~~~~~~~~~~~~~~~~~

There are two ways to program the ADICUP360 with the CN0397 software:

#. Dragging and dropping the ``.bin`` file to the MBED drive.
#. Building, compiling, and debugging using CCES.

.. admonition:: Download

   `ADuCM360_demo_cn0397.bin (prebuilt)
   <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0397.bin>`__

   `ADuCM360_demo_cn0397 Source Code
   <https://github.com/analogdevicesinc/EVAL-ADICUP360/tree/master/projects/ADuCM360_demo_cn0397>`__

ADICUP360 Software Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following parameters can be configured:

- **DISPLAY_REFRESH** -- How often to refresh the output data (in milliseconds).
- **USE_CALIBRATION** -- Enable/disable system offset calibration on all 3
  channels. ``YES`` enables calibration, ``NO`` disables calibration.

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

Calibration Procedure (ADICUP360)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CN0397 needs to be calibrated before use to achieve best performance. A
system zero offset calibration cancels the offset for all channels.

If the calibration routine is enabled (check ``USE_CALIBRATION`` parameter), the
terminal window will display messages asking the user to cover the photodiodes
one at a time so calibration can be performed. With the photodiodes covered,
press **<ENTER>** and the next message will prompt to cover the next
photodiode.

.. figure:: cn0397_demo_2.png
   :align: center
   :width: 500

   Calibration procedure in terminal

Once all channels have been calibrated, the circuit is ready for use. The output
data will be available for each LED.

.. figure:: cn0397_demo_3.png
   :align: center
   :width: 500

   Light intensity measurement output

ADICUP3029 Demo
---------------

The **ADICUP3029_CN0397** is an RGB light detection demo project for the
EVAL-ADICUP3029 base board with the EVAL-CN0397-ARDZ shield, created using
Analog Devices CrossCore Embedded Studio.

General Description
~~~~~~~~~~~~~~~~~~~

The ADICUP3029_CN0397 project uses the EVAL-CN0397-ARDZ shield for visible
light detection. The :adi:`AD8500` op amp converts photodiode current output
into voltage using a transimpedance amplifier configuration. The :adi:`AD7798`
16-bit ADC converts the analog voltage into digital data for processing into
light intensity. The circuit utilizes RGB photodiodes from Everlight with peak
sensitivities at 620 nm (R), 550 nm (G), and 470 nm (B).

.. figure:: cn0397_adicup3029_board.png
   :align: center
   :width: 400

   EVAL-CN0397-ARDZ with EVAL-ADICUP3029

The 16-bit ADC data are received using the **SPI interface** of the
EVAL-ADICUP3029 board. The **UART interface** (9600 baud rate, 8-bit data
length) is used to send and receive data.

Light intensity and concentration are calculated using the same formulas as the
ADICUP360 demo.

.. figure:: cn0397_led_table.png
   :align: center
   :width: 500

   LED data table used for calculations

ADICUP3029 Demo Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware:

- EVAL-ADICUP3029
- EVAL-CN0397-ARDZ
- Micro USB to USB cable
- PC or laptop with a USB port

Software:

- ADICUP3029_CN0397 software (inside Sensor_Sw Pack 1.0.0 or higher)
- CrossCore Embedded Studio (2.6.0 or higher)
- ADuCM302x DFP (2.0.0 or higher)
- ADICUP3029 BSP (1.0.0 or higher)
- Android IoTNode App (optional)
- Serial Terminal Program (such as PuTTY or Tera Term)

ADICUP3029 Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Place the **(S5)** switch to "Wall/USB" and the **(S2)** switch to "USB".
#. Connect a jumper on **P1** between position **1-2** on EVAL-CN0397-ARDZ.
#. Plug the **EVAL-CN0397-ARDZ** shield into the **EVAL-ADICUP3029** board,
   using (P3), (P4), (P5), (P6), and (P7).
#. Plug in the micro USB cable into the **(P10)** USB port on the
   EVAL-ADICUP3029, and the other end into the PC or laptop.

ADICUP3029 Software Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the ``cn0397_app.h`` header file, you can configure the following parameters:

- **ADI_APP_DISPATCH_TIMEOUT** -- Defines how often data is sent over Bluetooth.
- **ADI_APP_USE_BLUETOOTH** -- Enables Bluetooth. If disabled, output is
  printed to console window in debug mode or terminal in release mode.

ADICUP3029 Calibration
~~~~~~~~~~~~~~~~~~~~~~~

The CN0397 needs to be calibrated before use. Calibration (enabled by default)
is performed by covering the photodiodes within the first 5 seconds of program
start to prevent any light from reaching them.

.. figure:: cn0397_calibration.png
   :align: center
   :width: 500

   Calibration output on ADICUP3029

Once all channels have been calibrated, the circuit is ready for use.

ADICUP3029 Output Modes
~~~~~~~~~~~~~~~~~~~~~~~~~

There are three different ways to visualize the data:

- CrossCore Embedded Studio Console Window (through semihosting)
- Serial Terminal Program (such as PuTTY or Tera Term)
- IoTNode Smart Device App

.. list-table::
   :header-rows: 1
   :widths: 35 25 40

   * - Data Output Destination
     - Connected to Debugger
     - Configuration File
   * - CCES Console Window
     - Yes
     - ADICUP3029_Debug.launch
   * - PC/Laptop Serial Terminal
     - No
     - ADICUP3029_Release.launch
   * - IoTNode Smart App
     - Yes
     - ADICUP3029_Debug.launch
   * - IoTNode Smart App
     - No
     - ADICUP3029_Release.launch

**Debug launch mode** is used when connected to the debugger. All outputs are
directed to the console window via semihosting. Data is also sent by default to
the IoTNode smart app (``ADI_APP_USE_BLUETOOTH = 1``).

.. figure:: cn0397_debug_ble.png
   :align: center
   :width: 500

   Debug mode with Bluetooth enabled

When ``ADI_APP_USE_BLUETOOTH`` is set to 0, only console output is displayed:

.. figure:: cn0397_debug_noble.png
   :align: center
   :width: 500

   Debug mode without Bluetooth

**Release launch mode** is used for running without the debugger. Console
output is redirected to UART. If Bluetooth is enabled, sensor data is sent to
the Android application. UART settings for release mode:

.. code-block:: none

   Select COM Port
   Baud rate: 9600
   Data: 8 bit
   Parity: none
   Stop: 1 bit
   Flow Control: none

.. figure:: cn0397_release_ble.png
   :align: center
   :width: 500

   Release mode with Bluetooth enabled

.. note::

   The Visible Light Detection Demo (ADICUP3029_CN0397) only works with the
   Android IoTNode App.

.. important::

   Do not try to connect directly (or pair) to the EVAL-ADICUP3029 from your
   phone. Open the IoTNode application, scan for nearby demos, and click on your
   demo to connect.

ADICUP3029 Source Code
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   `ADuCM3029_demo_cn0397.hex (prebuilt)
   <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0397.hex>`__

   `ADuCM3029_demo_cn0397 Source Code
   <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_cn0397>`__
