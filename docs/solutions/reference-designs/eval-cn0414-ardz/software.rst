.. _eval-cn0414-ardz software:

Software Guide
==============

The **ADuCM3029_demo_cn0414** project provides a solution to control a PLC or
DCS input system using the :adi:`EVAL-CN0414-ARDZ <CN0414>` and the
:adi:`EVAL-ADICUP3029`. It uses an ADC with four differential voltage channels
and four current channels, features low-power open-wire detection capabilities
and HART communication, and includes a 32 KB EEPROM for board identification.
The system is controlled via a command-line interface (CLI).

General Description
-------------------

The :adi:`AD4111` ADC is the core of the EVAL-CN0414-ARDZ shield. It provides
eight single or four differential voltage channels and four current channels.
In this application the input channels are configured as four differential
voltage channels plus the current channels. The application maintains eight
internal registers, one for each channel, that are updated periodically on a
timer interrupt with the latest conversion results. This way, on a single read,
the user can have the data on a channel without waiting for a conversion.

.. figure:: images/cn0414_timer_diagram.png
   :align: center

   Timer-Based Channel Update Mechanism

Alternatively, the user can request a burst read of up to 2000 samples returned
at the ADC output data rate.

The application uses the ADC's open-wire detection capabilities for the voltage
channels. When activated, this option also tracks the state of the channel
connection on every read and gives a warning when a channel is disconnected.

The EVAL-CN0414-ARDZ is HART capable. When this option is activated, the
current channels can be used to transmit or receive HART messages or send
command zero and receive the response. The system can receive messages
asynchronously using a GPIO interrupt.

The system also includes an EEPROM memory that communicates with the controller
via I2C and can be used to store data or identification information for the
board. The memory can uniquely identify the board in a system of up to four
similar boards (EVAL-CN0414-ARDZ or EVAL-CN0418-ARDZ) controlled by the same
EVAL-ADICUP3029.

Demo Requirements
-----------------

**Hardware**

- :adi:`EVAL-ADICUP3029` development board
- EVAL-CN0414-ARDZ evaluation board
- Micro-USB to USB cable
- PC or laptop with a USB port
- 24 V, 1 A limited power supply (optional)

**Software**

- `ADuCM3029_demo_cn0414 demo application
  <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_cn0414>`__
- CrossCore Embedded Studio (2.8.0 or higher)
- ADuCM302x DFP (3.2.0 or higher)
- ADICUP3029 BSP (1.1.0 or higher)
- Serial terminal program (such as PuTTY or Tera Term)

Setting up the Hardware
-----------------------

#. Connect the EVAL-CN0414-ARDZ board to the :adi:`EVAL-ADICUP3029`.
#. Set the jumpers into the standard position as shown below. This configuration
   works for single-board systems.

   .. figure:: images/cn0414_jumper_pos.jpg
      :align: center
      :width: 500

      Standard Jumper Position for Single Board

#. Connect a micro-USB cable to the P10 connector of the EVAL-ADICUP3029 and
   connect it to a computer. The final setup should look similar to the picture
   below.

   .. figure:: images/cn0414_hw_setup.jpg
      :align: center
      :width: 500

      Hardware Setup Example

Configuring the Software
-------------------------

The configuration parameters can be found in the ``config.h`` file.

**vref** -- Reference voltage of the ADC. If the internal reference is used,
this value must be 2.5 V. If an external reference is used, set this to the
value of the external reference.

.. list-table::
   :header-rows: 1

   * - Reference
     - vref Value
   * - Internal
     - 2.5
   * - External
     - Actual reference voltage

.. code-block:: c

   /* Reference voltage of the ADC */
   float vref = 2.5;

Outputting Data
---------------

Serial Terminal Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A serial terminal application is used to display data and interact with the
EVAL-CN0414-ARDZ through the EVAL-ADICUP3029's USB-to-UART interface.
Recommended terminal programs include `PuTTY <https://www.putty.org/>`__,
`Tera Term <https://ttssh2.osdn.jp/index.html.en>`__, or
`RealTerm <https://realterm.sourceforge.io/>`__.

Configure the serial terminal with the following settings:

- **COM Port**: Check your device manager after plugging in the USB cable to
  identify the assigned COM port
- **Baud rate**: 115200
- **Data bits**: 8
- **Parity**: None
- **Stop bits**: 1
- **Flow Control**: None

Additionally, enable **Implicit CR in every LF** and **Implicit LF in every
CR** in your terminal settings. Enable **local echo** and **local line editing**
so that you can see what you type and correct mistakes.

