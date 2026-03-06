ADXL362 Pmod Xilinx FPGA Reference Design
=========================================

Introduction
------------

The :adi:`ADXL362` is an ultralow power, 3-axis MEMS accelerometer that consumes less than 2 μA at a 100 Hz output data rate and 270 nA when in motion triggered wake-up mode. Unlike accelerometers that use power duty cycling to achieve low power consumption, the ADXL362 does not alias input signals by undersampling; it samples the full bandwidth of the sensor at all data rates. The ADXL362 always provides 12-bit output resolution; 8-bit formatted data is also provided for more efficient single-byte transfers when a lower resolution is sufficient. Measurement ranges of ±2 g, ±4 g, and ±8 g are available, with a resolution of 1 mg/LSB on the ±2 g range. For applications where a noise level lower than the normal 550 μg/√Hz of the ADXL362 is desired, either of two lower noise modes (down to 175 μg/√Hz typical) can be selected at minimal increase in supply current.

**HW Platform(s):**

-  `Spartan-6 LX9 Microboard (Avnet) <https://www.xilinx.com/products/boards-and-kits/AES-S6MB-LX9.htm>`__
-  `Nexys™3 Spartan-6 FPGA Board (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,400,897&Prod=NEXYS3>`__
-  `Avnet ZedBoard <http://www.em.avnet.com/en-us/design/drc/Pages/Zedboard.aspx>`__

Quick Start Guide
-----------------

The bit file provided in the project \*.zip file combines the FPGA bit file and the SDK elf files. It may be used for a quick check on the system. All you need is the hardware and a PC running a UART terminal and the programmer (IMPACT).

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Spartan-6 LX9 Microboard (Avnet) <https://www.xilinx.com/products/boards-and-kits/AES-S6MB-LX9.htm>`__
-  `Nexys™3 Spartan-6 FPGA Board (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,400,897&Prod=NEXYS3>`__
-  `Avnet ZedBoard <http://www.em.avnet.com/en-us/design/drc/Pages/Zedboard.aspx>`__
-  `PmodACL2 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL2>`__

Required Software
~~~~~~~~~~~~~~~~~

-  Xilinx ISE 14.4 (Programmer (IMPACT) is sufficient for the demo and is available on Webpack).
-  A UART terminal (Tera Term/Hyperterminal), Baud rate 115200 for the Avnet LX-9 Microboard and ZedBoard or 9600 for the Digilent Nexys™3 Board.

Running Demo (SDK) Program
~~~~~~~~~~~~~~~~~~~~~~~~~~

|

.. tip::

   If you are not familiar with LX9 and/or Xilix tools, please visit

   | `AES-S6MB-LX9.htm <https://www.xilinx.com/products/boards-and-kits/AES-S6MB-LX9.htm>`__ for details.
   | If you are not familiar with Nexys™3 and/or Xilix tools, please visit
   | http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,400,897&Prod=NEXYS3 for details.
   | If you are not familiar with ZedBoard and/or Xilix tools, please visit
   | http://www.em.avnet.com/en-us/design/drc/Pages/Zedboard.aspx for details.


Avnet LX9 MicroBoard Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract the project from the archive file (ADXL362\_<board_name>.zip) to the location you desire.

To begin, connect the PmodACL2 to J5 connector of LX9 board (see image below). You can use an extension cable for ease of use. Connect the USB cable from the PC to the USB-UART female connector of the board for the UART terminal. The board will be programmed through its USB male connector.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodACL2.jpg
   :alt: PmodACL2 and LX-9
   :width: 200px

Digilent Nexys™3 Spartan-6 FPGA Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract the project from the archive file (ADXL362\_<board_name>.zip) to the location you desire.

To begin, connect the PmodACL2 to JA connector of NEXYS3 board (see image below). You can use an extension cable for ease of use. Connect the USB cables from the PC to the board, one for programming (Digilent USB device) and one for the UART terminal (FT232R USB UART).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_nexys3.jpg
   :alt: PmodACL2 and Nexys™3
   :width: 200px

Avnet ZedBoard
~~~~~~~~~~~~~~

To begin, connect the PmodACL2 to JA1 connector of ZedBoard (see image below). You can use an extension cable for ease of use. Connect the USB cables from the PC to the board, one for programming (Digilent USB device) and one for the UART terminal (FT232R USB UART).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_zed.jpg
   :alt: PmodACL2 and ZedBoard
   :width: 200px

