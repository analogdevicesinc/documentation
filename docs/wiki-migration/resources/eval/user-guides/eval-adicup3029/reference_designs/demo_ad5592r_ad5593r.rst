AD5592/AD5593 PMOD Demo
=======================

The **ADuCM3029_demo_ad5592r_ad5593r** project provides a solution to control a configurable input/output system using the **EVAL-AD5592R-PMDZ** or the **EVAL-AD5593R-PMDZ** and the **EVAL-ADICUP3029**. Both boards use a minimalist 8-channel, 12-bit, configurable ADC/DAC/GPIO device with either a SPI interface for **EVAL-AD5592R-PMDZ** and I2C interface for **EVAL-AD5593R-PMDZ**. The boards are SPI and I2C, respectively, PMOD form factor.

General Description/Overview
----------------------------

The **ADuCM3029_demo_ad5592r_ad5593r** project uses the **EVAL-AD5592R-PMDZ** or **EVAL-AD5593R-PMDZ** to provide a low-cost alternatives to the full-featured product evaluation boards, with terminal block connections and no extra signal conditioning. The application makes full use of the configurable 8 channels capability of the AD5592R and AD5593R, as every channel can be individually set to be either ADC, DAC, input GPIO or output GPIO. This provides a compact and highly flexible solution to signal acquisition and output control.

The application is controlled by the user with a CLI implemented using the serial UART core in the ADuCM3029 controller. The CLI is displayed on a connected PC using a serial terminal connection.

The program is divided in 2 parts: the setup part in which the present module is discovered and the main process. |Main flow chart| To do the discovery routine in the setup stage, the application first initializes the board SPI driver and tries to do a write and a read to a register to see if any device responds. If there is no SPI the application does the same test for the I2C device. If no device is found the application returns with an error message displayed on the serial connection. If any of the devices is found the program displays the active device and continues to the main process loop. If both PMODs are connected at the same time the one with SPI will be activated. |image1| The main process loop starts with the mirror mode. This mode sets up 4 channels as input and the other 4 as output, and then mirrors the inputs on the outputs. For example, if input channel 0 is driven externally to 1V the corresponding output channel, channel 7, will be driven to 1V as well by the application. The channels are linked as follows:

-  Channel 0 (ADC) -> Channel 7 (DAC);
-  Channel 1 (ADC) -> Channel 6 (DAC);
-  Channel 2 (input GPIO) -> Channel 5 (output GPIO);
-  Channel 3 (input GPIO) -> Channel 4 (output GPIO).

More information about the CLI commands can be found :doc:`here </wiki-migration/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_ad5592r_ad5593r>`.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-AD5592R-PMDZ or EVAL-AD5593R-PMDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad5592r_ad5593r demo application <projects/ADuCM3029_demo_ad5592r_ad5593r>`
   -  CrossCore Embedded Studio (2.8.0 or higher)
   -  ADuCM302x DFP (3.2.0 or higher)
   -  ADICUP3029 BSP (1.1.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

-  Connect **EVAL-AD5592R-PMDZ** or **EVAL-AD5593R-PMDZ** board to the **EVAL-ADICUP3029** as seen in the pictures below: |AD5592R-PMDZ connect|


|AD5593R-PMDZ connect|

   EVAL-AD5593R-PMDZ conforms to Pmod spec 1.1.0. This is physically compatible with Pmod platforms conforming to earlier Pmod specifications, provided that the VCC, GND, SDA, SCL pins are aligned with the corresponding signals on the platform board, leaving INT and RESET disconnected as shown.
-  Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and connect it to a computer.

|PC connect|

   Refer to https://blog.digilentinc.com/announcing-the-digilent-pmod-interface-specification-1-1-0/ for details on the Pmod specification.

Configuring the Software
------------------------

The configuration parameters can be found in the **config.h** file.

**AD5593R_A0_STATE** - This define contains the logic state of the A0 pin of the AD5593R device. This pin factors in the device I2C address and is by default logic "0" so no change is necessary to the define. If the pin state is changed by moving the pull-down resistor to be a pull-up resistor, this define needs to be changed to logic "1" too for the program to work.

::

      #define AD5593R_A0_STATE 0

Outputting Data
---------------


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#serial_terminal_setup>`_


Available commands
~~~~~~~~~~~~~~~~~~

Typing **help** or **h** after initial calibration sequence will display the list of commands and their short versions. Bellow is the short command list:

