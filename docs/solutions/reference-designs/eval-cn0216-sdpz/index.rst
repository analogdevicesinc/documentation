.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0216

.. _eval-cn0216-sdpz:

EVAL-CN0216-SDPZ
=================

Precision Weigh Scale Signal Conditioning System.

Overview
--------

:adi:`CN0216` is a precision weigh scale signal conditioning system. It uses
the :adi:`AD7791`, a low power buffered 24-bit sigma-delta ADC along with two
external :adi:`ADA4528-1` zero-drift amplifiers. This solution allows for high
DC gain with a single supply.

Ultralow noise, low offset voltage, and low drift amplifiers are used at the
front end for amplification of the low-level signal from the load cell. The
circuit yields 15.3-bit noise-free code resolution for a load cell with a
full-scale output of 10 mV.

This circuit allows great flexibility in designing a custom low-level signal
conditioning front end that gives the user the ability to easily optimize the
overall transfer function of the combined sensor-amplifier-converter circuit.
The :adi:`AD7791` maintains good performance over the complete output data
range, from 9.5 Hz to 120 Hz, which allows it to be used in weigh scale
applications that operate at various low speeds.

.. figure:: cn0216_simplified_schematic.png
   :align: center

   CN0216 Simplified Schematic

The EVAL-CN0216 circuit board is available in three form factors:

- **EVAL-CN0216-SDPZ** -- connects to the :adi:`EVAL-SDP-CB1Z` System
  Demonstration Platform via 120-pin connector
- **EVAL-CN0216-ARDZ** -- Arduino shield form factor for use with Arduino Uno
  or :adi:`EVAL-ADICUP360`
- **EVAL-CN0216-PMDZ** -- Pmod form factor

.. figure:: cn0216_board_photo.png
   :align: center
   :width: 500px

   EVAL-CN0216-ARDZ Board (Rev C)

.. important::

   The EVAL-CN0216-ARDZ is powered from the **VIN** connector on the Arduino
   Uno header. The bridge drive voltage requires more than 5 V to power the
   bridge. Therefore an external DC power supply (7 V to 12 V) must be
   connected through the DC power connector for proper functionality. The board
   will not work properly if powered only from USB.

Evaluation with SDP-B Controller Board
---------------------------------------

Required Equipment
~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-SDP-CB1Z` Controller Board (SDP-B Board)
- :adi:`EVAL-CN0216-SDPZ` Evaluation Board (CN-0216 Board)
- :adi:`EVAL-CFTL-6V-PWRZ` (+6 V Power Supply) or equivalent
- CN0216 Evaluation Software
- PC with USB Type A port (Windows XP SP2 32-bit or later, 1 GHz processor,
  512 MB RAM, 500 MB available disk space)
- USB Type A to USB Type Mini-B cable
- Tedea-Huntleigh Model 1042 Load Cell (or any compatible 4-wire or 6-wire
  load cell)

.. note::

   Any 4-wire or 6-wire load cells can be used with the CN-0216 Board. This
   guide was written with the Tedea-Huntleigh Model 1042 in mind.

General Setup
~~~~~~~~~~~~~

- The :adi:`EVAL-CN0216-SDPZ` (CN-0216 Board) connects to the
  :adi:`EVAL-SDP-CB1Z` (SDP-B Board) via the 120-pin connector.
- The :adi:`EVAL-CFTL-6V-PWRZ` (+6 V DC Power Supply) powers the CN-0216
  Board via the DC barrel jack.
- The SDP-B Board connects to the PC via the USB cable.
- The load cell connects to the CN-0216 Board via the 8-pin header.

.. figure:: cn0216_test_setup.png
   :align: center

   EVAL-CN0216-SDPZ Test Setup with SDP-B Board

Installing the Software
~~~~~~~~~~~~~~~~~~~~~~~~

1. Extract the file **CN0216 Eval Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the CN0216 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\CN0216\`` and
      all National Instruments products to
      ``C:\Program Files\National Instruments\``.

   .. figure:: cn0216_install_step1.png
      :align: center

      CN0216 Software Installation Wizard