FPGA Configuration for Nexys3 and LX-9 MicroBoard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start IMPACT, and double click "Boundary Scan". Right click and select Initialize Chain. The program should recognize the Spartan 6 device (see screenshot below). Start a UART terminal (set to appropiate baud rate) and then program the device using the bit file provided in the project \*.zip archive, located in the "sw" folder (../adxl362/sw/ADXL362.bit).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/PmodACL2Impact.jpg
   :alt: Programming FPGA in IMPACT
   :width: 200px

FPGA Configuration for ZedBoard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the **download.bat** script from the "../bin" folder downloaded from the github (see the links in the download section of the wiki page). The script will automatically configure the ZYNQ SoC and download the \*.elf file afterwards.

.. tip::

   If the download script fails to run, modify the Xilinx Tools path in **download.bat** to match your Xilinx Installation path.


If programming was successful, the Main Menu will apear in your UART terminal, as seen in the picture below. There are 9 options. Pressing [a], [x], [y], [z], [t], [r], [s], [i] or [m] key will allow you to select the desired option.

| |Main Menu|
| **Display acceleration on All Axes** will print the acceleration on X, Y and Z Axes, each on a separate row.

| |Acceleration on all 3 Axes|
| **Display acceleration on X Axis** will print the acceleration on X Axis, each new data read from the device will be displayed on a separate row.

| |Acceleration on X Axis|
| **Display acceleration on Y Axis** will print the acceleration on Y Axis, each new data read from the device will be displayed on a separate row.

| |Acceleration on Y Axis|
| **Display acceleration on Z Axis** will print the acceleration on Z Axis, each new data read from the device will be displayed on a separate row.

| |Acceleration on Z Axis|
| **Display temperature** will print the ADXL362 temperature in Celsius Degrees.

| |ADXL362 Temperature|
| **Select range** will allow setting the measurement range of the ADXL362. You can choose between ±2g, ±4g and ±8g. Selecting the desired range is done by pressing [1] to [3].

| |Selecting measurement range|
| **Switch resolution** option is used to choose reading data from 8 bit register or from 12 bit register.

| |Switching resolution|
| |image1|
| **Print device ID** will show information concerning the internal ID registers of ADXL362.

| |Printing ID Register|

Using the reference design
--------------------------

Functional Description
~~~~~~~~~~~~~~~~~~~~~~

The reference design is a SPI interface used to communicate with the device. The software programs the ADXL362s internal registers, and afterwards reads desired data from the device and prints it via UART.

|

.. important::


| \* Connecting the PmodACL2 to the boards using an extension cable provides ease of use.
   
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
      #define USE_TIMER    0
      // External interrupts used in the design
      #define USE_EXTERNAL     0
      // GPIO used in the design
      #define USE_GPIO         0
   


Downloads
---------

|

.. admonition:: Download
   :class: download

   | \**Avnet LX-9 MicroBoard: **
     \*** `Reference design source code for Avnet LX9 MicroBoard. <https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/adxl362_lx9.zip>`__\ **
     **\ Digilent Nexys™3:**
     \*** `Reference design source code for Digilent Nexys™3 Spartan-6 FPGA Board. <https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/adxl362_nexys3.zip>`__\ **
     **\ Avnet ZedBoard:\*\*
   | \* :git-fpgahdl_xilinx:`XPS Project <cf_adv7511_zed>`
   | \* :git-no-OS:`PmodACL2 Driver Files <Pmods/PmodACL2>`
   | \* :git-no-OS:`ZYNQ SoC Peripherals Driver Files <Pmods/Common/sw>`
   | \* :git-no-OS:`Programming Script <Pmods/PmodACL2/bin>`
   |


More information
----------------

-  :ez:`ask questions about the FPGA reference design <community/fpga>`
-  Example questions:

|//ez.analog.com/community/feeds/allcontent/atom|

.. |Main Menu| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_menu1.jpg
   :width: 600px
.. |Acceleration on all 3 Axes| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_menu2.jpg
   :width: 600px
.. |Acceleration on X Axis| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_menu3.jpg
   :width: 600px
.. |Acceleration on Y Axis| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_menu4.jpg
   :width: 600px
.. |Acceleration on Z Axis| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_menu5.jpg
   :width: 600px
.. |ADXL362 Temperature| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_menu6.jpg
   :width: 600px
.. |Selecting measurement range| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_menu7.jpg
   :width: 600px
.. |Switching resolution| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_menu8.jpg
   :width: 600px
.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_menu9.jpg
   :width: 600px
.. |Printing ID Register| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodacl2_menu10.jpg
   :width: 600px
.. |//ez.analog.com/community/feeds/allcontent/atom| image:: https://wiki.analog.com/_media/rss>http///ez.analog.com/community/feeds/allcontent/atom
