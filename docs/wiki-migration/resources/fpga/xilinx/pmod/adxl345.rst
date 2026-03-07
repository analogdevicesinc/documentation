ADXL345 Pmod Xilinx FPGA Reference Design
=========================================

Introduction
------------

The :adi:`ADXL345` is a small, thin, ultralow power, 3-axis accelerometer with high resolution (13-bit) measurement at up to ±16 g. Digital output data is formatted as 16-bit twos complement and is accessible through either a SPI (3- or 4-wire) or I2C digital interface. The ADXL345 is well suited for mobile device applications. It measures the static acceleration of gravity in tilt-sensing applications, as well as dynamic acceleration resulting from motion or shock. Its high resolution (3.9 mg/LSB) enables measurement of inclination changes less than 1.0°.

**HW Platform(s):**

-  `Spartan-6 LX9 Microboard (Avnet) <https://www.xilinx.com/products/boards-and-kits/AES-S6MB-LX9.htm>`_
-  `Nexys™3 Spartan-6 FPGA Board (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,400,897&Prod=NEXYS3>`_
-  `Avnet ZedBoard <http://www.em.avnet.com/en-us/design/drc/Pages/Zedboard.aspx>`_

Quick Start Guide
-----------------

The bit file provided in the project \*.zip file combines the FPGA bit file and the SDK elf files. It may be used for a quick check on the system. All you need is the hardware and a PC running a UART terminal and the programmer (IMPACT).

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Spartan-6 LX9 Microboard (Avnet) <https://www.xilinx.com/products/boards-and-kits/AES-S6MB-LX9.htm>`_
-  `Nexys™3 Spartan-6 FPGA Board (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,400,897&Prod=NEXYS3>`_
-  `Avnet ZedBoard <http://www.em.avnet.com/en-us/design/drc/Pages/Zedboard.aspx>`_
-  `PmodACL (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL>`_

Required Software
~~~~~~~~~~~~~~~~~

-  Xilinx ISE 14.4 (Programmer (IMPACT) is sufficient for the demo and is available on Webpack).
-  A UART terminal (Tera Term/Hyperterminal), Baud rate 115200 for the Avnet LX-9 Microboard and ZedBoard or 9600 for the Digilent Nexys™3 Board.

Running Demo (SDK) Program
~~~~~~~~~~~~~~~~~~~~~~~~~~

|

.. tip::

   If you are not familiar with LX9 and/or Xilix tools, please visit

   | `AES-S6MB-LX9.htm <https://www.xilinx.com/products/boards-and-kits/AES-S6MB-LX9.htm>`_ for details.
   | If you are not familiar with Nexys™3 and/or Xilix tools, please visit
   | http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,400,897&Prod=NEXYS3 for details.
   | If you are not familiar with ZedBoard and/or Xilix tools, please visit
   | http://www.em.avnet.com/en-us/design/drc/Pages/Zedboard.aspx for details.


Avnet LX9 MicroBoard Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract the project from the archive file (ADXL345\_<board_name>.zip) to the location you desire.

To begin, connect the PmodACL to J5 connector of LX9 board (see image below). You can use an extension cable for ease of use. Connect the USB cable from the PC to the USB-UART female connector of the board for the UART terminal. The board will be programmed through its USB male connector.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodACL.jpg
   :alt: PmodACL and LX-9
   :width: 200px

Digilent Nexys™3 Spartan-6 FPGA Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract the project from the archive file (ADXL345\_<board_name>.zip) to the location you desire.

To begin, connect the PmodACL to JA connector of NEXYS3 board (see image below). You can use an extension cable for ease of use. Connect the USB cables from the PC to the board, one for programming (Digilent USB device) and one for the UART terminal (FT232R USB UART).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl_nexys3.jpg
   :alt: PmodACL and Nexys™3
   :width: 200px

Avnet ZedBoard
~~~~~~~~~~~~~~

To begin, connect the PmodACL to JA1 connector of ZedBoard (see image below). You can use an extension cable for ease of use. Connect the USB cables from the PC to the board, one for programming (Digilent USB device) and one for the UART terminal (FT232R USB UART).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl_zed.jpg
   :alt: PmodACL and ZedBoard
   :width: 200px