.. tip::

   If you see nothing in the serial terminal after connecting, try pressing
   the reset button on the EVAL-ADICUP3029 development board.

Available Commands
~~~~~~~~~~~~~~~~~~

Typing ``help`` or ``h`` after the initial calibration sequence displays the
list of available commands.

.. list-table::
   :header-rows: 1
   :widths: 10 60

   * - Command
     - Description
   * - **General Commands**
     -
   * - ``h``
     - Display available commands.
   * - ``stts``
     - Display parameters of the application.
   * - **Internal Register Commands**
     -
   * - ``r <chan>``
     - Display voltage or current on the selected channel.
   * - ``sur <rate>``
     - Change channel update rate (Hz). If larger than output data rate / 80,
       can cause unpredictable behavior.
   * - **HART Commands**
     -
   * - ``he``
     - Enable HART channel.
   * - ``hd``
     - Disable HART channel.
   * - ``hcc <chan>``
     - Select desired HART channel.
   * - ``ht <string>``
     - Transmit string through HART.
   * - ``hg``
     - Send the received buffer through UART connection.
   * - ``hcz <pbsize>``
     - Send command zero with the specified preamble size.
   * - ``hpt <byte>``
     - Send a byte in loop to test the physical connection.
   * - **ADC Commands**
     -
   * - ``arr <reg>``
     - Display value of ADC register at the given address.
   * - ``awr <reg> <val>``
     - Change value of ADC register at the given address.
   * - ``ags <ch> <nr>``
     - Get a specific number of samples from the given channel (max 2048).
   * - ``aso <sps>``
     - Set sample rate option.
   * - ``asf <filter>``
     - Set filter option.
   * - ``aep``
     - Enable post filter.
   * - ``adp <opt>``
     - Select post filter option.
   * - ``asp``
     - Reset controller, parameters, and faults.
   * - ``aowe``
     - Enable open-wire detection.
   * - ``aowd``
     - Disable open-wire detection.
   * - **EEPROM Commands**
     -
   * - ``de``
     - Discover EEPROM I2C addresses.

.. figure:: images/cn0414_console.png
   :align: center
   :width: 500

   Terminal Example Output

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for
the CN0414:

#. **Drag and Drop** -- Copy the ``.hex`` file to the DAPLINK drive. This is
   the easiest way to get started with the reference design. Using the drag
   and drop method, the software is a version that Analog Devices creates for
   testing and evaluation purposes.
#. **Build and Debug using CCES** -- Import the project into CrossCore Embedded
   Studio to customize the software. This approach allows you to change
   parameters and adapt the software to fit your needs, but requires
   downloading the CrossCore toolchain.

.. admonition:: Downloads

   - `Prebuilt CN0414 Hex File
     <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0414.hex>`__
   - `CN0414 Source Code
     <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_cn0414>`__

Using CrossCore Embedded Studio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The official tool promoted for use with the EVAL-ADICUP3029 is CrossCore
Embedded Studio (CCES). For detailed instructions on importing this demo
project into CCES and configuring a debug session, refer to the
EVAL-ADICUP3029 tools documentation.

Project Structure
-----------------

The program is composed of two main parts:

#. Board setup with initial values.
#. Main process.

.. figure:: images/cn0414_main_flowchart.png
   :align: center

   Main Flow Chart

Board setup initializes UART, SPI, and I2C communication and verifies if there
is an active EVAL-CN0414-ARDZ board connected by reading the AD4111 ID
register. The update timer for the internal channel registers is also
initialized here.

.. figure:: images/cn0414_board_setup_flow.png
   :align: center

   Board Setup Flow Chart

The main process routine implements the CLI and calls the commands input by the
user. This routine also checks the flags asserted in asynchronous events (the
update channel register flag, the HART received flag, and the floating channel
flags) and calls the appropriate handler methods. There is also a flag asserted
by the channel register update rate and the ADC output data rate. If the update
rate would be too close to the output data rate, the actual update rate might
slow down so the program can maintain all functionality. The update rate may
never be greater than or equal to the ADC output data rate divided by 8 (for
8 channels).

.. figure:: images/cn0414_process_flow.png
   :align: center

   Process Flow Chart

The flow chart below represents the way the channel registers are updated. Only
one channel is active at any one time (the channel that must be read).

.. figure:: images/cn0414_update_channel_flow.png
   :align: center

   Update Channel Flow Chart