2. Click **Next** to view the installation review page.

   .. figure:: cn0216_install_step2.png
      :align: center

      Installation Review

3. Click **Next** to start the installation.

   .. figure:: cn0216_install_step3.png
      :align: center

      Installation Progress

4. Upon completion of the CN0216 Evaluation Software installation, the
   installer for the ADI SDP Drivers will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: cn0216_install_step4.png
      :align: center

      ADI SDP Driver Installation

5. Press **Next** to set the installation location for the SDP Drivers.

   .. tip::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\Drivers``.

   .. figure:: cn0216_install_step5.png
      :align: center

      SDP Driver Installation Path

6. Press **Next** to install the SDP Drivers and complete the installation of
   all software. Click **Finish** when done.

   .. figure:: cn0216_install_step6.png
      :align: center

      Installation Complete

Connecting the Hardware
~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect the load cell to the **8-pin header** of the EVAL-CN0216-SDPZ
   (CN-0216 Board) as depicted below.

   .. note::

      If a different load cell is used other than the Tedea-Huntleigh Model
      1042, the wiring schematic will be different.

.. figure:: cn0216_wiring_table.png
   :align: center

   Load Cell Wiring Pin Assignment

.. figure:: cn0216_wiring_schematic.png
   :align: center

   Tedea-Huntleigh Model 1042 Wiring Schematic

Using the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software Control and Indicator Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0216_software_main.png
   :align: center

   CN0216 Evaluation Software -- Main Tab

.. figure:: cn0216_software_calibrate.png
   :align: center

   CN0216 Evaluation Software -- Calibrate System Tab

The software interface provides the following controls and indicators:

1. **Connect/Reconnect Button** -- Establishes a USB connection between the
   SDP-B Board and the CN-0216 Board. A connection must be made before using
   any other software features.

2. **Run Button** -- Starts collecting conversion data and displays
   acquisitions in the chart.

3. **Stop Button** -- Stops data collection from the CN-0216 Board.

4. **Clear Chart Button** -- Clears all collected data from the chart history.

5. **Control Tabs**:

   - *Main* -- Displays the data collection chart.
   - *Calibrate System* -- Displays system configuration settings.

6. **Current Weight Numerical Indicator** -- Displays the mass (in grams)
   on the load cell.

7. **Chart Controls** -- Allow zooming in, zooming out, and panning through
   the collected data.

8. **Select Units Radio Buttons** -- Determines the Y-axis units of the
   data displayed in the chart.

9. **System Status String Indicator** -- Displays a message detailing the
   current state of the software.

10. **System Status LED Indicator** -- Displays the current state of the
    software as a colored LED:

    - |led_inactive| Inactive
    - |led_busy| Busy
    - |led_error| Error

.. |led_inactive| image:: cn0216_led_inactive.png
.. |led_busy| image:: cn0216_led_busy.png
.. |led_error| image:: cn0216_led_error.png

11. **Calibration Weight Numerical Control** -- Set this to the weight of the
    object used to calibrate the load cell.

12. **Calibrate Button** -- Initiates the calibration of the load cell.

13. **ADC Mode Radio Buttons** -- Sets the mode of the :adi:`AD7791`. The
    default value is *Unbuffered Mode*:

    - *Buffered Mode* -- Turns the on-chip analog input channel buffer ON.
    - *Unbuffered Mode* -- Turns the on-chip analog input channel buffer OFF.

14. **ADC Channel Select Radio Buttons** -- Selects the analog input channel
    of the :adi:`AD7791` for conversion. The default value is *AIN(+)-AIN(-)*:

    - *AIN(+)-AIN(-)* -- Normal operation.
    - *AIN(-)-AIN(-)* -- Shorts the analog input channels.
    - *Vdd Monitor* -- Monitors the Vdd pin voltage. The voltage is attenuated
      by 5 and converted using an internal 1.17 V reference.

15. **Update Rate Radio Buttons** -- Changes the output word rate of the
    :adi:`AD7791`. The default value is *9.5 Hz*.