FPGA Configuration for Nexys3 and LX-9 MicroBoard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start IMPACT, and double click "Boundary Scan". Right click and select Initialize Chain. The program should recognize the Spartan 6 device (see screenshot below). Start a UART terminal (set to appropiate baud rate) and then program the device using the bit file provided in the project \*.zip archive, located in the "sw" folder (../adxl345/sw/ADXL345.bit).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/PmodACLImpact.jpg
   :alt: Programming FPGA in IMPACT
   :width: 200px

FPGA Configuration for ZedBoard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the **download.bat** script from the "../bin" folder downloaded from the github (see the links in the download section of the wiki page). The script will automatically configure the ZYNQ SoC and download the \*.elf file afterwards.

.. tip::

   If the download script fails to run, modify the Xilinx Tools path in **download.bat** to match your Xilinx Installation path.


If programming was successful, the **Main Menu** will apear in your UART terminal, as seen in the picture below. There are 7 options. Pressing [e], [d], [a], [s], [r], [t] or [q] key will allow you to select the desired option. After the end of every option, all the possible options (the Menu) will be shown again, allowing the user to make a new choice.

| |Main Menu|
| **Enable Measurement** sets the ADXL345 into measurement mode. Any measurement that takes place from that moment on will be valid data.

| |Enable Measurement|
| **Disable Measurement** sets the ADXL345 into standby mode. Any measurement that takes place from that moment will not be valid data (usually 0).

| |Disable Measurement|
| **Display Acceleration** displays acceleration data on all 3 Axes.

| |Acceleration on all 3 Axes|
| **Select Measurement Range** allows choosing between 4 options: ±2g, ±4g, ±8g and ±16g. Desired measurement range is selected by pressing [1] to [4].

| |Selecting Measurement Range|
| **Change Acquisition Rate** allows choosing different Acquisition rates for the ADXL345. Desired option is selected by pressing [1] to [9].

| |Acquisition Rate|
| **Select Tap Interrupts** allows enabling or disabling tap interrupts. Desired option is selected by pressing [1] to [4]. If the tap option selected is [1] or [3], after a single tap, D2 (LX9) / LD0 (Nexys3 and ZedBoard) will be ON. If the tap option selected is [2] or [3], after two consecutive taps, D3 and D2 (LX9) / LD1 and LD0 (Nexys3 and ZedBoard) will both be on at the same time. If the tap option selected is [4], no LEDs will be ON after a single or double tap.

| |Select Tap Interrupts|
| **Stop any ongoing action** will stop any display of measurements and afterwards display the Main Menu.

| |Stop actions|

Using the reference design
--------------------------

Functional Description
~~~~~~~~~~~~~~~~~~~~~~

The reference design is a SPI interface used to communicate with the device. The software programs the ADXL345 internal registers, and afterwards reads desired data from the device and prints it via UART. Three Interrupt signals are used in the design: one coming from the ADXL345, one from the UART and a timer interrupt (used for single and double tap LED signaling).

|

.. important::


   ..

| \* Connecting the PmodACL to the boards using an extension cable provides ease of use.
   
   -  UART must be set to 115200 Baud Rate for the Avnet LX-9 Microboard and ZedBoard or 9600 Baud Rate for the Digilent Nexys™3 Board.
   
   |

   |


.. important::

   When using the ZedBoard reference design in order to develop your own software, please make sure that the following options are set in "system_config.h":

   
   .. code:: c
   
      // Select between PS7 or AXI Interface
      #define USE_PS7      1
      // SPI used in the design
      #define USE_SPI      1
      // I2C used in the design
      #define USE_I2C      0
      // Timer (+interrupts) used in the design
      #define USE_TIMER    1
      // External interrupts used in the design
      #define USE_EXTERNAL     1
      // GPIO used in the design
      #define USE_GPIO         1
   


Downloads
---------

|

.. admonition:: Download
   :class: download

   | \**Avnet LX-9 MicroBoard: **
     \*** `Reference design source code for Avnet LX9 MicroBoard. <https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/adxl345_lx9.zip>`_\ **
     **\ Digilent Nexys™3:**
     \*** `Reference design source code for Digilent Nexys™3 Spartan-6 FPGA Board. <https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/adxl345_nexys3.zip>`_\ **
     **\ Avnet ZedBoard:\*\*
   | \* :git-fpgahdl_xilinx:`XPS Project <cf_adv7511_zed>`
   | \* :git-no-OS:`PmodACL Driver Files <Pmods/PmodACL>`
   | \* :git-no-OS:`ZYNQ SoC Peripherals Driver Files <Pmods/Common/sw>`
   | \* :git-no-OS:`Programming Script <Pmods/PmodACL/bin>`
   |