+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command                    | Example   | Description                                                                                                                                                                                                                                                                                                                                                |
+============================+===========+============================================================================================================================================================================================================================================================================================================================================================+
| General commands           |           |                                                                                                                                                                                                                                                                                                                                                            |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *h*                        | h         | Display available commands.                                                                                                                                                                                                                                                                                                                                |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *stts*                     | stts      | Display parameters of the application.                                                                                                                                                                                                                                                                                                                     |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Single channel commands    |           |                                                                                                                                                                                                                                                                                                                                                            |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *ao* <*chan*> <*dac_code*> | ao 0 2000 | Set a channel as analog output (DAC channel) and set the output code.                                                                                                                                                                                                                                                                                      |
|                            |           | <*chan*> = channel to be set (0-7);                                                                                                                                                                                                                                                                                                                        |
|                            |           | <*dac_code*> = DAC code in decimal integer format (0-4095).                                                                                                                                                                                                                                                                                                |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *ai* <*chan*>              | ai 0      | Change the channel to analog input and read the ADC channel.                                                                                                                                                                                                                                                                                               |
|                            |           | <*chan*> = channel to be changed and read. (0-7).                                                                                                                                                                                                                                                                                                          |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *do* <*chan*> <*val*>      | do 7 1    | Change the channel to digital output and set it's state to HIGH or LOW.                                                                                                                                                                                                                                                                                    |
|                            |           | <*chan*> = channel to be changed (0-7).                                                                                                                                                                                                                                                                                                                    |
|                            |           | <*val*> = '0' or '1' for LOW or HIGH, respectively.                                                                                                                                                                                                                                                                                                        |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *di* <*chan*>              | di 5      | Change the channel to digital input and read it's state.                                                                                                                                                                                                                                                                                                   |
|                            |           | <*chan*> = channel to be changed and read. (0-7).                                                                                                                                                                                                                                                                                                          |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Mode commands              |           |                                                                                                                                                                                                                                                                                                                                                            |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *m*                        | m         | Start mirror mode. This mode sets 4 channels as input and 4 channels as output. Then the application reads the input channels and drives the corresponding output channel to the value read on the input channel. For example, if channel 0 reads 1V then the corresponding channel, channel 7, will output 1V. The channels are linked the following way: |
|                            |           | \* Channel 0 (ADC) → Channel 7 (DAC);                                                                                                                                                                                                                                                                                                                      |
|                            |           | \* Channel 1 (ADC) → Channel 6 (DAC);                                                                                                                                                                                                                                                                                                                      |
|                            |           | \* Channel 2 (input GPIO) → Channel 5 (output GPIO);                                                                                                                                                                                                                                                                                                       |
|                            |           | \* Channel 3 (input GPIO) → Channel 4 (output GPIO).                                                                                                                                                                                                                                                                                                       |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *t*                        | t         | Start production test mode. The following connections must be made:                                                                                                                                                                                                                                                                                        |
|                            |           | \* Channel 0 → Channel 7;                                                                                                                                                                                                                                                                                                                                  |
|                            |           | \* Channel 1 → Channel 6;                                                                                                                                                                                                                                                                                                                                  |
|                            |           | \* Channel 2 → Channel 5;                                                                                                                                                                                                                                                                                                                                  |
|                            |           | \* Channel 3 → Channel 4.                                                                                                                                                                                                                                                                                                                                  |
|                            |           | Test mode sets CH0:3 to DAC mode, CH4:7 to ADC mode. CH0:3 are set to 0.5V, 1V, 1.5V, 2V, and the voltages at CH4:7 are read back and compared to the expected value. A pass message is then displayed if all the values are read back correctly.                                                                                                          |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *ais* <*ch_no*>            | ais a     | Start streaming mode. This mode reads the selected ADC channel twice a second and outputs the data to the terminal.                                                                                                                                                                                                                                        |
|                            |           | <*chan*> = channel to be read (0-7) or all channels simultaneously (a).                                                                                                                                                                                                                                                                                    |
|                            |           | If the channel picked is not an ADC channel the terminal will show an appropriate message.                                                                                                                                                                                                                                                                 |
|                            |           | This command does not change the setting of the channels. The desired channels need to be set as ADC separately.                                                                                                                                                                                                                                           |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  For the "h", "stts", "m" and "t" commands press Enter without inserting any space afterwards.
-  For the "ao", "ai", "do" and "di" commands, to invoke in application instructions, write just the command without parameters, insert a space afterwards and press Enter.

| 
| |image2|

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the AD5592/AD5593 PMOD.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that Analog Devices creates for testing and evaluation purposes. This is the EASIEST way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters and customize the software to fit your needs, but will be a bit more advanced and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_ad5592r_ad5593r** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt AD5592/AD5593 PMOD Hex File

   
   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_ad5592r_ad5593r.Hex <releases/download/Latest/ADuCM3029_demo_ad5592r_ad5593r.hex>`
   
   Complete AD5592/AD5593 PMOD Source Files
   
   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_ad5592r_ad5593r Source Code <projects/ADuCM3029_demo_ad5592r_ad5593r>`
   


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

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad559xr_project_structure.png
   :align: center

Project structure includes:

-  AD559xR driver module with files: ad5592r-base.c, ad5592r-base.h, ad5592r.c, ad5592r.h, ad5593r.c, ad5593r.h;
-  Main file ADuCM3029_demo_aiodiopdmz.c
-  Application module with files: aio_dio_pdmz.c, aio_dio_pdmz.h;
-  CLI module with files: cli.c, cli.h;
-  Configuration file config.h
-  Communication and GPIO driver module with files: platform_drivers.c, platform_drivers.h;
-  Power core initialization module with files: power.c, power.h;
-  Timer and delay driver module with files: timer.c, timer.h.

// End of Document //

.. |Main flow chart| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0414_main_flowchart.png
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad55923r_discovery_routine.png
.. |AD5592R-PMDZ connect| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad5592r_adicup_connect-min.jpg
.. |AD5593R-PMDZ connect| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad5593r_adicup_connect-min.jpg
.. |PC connect| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad5593r_adicup_pc_connect-min.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad5593r_cli_example.png
