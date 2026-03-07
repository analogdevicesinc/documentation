PLC Arduino Shield Output Demo
==============================

The **ADuCM3029_demo_cn0418** project provides a solution to control a **PLC** or **DCS** output system using the **EVAL-CN0418-ARDZ** and the **EVAL-ADICUP3029**. It uses a DAC with 4 channels that can be configured as either voltage or current output and is compatible with **HART** modem output to enable **HART** communication on any channel. It has a 32kb EEPROM memory that can also be used to identify the board and is controlled via a command line interface (CLI).

General Description/Overview
----------------------------

The **EVAL-CN0418-ARDZ** is an Arduino compatible shield includes a **AD5755-1** (quad channel voltage and current output DAC with dynamic power control) and the **AD5700-1 HART modem**, to give a completely isolated multiplexed **HART** analog output solution.

The **ADuCM3029_demo_cn0418** application uses different software modules to deliver a CLI interface that can be used to set any channel range or output and transmit and receive **HART** messages on any of those channels. It uses SPI to communicate with the **AD5755-1**, to read and write its registers. The channle code and range registers can be set as well as the RSET register. It can function both in voltage and current mode.

The current mode is used with the **AD5700-1 HART modem** to transmit and receive **HART** messages. The application can send command zero and then receive and interpret the result. The receiving is done asynchronous through the use of GPIO group interrupts featured by the **ADuCM3029**. The maximum baudrate of the **HART** communication is 1200 and is implemented by a **software UART**. It transmits and receives data bytes of 8 bits with one stop bit and one parity bit, using odd parity.

The **CLI** is implemented using the hardware UART module in the **ADuCM3029** and can work up 115200 baudrate.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/plc_out_interaction_block_diagram.png
   :alt: CN0418 connection block diagram
   :align: center

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-CN0418-ARDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port
   -  24V source