16. **Configure ADC Button** -- Applies the current ADC Mode, Channel Select,
    and Update Rate settings to the :adi:`AD7791`.

Establishing a USB Connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Follow the instructions to properly install the software and connect the
   hardware as described in the previous sections.
2. Open the file named **CN0216.exe** in the installation directory.

   .. note::

      If the software was installed to the default location it will be found at
      ``C:\Program Files\Analog Devices\CN0216\CN0216.exe``.

3. Click the **Connect/Reconnect Button**. A window with a progress bar will
   load.

   .. figure:: cn0216_software_wait.png
      :align: center

      SDP-B Board Connection Progress

4. Upon success, the System Status String Indicator will display *SDP Board
   Ready to Acquire Data*.

Capturing Data
^^^^^^^^^^^^^^

1. Establish a USB Connection Link.
2. Click the **Run Button**.
3. Click the **Stop Button** when acquisition is complete.

Calibrating the Load Cell
^^^^^^^^^^^^^^^^^^^^^^^^^

1. Establish a USB Connection Link.
2. Click the **Calibrate System** control tab.
3. Set the **Calibration Weight Numerical Control** to the weight (in grams)
   of the object to be used for calibration.
4. Place the calibration weight on the load cell.
5. Click the **Calibrate Button** and wait for calibration to complete.

   .. figure:: cn0216_calibrate_wait.png
      :align: center

      Calibration in Progress

6. Remove the calibration weight when prompted to do so.

   .. figure:: cn0216_calibrate_continue.png
      :align: center

      Calibration Prompt to Remove Weight

7. Click the **Continue Button**.
8. Wait for the second calibration phase to complete.

Evaluation with EVAL-ADICUP360
-------------------------------

The **ADuCM360_demo_cn0216** is a weigh scale measurement demo project for the
:adi:`EVAL-ADICUP360` base board with the EVAL-CN0216-ARDZ shield, created
using the CrossCore Embedded Studios IDE.

The CN0216 circuit translates resistance changes on the bridge into very small
voltages. The bridge is excited by a regulated 5 V, which determines the
full-scale range of the bridge output. Those values are passed through very low
noise, auto-zero amplifiers to remove as many error sources as possible before
being gained up to levels compatible with the ADC. The 24-bit ADC value is
received via the SPI interface of the EVAL-ADICUP360 board.

.. figure:: cn0216_hw_stacked.jpg
   :align: center
   :width: 550px

   EVAL-CN0216-ARDZ Shield Stacked on EVAL-ADICUP360 Board

Demo Requirements (ADICUP360)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware:

- EVAL-ADICUP360
- EVAL-CN0216-ARDZ
- Precision weight set
- 4-wire or 6-wire Wheatstone bridge weigh scale
- Micro USB to USB cable
- PC or laptop with a USB port

Software:

- ADuCM360_demo_cn0216 software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM36x DFP (1.0.2 or higher)
- CMSIS ARM Pack (4.3.0 or higher)
- Serial terminal program (such as PuTTY or Tera Term)

Setting Up the Hardware (ADICUP360)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Set the jumpers and switches on the EVAL-ADICUP360 as shown below. The
   important jumpers/switches are highlighted in red.

   .. figure:: cn0216_hw_config.png
      :align: center
      :width: 500px

      EVAL-ADICUP360 Jumper Configuration for CN0216

2. Connect the **EVAL-CN0216-ARDZ** to the Arduino connectors **P2, P5, P6,
   P7, P8** of the **EVAL-ADICUP360** board.
3. Connect the weigh scale to the EVAL-CN0216-ARDZ via the sensor connector
   (see the :ref:`cn0216_sensor_connector_section` section for pinout details).
4. Connect an acceptable 7 V to 12 V power supply into the **P11** barrel jack
   of the EVAL-ADICUP360.

.. important::

   It is extremely important to plug in an acceptable power supply to the
   barrel jack **P11** for the EVAL-CN0216-ARDZ. The boards will not work if
   you try only to power from the DEBUG_USB or the USER_USB.

