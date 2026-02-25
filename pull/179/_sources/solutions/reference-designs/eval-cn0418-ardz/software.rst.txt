.. _eval-cn0418-ardz software:

Software Guide
==============

The **ADuCM3029_demo_cn0418** project provides a solution to control a PLC or
DCS output system using the :adi:`EVAL-CN0418-ARDZ <CN0418>` and the
:adi:`EVAL-ADICUP3029`. It uses a DAC with four channels that can be configured
as either voltage or current output and is compatible with HART modem output to
enable HART communication on any channel. It includes a 32 KB EEPROM for board
identification and is controlled via a command-line interface (CLI).

General Description
-------------------

The EVAL-CN0418-ARDZ includes the :adi:`AD5755-1` quad-channel voltage and
current output DAC with dynamic power control, and the :adi:`AD5700-1` HART
modem, giving a completely isolated multiplexed HART analog output solution.

The application uses different software modules to deliver a CLI interface that
can be used to set any channel range or output and transmit and receive HART
messages on any of those channels. It uses SPI to communicate with the
AD5755-1, to read and write its registers. The channel code and range registers
can be set, as well as the RSET register. It can function in both voltage and
current mode.

The current mode is used with the AD5700-1 HART modem to transmit and receive
HART messages. The application can send command zero and then receive and
interpret the result. The receiving is done asynchronously through the use of
GPIO group interrupts featured by the ADuCM3029. The maximum baud rate of the
HART communication is 1200 bps and is implemented by a software UART. It
transmits and receives data bytes of 8 bits with one stop bit and one parity
bit, using odd parity.

The CLI is implemented using the hardware UART module in the ADuCM3029 and can
work up to 115200 baud rate.

.. figure:: images/cn0418_interaction_block.png
   :align: center

   CN0418 Software Interaction Block Diagram

Demo Requirements
-----------------

**Hardware**

- :adi:`EVAL-ADICUP3029` development board
- EVAL-CN0418-ARDZ evaluation board
- Micro-USB to USB cable
- PC or laptop with a USB port
- 24 V power source

**Software**

- ADuCM3029_demo_cn0418 application
- CrossCore Embedded Studio (2.8.0 or higher)
- ADuCM302x DFP (3.2.0 or higher)
- ADICUP3029 BSP (1.1.0 or higher)
- Serial terminal program (such as PuTTY or Tera Term)

Setting up the Hardware
-----------------------

#. Connect the EVAL-CN0418-ARDZ to the :adi:`EVAL-ADICUP3029`.
#. Set the jumpers into the standard position as shown below. This
   configuration works for single-board systems.

   .. figure:: images/cn0418_jumper_pos.jpg
      :align: center
      :width: 500

      Standard Jumper Position

#. Connect a micro-USB cable to the **P10** connector of the EVAL-ADICUP3029
   and connect it to a computer.
#. Connect the 24 V power source to the **P1** connector with the ground wire
   to pin 2 and the 24 V wire to pin 3. The final setup should look similar to
   the picture below.

   .. figure:: images/cn0418_final_setup.jpg
      :align: center
      :width: 500

      Final Hardware Setup

Configuring the Software
-------------------------

The software needs no configuration beyond the CLI UART baud rate, and HART
UART parity and number of bits. These can be accessed in the
``ADuCM3029_demo_cn0418.c`` file in the main function, but usually the default
values work best.

Outputting Data
---------------

Serial Terminal Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the serial terminal with the following settings:

- **Baud rate**: 115200
- **Data bits**: 8
- **Parity**: None
- **Stop bits**: 1
- **Flow Control**: None

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
   * - **DAC Commands**
     -
   * - ``dsr <chan> <range>``
     - Set range of a channel. Channels: cha, chb, chc, chd. Ranges: r05v,
       r010v, rmp5v, rmp10v, r420ma, r020ma, r024ma.
   * - ``dsv <chan> <voltage>``
     - Set voltage output on a channel (voltage range only). Use decimal point
       for fractional values.
   * - ``dsc <chan> <current>``
     - Set current output on a channel (current range only). Value in amperes.
   * - ``dsx <chan> <code>``
     - Set output on a channel using a 16-bit code (any range).
   * - ``dse <chan> <opt>``
     - Set the RSET of a channel. Options: int, ext.
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
   * - **EEPROM Commands**
     -
   * - ``de``
     - Discover EEPROM I2C addresses.

.. figure:: images/cn0418_terminal.png
   :align: center
   :width: 500

   Terminal Example Output

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for
the CN0418:

#. **Drag and Drop** -- Copy the ``.hex`` file to the DAPLINK drive. This is
   the easiest way to get started.
#. **Build and Debug using CCES** -- Import the project into CrossCore Embedded
   Studio to customize the software.

**Downloads:**

- `Prebuilt CN0418 Hex File
  <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0418.hex>`__
- `CN0418 Source Code
  <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_cn0418>`__

Project Structure
-----------------

The program is composed of two main parts:

#. Board setup with initial values.
#. Main process.

.. figure:: images/cn0418_main_flowchart.png
   :align: center

   Main Flow Chart

Board setup initializes UART, SPI, and I2C communication and verifies if there
is an active EVAL-CN0418-ARDZ board connected by reading the main control
register, memorizing the value, then trying to write and read that register to
verify an AD5755-1 device is present. If the device's presence is confirmed,
the register is reset to the initial value and the application continues.

.. figure:: images/cn0418_board_setup_flow.png
   :align: center

   Board Setup Flow Chart

After initialization, the application enters a loop where it memorizes UART
characters as they come from the CLI. If an ENTER character is detected, the
application determines if a command has been called and executes it. The
application also listens on the active HART channel and memorizes in a buffer
any transmission received.

.. figure:: images/cn0418_process_flow.png
   :align: center

   Process Flow Chart