-  Software

   -  ADuCM3029_demo_cn0418 software
   -  CrossCore Embedded Studio (2.8.0 or higher)
   -  ADuCM302x DFP (3.2.0 or higher)
   -  ADICUP3029 BSP (1.1.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

-  Connect **EVAL-CN0418-ARDZ** to the **EVAL-ADICUP3029**.
-  Set the jumpers into the position shown below. This is the standard position and only works for one board systems.

|image1|

-  Connect a micro-USB cable to **P10** connector of the **EVAL-ADICUP3029** and connect it to a computer.
-  Connect the 24V power source to the **P1** connector with the ground wire to pin 2 and 24V wire to pin 3. The final setup should look similar to the picture below.

|image2|

Configuring the Software
------------------------

The software needs no configuration beyond the CLI UART baudrate, and HART UART parity and number of bits. These can be accessed in the ADuCM3029_demo_cn0418.c file in the main function, but usually the default values work best.

Outputting Data
---------------

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#serial_terminal_setup>`_


Available Commands
~~~~~~~~~~~~~~~~~~

Typing help or h after initial calibration sequence will display the list of commands and their short versions. Bellow is the short command list:

+------------------+------------------------------------------------------------------------------------------+
| Command          | Description                                                                              |
+==================+==========================================================================================+
| General commands |                                                                                          |
+------------------+------------------------------------------------------------------------------------------+
| *h*              | Display available commands.                                                              |
+------------------+------------------------------------------------------------------------------------------+
| *stts*           | Display parameters of the application.                                                   |
+------------------+------------------------------------------------------------------------------------------+
| DAC commands     |                                                                                          |
+------------------+------------------------------------------------------------------------------------------+
| *dsr*            | Set range of a channel.                                                                  |
|                  | <*chan*> = channel to be set.                                                            |
|                  | Available channel options are: cha, chb, chc, chd.                                       |
|                  | <*range*> = chosen range for the channel.                                                |
|                  | Available options are:                                                                   |
|                  | - r05v = range from 0 to 5 volts;                                                        |
|                  | - r010v = range from 0 to 10 volts;                                                      |
|                  | - rmp5v = range form -5 to +5 volts;                                                     |
|                  | - rmp10v = range from -10 to +10 volts;                                                  |
|                  | - r420ma = range from 4 to 20 mili-amperes;                                              |
|                  | - r020ma = range from 0 to 20 mili-amperes;                                              |
|                  | - r024ma = range from 0 to 24 mili-amperes.                                              |
+------------------+------------------------------------------------------------------------------------------+
| *dsv*            | Set voltage output on a channel. Only works if the channel is set to a voltage range.    |
|                  | <chan> = channel to update.                                                              |
|                  | Available channel options are: cha, chb, chc, chd.                                       |
|                  | <voltage> = voltage level expressed in volts. Use decimal point for fractional values.   |
+------------------+------------------------------------------------------------------------------------------+
| *dsc*            | Set current output on a channel. Only works if the channel is set to a current range.    |
|                  | <chan> = channel to update.                                                              |
|                  | Available channel options are: cha, chb, chc, chd.                                       |
|                  | <current> = current level expressed in amperes. Use decimal point for fractional values. |
+------------------+------------------------------------------------------------------------------------------+
| *dsx*            | Set output on a channel. Works independent of channel range.                             |
|                  | <chan> = channel to update.                                                              |
|                  | Available channel options are: cha, chb, chc, chd.                                       |
|                  | <code> = 16-bit output code for the channel.                                             |
+------------------+------------------------------------------------------------------------------------------+
| *dse*            | Set the RSET of a channel.                                                               |
|                  | <chan> = channel to update.                                                              |
|                  | Available channel options are: cha, chb, chc, chd.                                       |
|                  | <opt> = RSET option.                                                                     |
|                  | Available options are: int and ext.                                                      |
+------------------+------------------------------------------------------------------------------------------+
| HART commands    |                                                                                          |
+------------------+------------------------------------------------------------------------------------------+
| *he*             | Enable HART channel.                                                                     |
+------------------+------------------------------------------------------------------------------------------+
| *hd*             | Disable HART channel.                                                                    |
+------------------+------------------------------------------------------------------------------------------+
| *hcc*            | Select wanted channel.                                                                   |
|                  | <*chan*> = Channel to be selected.                                                       |
+------------------+------------------------------------------------------------------------------------------+
| *ht*             | Transmit string through HART.                                                            |
|                  | <*string*> = string to be transmitted.                                                   |
+------------------+------------------------------------------------------------------------------------------+
| *hg*             | Send the received buffer through UART connection.                                        |
+------------------+------------------------------------------------------------------------------------------+
| *hcz*            | Send command zero with the specified number of FFs in the preambule.                     |
|                  | <*pbsize*> = size of the preambule (no. of 0xFFs in the beginning).                      |
+------------------+------------------------------------------------------------------------------------------+
| *hpt*            | Send a byte in a loop through HART to test the physical connection.                      |
|                  | <*byte*> = byte to send in loop.                                                         |
+------------------+------------------------------------------------------------------------------------------+
| EEPROM commands  |                                                                                          |
+------------------+------------------------------------------------------------------------------------------+
| *de*             | Discover EEPROM I2C addresses if there are any.                                          |
+------------------+------------------------------------------------------------------------------------------+

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0418_terminal_pic.png
   :alt: CN0418 application terminal example
   :align: center

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the CN0418.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that Analog Devices creates for testing and evaluation purposes. This is the EASIEST way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters and customize the software to fit your needs, but will be a bit more advanced and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0418** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0418 Hex File

   
   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0418.Hex <releases/download/Latest/ADuCM3029_demo_cn0418.hex>`
   
   Complete CN0418 Source Files
   
   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0418 Source Code <projects/ADuCM3029_demo_cn0418>`
   


How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to import existing projects into your workspace </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to configure the debug session </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>` section.

Project Structure
~~~~~~~~~~~~~~~~~

The program is composed of two main parts:

-  Board setup with initial values.
-  Main process.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0418_main_flowchart.png
   :alt: CN0418 application flow chart
   :align: center

Board setup initializes UART, SPI and I2C communication and verifies if there is an active EVAL-CN0418-ARDZ board connected by reading the main control register to memorize the value then trying to write and read that register to see if there is any device present that communicates through SPI the same way as the AD5755 and has the same register. If the AD5755's presence is confirmed this way the register is reset to the initial value and the application continues.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0418_board_setup_flow.png
   :alt: CN0418 board setup flow
   :align: center

After initialization, the application enters a loop where it memorizes UART characters as they come from the CLI. If an ENTER character is detected the application determines if a command has been called and executes it. The application also listens on the active HART channel and memorizes in a buffer any transmission received.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0418_process_flow.png
   :alt: CN0418 process flow
   :align: center

// End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0418_jumper_position.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0418_final_hw_setup.jpg