5. Plug the USB cable from the PC to the EVAL-ADICUP360 via the Debug USB
   (P14).

Obtaining the Source Code (ADICUP360)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways to program the ADICUP360 with the CN0216 software:

1. **Drag and drop** the ``.bin`` file to the MBED drive -- this is the
   easiest way to get started with the reference design.
2. **Build, compile, and debug** using CrossCore Embedded Studio (CCES) --
   allows customization of software parameters.

The software for the ADuCM360_demo_cn0216 demo can be found at:

- `Prebuilt CN0216 Bin File
  <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases>`__
- `ADuCM360_demo_cn0216 Source Code
  <https://github.com/analogdevicesinc/EVAL-ADICUP360/tree/master/projects/ADuCM360_demo_cn0216>`__

Configuring the Software (ADICUP360)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the reference voltage in the ``AD7791.h`` file (in volts):

.. code-block:: c

   #define VREF       5         /* The board default value is 5V */

Configure the full-scale calibration weight in the ``CN0216.h`` file
(in grams):

.. code-block:: c

   #define CAL_WEIGHT     1000

Serial Terminal Output (ADICUP360)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Flash the program to the EVAL-ADICUP360.
2. Switch the USB cable from the DEBUG USB (P14) to the USER USB (P13).
3. Configure the serial terminal program with the following settings:

.. code-block:: none

   Baud rate:    9600
   Data:         8 bit
   Parity:       none
   Stop:         1 bit
   Flow Control: none

At the start of the project, a calibration of the upper and lower input range
of the weigh scale is performed to remove both offset and gain errors, providing
the most accurate measurements possible:

- The program will prompt for a **zero-scale calibration** -- ensure nothing is
  on the scale, then press **<ENTER>** (takes approximately 5 seconds).
- Next, the program will prompt to add the **calibration weight** to the scale,
  then press **<ENTER>** for the full-scale calibration (approximately
  5 seconds). Measurements are averaged over 100 samples and stored as
  calibration coefficients.
- Once calibration is complete, weight measurements are displayed each time
  **<ENTER>** is pressed.

.. figure:: cn0216_putty_output.png
   :align: center
   :width: 550px

   Serial Terminal Output Showing Weight Measurements

Evaluation with Arduino Uno
-----------------------------

The **CN0216_example** is a weigh scale measurement demo project for the
Arduino Uno base board with the EVAL-CN0216-ARDZ shield, created using the
Arduino IDE.

Demo Requirements (Arduino)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware:

- Arduino Uno Rev 3
- EVAL-CN0216-ARDZ
- 4-wire or 6-wire Wheatstone bridge weigh scale
- Type B to Type A USB cable
- PC or laptop with a USB port

Software:

- CN0216_example sketch
- Arduino IDE

Setting Up the Hardware (Arduino)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Plug the **EVAL-CN0216-ARDZ** shield on top of the **Arduino Uno** by
   matching up the **POWER, ANALOG, DIGI0, DIGI1** connectors. The boards
   should only plug together one way, preventing reverse connections.
2. Connect the weigh scale to the EVAL-CN0216-ARDZ via the sensor connector
   (see the :ref:`cn0216_sensor_connector_section` section for pinout details).
3. Connect an acceptable 7 V to 12 V power supply into the power jack of the
   Arduino Uno.

.. important::

   It is extremely important to plug in an acceptable power supply to the
   power jack for the EVAL-CN0216-ARDZ. The boards will not work if you try
   only to power from USB.

4. Plug the Type B USB cable into the USB port on the Arduino Uno and the
   other end into the PC or laptop.

Obtaining the Source Code (Arduino)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The source code for the CN0216_example can be found at:

- `CN0216_example at GitHub
  <https://github.com/analogdevicesinc/arduino/tree/master/Arduino%20Uno%20R3/examples/CN0216_example>`__

Serial Terminal Output (Arduino)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the serial terminal with the following settings:

