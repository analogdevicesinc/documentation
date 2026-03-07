Mbed: User Guide for SDP-K1
===========================

Introduction
------------

| The SDP-K1 (EVAL-SDP-CK1Z board) is one of Analog Devices' Mbed enabled boards. Based on an STM32F469NI microcontroller, it allows users to easily develop drivers and example code for Analog Devices products and evaluation boards. The CMSIS-DAP hardware circuit and DAPLink firmware in the Freescale processor, allows SDP-K1 board to be easily programmed and debugged. The board has an Arduino header and 120-pin SDP connector making it compatible with many Analog Devices evaluation boards. 
| `Mbed <http://www.mbed.com>`_ is used by Analog Devices to develop and distribute drivers for Analog ICs. Mbed is an online IDE developed by ARM. It is open-source and supports controller boards with Cortex ARM core processors. These controller boards are developed by various companies including Analog Devices, ST Microcontroller, NXP, Renesas etc. Mbed allows for development using:

-  Online compiler: https://os.mbed.com/docs/mbed-os/v6.6/quick-start/build-with-the-online-compiler.html
-  Desktop IDE (recommended): https://os.mbed.com/studio/
-  Command line tool: https://os.mbed.com/docs/mbed-os/v6.6/quick-start/build-with-mbed-cli.html.

| The platform is available at no cost for customers and is easy to use. A major advantage to Mbed is that the example programs can be run on other Mbed enabled boards that customers are familiar with as long as it meets the hardware setup requirements. This allows for the evaluation of parts regardless of the controller board available.

SDP-K1 Board Features
~~~~~~~~~~~~~~~~~~~~~

-  Arduino Uno headers
-  120-pin SDP connector
-  High performance ARM® Cortex™-M4 Core (STM32F469NI)
-  180 MHz max CPU frequency, 384 KB SRAM, 2048 KB Flash
-  1.8V or 3.3V selectable IO voltage
-  480Mbps High-Speed USB 2.0 with USB-C connector (Device)
-  45MHz SPI at 3.3V & 22.5MHz at 1.8V
-  400KHz I2C
-  UART
-  Timers / PWM
-  12-bit ADC
-  GPIO
-  16MB SDRAM
-  3 traffic light LEDS (green, orange, red)
-  1 status LED

Board Components
~~~~~~~~~~~~~~~~

| |image1|
| |image2|

Quick Start Guide
-----------------

Each product with Mbed support comes with:

-  Library files or drivers for the product and,
-  A top level example program that provides a text based menu driven interface that demonstrates the library functions.

| All the code files will be shared on the code tab of Analog Devices Mbed web page https://os.mbed.com/teams/AnalogDevices/code/. Each project comes with a README.txt that explains how to use the code. This document is a user guide on how to use the code to evaluate products supported with Mbed code. It explains in more detail, the Mbed setup instructions written in the README.txt. The hardware setup instructions depends on the product and evaluation board used and will be explained in the README.txt.

Mbed Setup
~~~~~~~~~~

-  Go to Mbed web page https://www.mbed.com and click Log in/sign Up button on top right. Create an Mbed account or log in. Please note the username you are using. Open the online compiler by clicking the yellow button on the top right. This is what the compiler will look like:


|image3|

   \* Add SDP-K1 board to your compiler by going to https://os.mbed.com/platforms/SDP_K1/ and click on Add to your Mbed Compiler button on the bottom right.

   |image4|

   ==== Running Code on Mbed ====
-  On the product web page, find the link to Mbed example code, say EVAL-AD1234. Click Import Into Compiler. This should import the entire project, along with libraries.

|image5|

-  Click Compile. This should download a binary file, <<program_name>>.SDP_K1.bin. Find the file in your Downloads folder.
-  To program the SDP-K1 board, connect the SDP-K1 board to your computer using the USB cable provided. You should see the board as a new drive on your computer. Copy the binary file into the Mbed enabled board drive. You can also drag and drop the file, like a USB stick.  
-  Connect the evaluation board and follow the demo manual for the evaluation board to set up the board as required.
-  To communicate with the board, use your favorite Terminal program, like `Putty <https://putty.org>`_, `Tera Term <http://ttssh2.osdn.jp/>`_ etc. To use Putty, download and install Putty from `here <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_. Here are some `installation instructions <https://www.ssh.com/ssh/putty/windows/install>`_. Open Putty and select Serial connection type. Enter the serial port number and baud rate. Click Open.
   NOTE: You can find the serial port (which constantly changes, every time you plug a device in), by checking device manager.

   |image6|

Useful Links
------------

For further information on Mbed, developing and running code, and the SDP-K1 controller board, consult the following:

Mbed documentation: https://os.mbed.com/docs/mbed-os/v6.5/introduction/index.html

SDP-K1 Mbed page (includes pinouts and more detailed description of using the SDP-K1 in Mbed): https://os.mbed.com/platforms/SDP_K1/

Mbed supported ADI parts: :doc:`/wiki-migration/resources/tools-software/mbed-list`

Purchase SDP-K1: http://www.analog.com/SDP-K1

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sdpk1-e-top.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/mbed/board_components_sdp_6.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/mbed/mbed_compiler.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/mbed/add_to_compiler.png
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/mbed/import_to_compiler.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/mbed/putty.png
   :width: 400px
