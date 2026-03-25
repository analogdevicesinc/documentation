.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0428

.. _eval-cn0428-ebz:

EVAL-CN0428-EBZ
================

Modular Water Quality Measurement Platform.

Overview
--------

:adi:`CN0428` is a modular sensing platform that allows the user to design a
flexible electrochemical water quality measurement solution. Its high level of
integration enables an electrochemical measurement platform applicable to a
variety of water quality probes including pH, oxidation reduction potential
(ORP), and conductivity cells. The system allows up to four probes to be
connected at one time for different water quality measurements.

.. figure:: cn0428_complete_setup.jpg
   :align: center
   :width: 600

   EVAL-CN0428-EBZ Complete Board Setup

.. figure:: cn0428_ebz.jpg
   :align: center
   :width: 400

   EVAL-CN0428-EBZ Water Sensor Board

Features
--------

- Capable of measuring pH, conductivity, temperature, and ORP of a solution.
- The board can be configured for customized measurements such as dissolved
  oxygen (DO) measurement, ion selective electrode (ISE) measurement, and
  other water quality factors.
- Up to four sensor boards can be connected simultaneously.
- Temperature can be measured on one or all sensor boards.

Boards Used
-----------

The water quality measurement system uses three boards:

- **EVAL-CN0428-EBZ** -- Water quality sensor board (up to four)
- **EVAL-M355-ARDZ-INT** -- Arduino shield board
- :adi:`EVAL-ADICUP3029` -- Host controller board

Required Equipment
------------------

**Hardware**

- :adi:`EVAL-ADICUP3029` circuit board
- EVAL-M355-ARDZ-INT Arduino-compatible platform
- :adi:`EVAL-CN0428-EBZ <CN0428>` water quality sensor board (up to four)
- PC with USB port (Windows 7 or higher)
- USB type A to USB micro cable
- Test solutions
- BNC connectorized probe (up to four)
- (Optional) RCA connectorized temperature probe (up to four)
- (Optional) Calibration buffers for probe calibration

**Software**

- Serial terminal software (PuTTY, Tera Term, or similar)
- ADuCM302x DFP
- CN0428 ADuCM355 firmware
- ADICUP3029 firmware

**Recommended Probes**

- `Cole-Parmer 100-series pH/Temperature Electrode
  <https://www.coleparmer.com/i/cole-parmer-100-series-replacement-ph-temperature-electrode/5920006>`__
- `Cole-Parmer 100-series Conductivity/Temperature Probe, K=1
  <https://www.coleparmer.com/i/cole-parmer-100-series-replacement-conductivity-temperature-probe-k-1/5920009>`__
- `Sensorex S550C-ORP Heavy-Duty ORP Sensor
  <https://sensorex.com/product/s550c-orp/>`__

Functional Block Diagram
-------------------------

.. figure:: functional_block_diag2.jpg
   :align: center

   CN0428 System Functional Block Diagram

Hardware Setup
--------------

Switch Configurations
~~~~~~~~~~~~~~~~~~~~~

**EVAL-CN0428-EBZ Sensor Board (S1 and S2)**

.. list-table::
   :header-rows: 1

   * - Desired Measurement
     - S1 Setting
     - S2 Setting
   * - pH, ORP, etc.
     - pH
     - n/a
   * - Conductivity, Impedance (100 ohm to 10 Mohm autoranging)
     - Z
     - Int
   * - Low current conductivity or impedance > 200 kohm
     - Z
     - HI-Z

**EVAL-M355-ARDZ-INT Shield Board**

- **S2** -- Set to **I2C** mode (default). UART mode enables direct
  communication between the shield and the :adi:`EVAL-ADICUP3029`.
- **S1** -- 4-position slide switch selects which channel is connected to the
  SWD programming port.

**EVAL-ADICUP3029 Board**

- **S5** -- Set to **Wall/USB** for USB power.
- **S2** -- Set to **USB** for serial communication to the PC.

Setup Procedure
~~~~~~~~~~~~~~~

#. Set switches on the :adi:`EVAL-ADICUP3029` (S5 to "Wall/USB", S2 to "USB")
   and EVAL-M355-ARDZ-INT (S2 to "I2C").
#. Mount the sensor board(s) onto the shield board using the included hardware
   (two bolts, two standoffs, and two nuts per sensor board).
#. Plug the shield board into the :adi:`EVAL-ADICUP3029`.
#. Connect the desired measurement probe to the sensor board.
#. Set the sensor board switches (S1 and S2) for the desired measurement.
#. Connect USB to supply power to all boards.
#. Set serial terminal software to 115200 bps and select the correct COM port.
#. Type ``help`` and press Enter to see available commands.

Software Setup
--------------

Programming the EVAL-ADICUP3029
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the :adi:`EVAL-ADICUP3029` to the PC via micro-USB. An orange LED
   should light on the board.
#. Install the
   `mbed Windows serial port driver <https://os.mbed.com/handbook/Windows-serial-configuration>`__.
#. Verify that a DAPLINK device appears under "This PC" in Windows File
   Explorer.
#. Copy the ``.hex`` firmware file onto the DAPLINK device to flash the
   firmware.
#. The DAPLINK device will momentarily disappear, then reappear. If a
   ``FAIL.TXT`` file is present, the download failed.
#. Perform a hard reset by unplugging and reconnecting the USB cable.

The firmware hex file can be obtained from the
`EVAL-ADICUP3029 GitHub repository
<https://github.com/analogdevicesinc/EVAL-ADICUP3029>`__.

Serial Terminal Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Open Device Manager and note the COM port for the USB Serial Device.
#. Open PuTTY (or similar) and configure:

   - **Connection type**: Serial
   - **Serial line**: COM port noted above
   - **Speed**: 115200

#. Under Terminal settings, configure local echo and line editing as needed.
#. Click **Open** to launch the terminal.

Available Commands
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Command
     - Description
   * - ``help``
     - Displays all available commands
   * - ``sensortype <type>``
     - Selects sensor type (ph, conductivity, ORP)
   * - ``measuretemp``
     - Measures and prints current temperature
   * - ``measuresensor``
     - Performs sensor measurement for configured type
   * - ``measureeis``
     - Performs EIS sweep and estimates sensor health
   * - ``printhealth``
     - Prints sensor health from last EIS measurement
   * - ``printtemp``
     - Prints last measured temperature
   * - ``printconfig``
     - Prints current configuration
   * - ``printserialnumber``
     - Prints the unique board ID
   * - ``enabletemp <en>``
     - Enables (1) or disables (0) temperature measurement
   * - ``enablehizmode <en>``
     - Enables (1) or disables (0) high impedance TIA
   * - ``renamesensor <name>``
     - Renames sensor channel (max 16 characters)
   * - ``switchsensor <site>``
     - Switches to sensor board at site 1, 2, 3, or 4

Documents
---------

- `ADuCM355 Data Sheet
  <https://www.analog.com/media/en/technical-documentation/data-sheets/ADuCM355.pdf>`__
- :adi:`CN0428 Circuit Note <CN0428>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0428-EBZ Design & Integration Files
   <https://www.analog.com/cn0428-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Software
--------

- `EVAL-CN0428-EBZ Firmware Source Code
  <https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/cn0428.html>`__
- `EVAL-ADICUP3029 Source Code for CN0428
  <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/main/projects/ADuCM3029_demo_cn0428_cn0429>`__

Additional Information
----------------------

- :adi:`ADuCM355 Product Page <ADUCM355>`
- :adi:`CN0428 Circuit Note <CN0428>`
- :adi:`EVAL-ADICUP3029 Product Page <EVAL-ADICUP3029>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