.. code-block:: none

   Baud rate:    9600
   Data:         8 bit
   Parity:       none
   Stop:         1 bit
   Flow Control: none

The calibration procedure and output format are the same as described in the
ADICUP360 section above.

.. _cn0216_sensor_connector_section:

EVAL-CN0216-ARDZ Hardware Details
----------------------------------

.. _cn0216_connectors_section:

Connectors and Jumper Configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0216_connectors.png
   :align: center
   :width: 500px

   EVAL-CN0216-ARDZ Connector and Jumper Locations

Sensor Connector
^^^^^^^^^^^^^^^^^

The sensor connector accepts an 8-pin header for load cell wiring.

.. figure:: cn0216_sensor_connector.png
   :align: center
   :width: 300px

   Sensor Connector Pinout

.. list-table:: Sensor Connector Pin Assignment
   :header-rows: 1
   :align: center

   * - Pin Number
     - Pin Function
   * - Pin 1
     - Not Used
   * - Pin 2
     - - Excitation
   * - Pin 3
     - + Signal
   * - Pin 4
     - - Sense
   * - Pin 5
     - + Sense
   * - Pin 6
     - - Signal
   * - Pin 7
     - + Excitation
   * - Pin 8
     - Not Used

.. figure:: cn0216_wiring_schematic.png
   :align: center

   Tedea-Huntleigh Model 1042 Wiring to Sensor Connector

REF SEL / Bridge Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These jumpers allow the circuit to be configured for use with 4-wire or 6-wire
load cells.

.. note::

   Any 4-wire or 6-wire load cells can be used with the EVAL-CN0216-ARDZ. The
   Tedea-Huntleigh Model 1042 load cell was used during testing.

**6-Wire Configuration:**

.. figure:: cn0216_ref_sel_6wire.png
   :align: center
   :width: 100px

   P1/P2 Jumper Position for 6-Wire Load Cell

- **P1** -- Connects ADC REFIN+ to Sensor +Sense pin
- **P2** -- Connects ADC REFIN- to Sensor -Sense pin

**4-Wire Configuration:**

.. figure:: cn0216_ref_sel_4wire.png
   :align: center
   :width: 100px

   P1/P2 Jumper Position for 4-Wire Load Cell

- **P1** -- Connects ADC REFIN+ to 5 V supply
- **P2** -- Connects ADC REFIN- to GND

Chip Select
^^^^^^^^^^^^

These jumpers allow changing the pin mapping of the :adi:`AD7791` chip select
line to different Arduino digital pins.

.. figure:: cn0216_cs_sel_pin10.png
   :align: center
   :width: 100px

   CS -- Arduino Digital Pin 10

.. figure:: cn0216_cs_sel_pin9.png
   :align: center
   :width: 100px

   CS -- Arduino Digital Pin 9

.. figure:: cn0216_cs_sel_pin8.png
   :align: center
   :width: 100px

   CS -- Arduino Digital Pin 8

.. note::

   If using an EVAL-CN0216-ARDZ board prior to Rev C, install a 0-ohm resistor
   to resistor pads R7, R8, or R9 instead:

   - **R7** -- Arduino Digital Pin 8
   - **R8** -- Arduino Digital Pin 9
   - **R9** -- Arduino Digital Pin 10

Documents
---------

- :adi:`CN0216 Circuit Note <CN0216>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0216-SDPZ Design & Integration Files
   <https://www.analog.com/cn0216-designsupport>`__

   `EVAL-CN0216-ARDZ Design & Integration Files
   <https://www.analog.com/cn0216-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Gerber Files
   - Allegro/PADS Board File

Additional Information
----------------------

- :adi:`AD7791 Product Page <AD7791>`
- :adi:`ADA4528-1 Product Page <ADA4528-1>`
- :adi:`ADA4528-2 Product Page <ADA4528-2>`
- :adi:`EVAL-SDP-CB1Z Product Page <EVAL-SDP-CB1Z>`
- :adi:`EVAL-ADICUP360 Product Page <EVAL-ADICUP360>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
