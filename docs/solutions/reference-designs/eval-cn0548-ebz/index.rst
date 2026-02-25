.. _eval-cn0548-ebz:

EVAL-CN0548-ARDZ
=================

Isolated Current and Voltage Measurement System.

Overview
--------

:adi:`CN0548` is a complete, isolated current and voltage measurement system
for industrial, telecommunications, instrumentation, and automated test
equipment (ATE) applications. The system is galvanically isolated from the host
controller and tolerates up to +/-250 V between the host computer and
measurement system grounds.

When paired with the :adi:`EVAL-ADICUP3029` and open-source firmware,
application software communicates with the CN0548 over the industry-standard
Industrial Input/Output (IIO) libiio library.

.. figure:: cn0548_high_resolution_photo_3d_view.jpg
   :align: center

   EVAL-CN0548-ARDZ board

Simplified Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: block_diagram.png
   :align: center

   CN0548 block diagram

Features
--------

- Absolute maximum input rating: 80 V, 14 A
- Configurable voltage and current settings
- 16-bit ADC resolution with adjustable output data rate
- SPI digital output
- Galvanic isolation from host controller
- 3.3 V and 5 V compatible
- Arduino form factor
- Chip select remappable (stackable with other shields)

Required Equipment
------------------

**Hardware**

- EVAL-CN0548-ARDZ shield
- :adi:`EVAL-ADICUP3029` controller board
- Micro-USB to USB cable
- PC or laptop with USB port

**Software**

- Pre-built HEX file (unipolar or bipolar variant)
- Python 3.7 or later
- Python IDE (Visual Studio Code, Anaconda, or PyCharm)

Input Configuration
--------------------

.. figure:: cn0548_high_resolution_photo.jpg
   :align: center

   EVAL-CN0548-ARDZ board layout

Input Mode Ranges
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Mode
     - Minimum Input
     - Maximum Input
   * - Unipolar voltage
     - 0 V
     - 80 V
   * - Bipolar voltage
     - -40 V
     - 40 V
   * - Unidirectional current
     - 0 A
     - 14 A
   * - Bidirectional current
     - -10 A
     - 10 A

Polarity and Current Direction Jumpers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **P12, P13** -- Configure input current setting (unidirectional: GND,
  bidirectional: 2.048 V)
- **P7, P14** -- Configure input voltage setting (unipolar: GND,
  bipolar: 2.048 V)

.. figure:: mode_jumper.png
   :align: center

   Voltage polarity and current direction jumper locations

Voltage Range Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: gain_jumper.png
   :align: center

   Voltage range jumper locations

.. list-table::
   :header-rows: 1

   * - Max Range
     - P1
     - P3
     - P10
     - P8
     - P9
     - P11
   * - 80 V
     - Open
     - Vin-
     - Vin+
     - Open
     - Vin+
     - Vin-
   * - 40 V
     - Vin+
     - Open
     - Open
     - Vin-
     - Open
     - Open
   * - 27 V
     - Vin-
     - Open
     - Vin+
     - Vin+
     - Open
     - Vin-
   * - 20 V
     - Open
     - Vin+
     - Open
     - Open
     - Vin-
     - Open
   * - 16 V
     - Open
     - Open
     - Vin+
     - Open
     - Open
     - Vin-

.. figure:: gain_config.png
   :align: center

   Voltage range configuration lookup table

Chip Select Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default chip select uses jumper **P15** (shunted). The CS can be remapped
for stacking with other Arduino shields.

.. figure:: chip_select.png
   :align: center

   Chip select jumper configuration

Hardware Setup
--------------

#. Attach the EVAL-CN0548-ARDZ shield to the :adi:`EVAL-ADICUP3029`.
#. Connect a micro-USB cable to the **P10** connector of the
   :adi:`EVAL-ADICUP3029` and to the computer.

Software Setup
--------------

Flashing Firmware
~~~~~~~~~~~~~~~~~~

#. Configure the :adi:`EVAL-ADICUP3029` on-board switches as specified in the
   documentation.
#. Connect the :adi:`EVAL-ADICUP3029` to the PC via micro-USB cable.
#. Verify that a **DAPLINK** drive appears in the file explorer.
#. Download the appropriate ``.hex`` file (unipolar or bipolar variant) from
   the `EVAL-ADICUP3029 GitHub repository
   <https://github.com/analogdevicesinc/EVAL-ADICUP3029>`__.
#. Drag and drop the ``.hex`` file onto the DAPLINK drive.
#. Wait for the DS2 red LED to stop blinking and stay on.
#. Disconnect and reconnect the :adi:`EVAL-ADICUP3029`.

Available pre-built hex files:

- ``ADuCM3029_demo_cn0548_demo_unipolar.hex``
- ``ADuCM3029_demo_cn0548_demo_bipolar.hex``

CCES Project Development
~~~~~~~~~~~~~~~~~~~~~~~~~~

The CrossCore Embedded Studio (CCES) project allows editing the software to fit
specific requirements. Import the project into CCES to generate custom ``.hex``
files or use debug sessions.

.. figure:: cces.png
   :align: center

   CCES code snippet showing polarity and gain attribute configuration

PyADI-IIO
~~~~~~~~~~~

The :adi:`PyADI-IIO <pyadi-iio>` Python abstraction module provides
device-specific APIs built on top of the current libiio Python bindings,
enabling easier hardware interaction.

Python Application
~~~~~~~~~~~~~~~~~~~

The CN0548 Python script (``CN0548_simple_plot.py``) provides:

- Graphic jumper configuration guide
- Real-time numerical readings display
- Data logging with automatic CSV generation
- Real-time plotting with tracking and non-tracking modes
- Session memory for reusing previous configurations
- Automatic port detection

Running the Example
~~~~~~~~~~~~~~~~~~~~

#. Download ``CN0548_simple_plot.py`` from the `EVAL-ADICUP3029 GitHub
   repository <https://github.com/analogdevicesinc/EVAL-ADICUP3029>`__.
#. Run the script:

   .. code-block:: bash

      python CN0548_simple_plot.py

#. Review safety reminders and press Enter to continue.
#. Choose to create a new configuration or reuse a previous session.
#. Specify voltage and current input types (unipolar/bipolar,
   unidirectional/bidirectional).
#. Configure software parameters via the prompts.
#. Specify the :adi:`EVAL-ADICUP3029` connection port.
#. Begin continuous readings.

Display modes:

- **Tracking mode** -- Shows all data points.
- **Non-tracking mode** -- Displays the last 50 samples.

Data Logging
~~~~~~~~~~~~~

CSV files are created automatically with the naming format
``CN0548_[timestamp]``. Data is written continuously and survives premature
termination.

Session Memory
~~~~~~~~~~~~~~~

A ``session_record`` text file stores all user configurations for quick reuse.
The file is unencrypted and manually editable. The program validates
configuration validity on reload.

.. note::

   ADC polarity configuration affects bit resolution: unipolar mode provides
   full resolution, while bipolar mode provides n-1 bits. Consult the
   AD7798/AD7799 data sheet before customizing the HEX file.

Documents
---------

- :adi:`CN0548 Circuit Note <CN0548>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0548-ARDZ Design & Integration Files
   <https://www.analog.com/cn0548-DesignSupport>`__

   - Schematics
   - Bill of Materials
   - Gerber Files
   - Allegro Project

Additional Information
----------------------

- :adi:`EVAL-ADICUP3029 Product Page <EVAL-ADICUP3029>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