.. container:: hide

   
   Linux Device Driver
   ===================
   
   Connect PmodACL to the JA1 connector of the ZedBoard (upper row of pins).
   
   Preparing the SD Card
   ---------------------
   
   In order to prepare the SD Card for booting Linux on the ZedBoard:
   
   -  Download the device tree: :git-no-OS:`PmodACL Linux devicetree <Pmods/PmodACL/dts>`
   -  Configure the kernel to include the driver for the ADXL345: :doc:`Compiling the ADXL345 driver into the kernel </wiki-migration/resources/tools-software/linux-drivers/input-misc/adxl345>`
   -  Follow the instructions on the following wiki page, but use the device tree downloaded on the previous step and the kernel configuration above
   
      -  :doc:`Linux with HDMI video output on the ZED and ZC702 </wiki-migration/resources/tools-software/linux-drivers/platforms/zynq>`. When following those instructions make sure to copy the devicetree file that was downloaded in step 1) to arch/arm/boot/dts/zynq-zed-adv7511-pmod-acl.dts before trying to build the zynq-zed-adv7511-pmod-acl.dtb file.
   
   Make sure you have an HDMI monitor connected to the ZedBoard, plug in the SD Card and power on the board. If everything is correct, the system should boot up. If you don't have an HDMI monitor, connect to the board via UART, Baud Rate 115200.
   
   There are 2 ways to test the driver.
   
   -  Using the terminal window
   -  Using a serial terminal
   
   Using the terminal window
   -------------------------
   
   Open a new terminal window by pressing **Ctrl+Alt+T**.
   
   Navigate to the location of the device and identify it using the following commands:
   
   ::
   
      cd /sys/bus/spi/devices/
      ls
      spi32765.0  spi32766.0
      cd spi32766.0
      cat modalias
      spi:adxl34x
   
   If the **cat name** command doesn't return **spi:adxl34x**, then change the spi:device, and check again.
   
   ::
   
      cd ..
      cd spi32765.0
      cat modalias
   
   To see the list of options that the ADXL345 driver provides, type:
   
   ::
   
      ls
      autosleep  disable  input     position  rate       uevent
      calibrate  driver   modalias  power     subsystem
   
   To calibrate the device, type:
   
   ::
   
      echo 1 > calibrate
      cat calibrate
      4,3,-218
   
   To read the position, type:
   
   ::
   
      cat position
      (1, 0, 1)
   
   .. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/adxl345_linaro_terminal.jpg
      :alt: ADXL345 Set Voltage from Terminal
      :width: 600px
   
   The commands written above can also be used if not using an HDMI monitor and a wireless keyboard, by using a serial terminal, and typing the commands after the system boot-up is complete.

   
   |ADXL345 Read Voltage from Serial Terminal|

More information
----------------

-  :ez:`ask questions about the FPGA reference design <community/fpga>`
-  Example questions:

|//ez.analog.com/community/feeds/allcontent/atom|

.. |Main Menu| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl_menu1.jpg
   :width: 600px
.. |Enable Measurement| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl_menu2.jpg
   :width: 600px
.. |Disable Measurement| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl_menu3.jpg
   :width: 600px
.. |Acceleration on all 3 Axes| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl_menu4.jpg
   :width: 600px
.. |Selecting Measurement Range| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl_menu5.jpg
   :width: 600px
.. |Acquisition Rate| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl_menu6.jpg
   :width: 600px
.. |Select Tap Interrupts| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl_menu7.jpg
   :width: 600px
.. |Stop actions| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl_menu1.jpg
   :width: 600px
.. |ADXL345 Read Voltage from Serial Terminal| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/adxl345_linux_serial.jpg
   :width: 600px
.. |//ez.analog.com/community/feeds/allcontent/atom| image:: https://wiki.analog.com/_media/rss>http///ez.analog.com/community/feeds/allcontent/atom
