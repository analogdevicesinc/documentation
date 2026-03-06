ADMP441 Pmod Xilinx FPGA Reference Design
=========================================

Introduction
------------

The :adi:`ADMP441` is a high performance, low power, digital output, omnidirectional MEMS microphone with a bottom port. The complete ADMP441 solution consists of a MEMS sensor, signal conditioning, an analog-to-digital converter, antialiasing filters, power management, and an industry standard 24-bit I²S interface. The I²S interface allows the ADMP441 to connect directly to digital processors, such as DSPs and microcontrollers, with-out the need for an audio codec in the system. The ADMP441 has a high SNR and high sensitivity, making it an excellent choice for far field applications. The ADMP441 has a flat wideband frequency response, resulting in natural sound with high intelligibility.

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
-  `PmodMIC2 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-MIC2>`__

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

Extract the project from the archive file (ADMP441_lx9.zip) to the location you desire.

To begin, connect the PmodMIC2 to J5 connector of LX9 board (see image below). You can use an extension cable for ease of use. Connect the USB cable from the PC to the USB-UART female connector of the board for the UART terminal. The board will be programmed through its USB male connector.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodMIC2_lx9.jpg
   :alt: PmodMIC2 and LX-9
   :width: 200px

Digilent Nexys™3 Spartan-6 FPGA Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract the project from the archive file (ADMP441_lx9.zip) to the location you desire.

To begin, connect the PmodMIC2 to JA connector of Nexys™3 board (see image below). You can use an extension cable for ease of use. Connect the USB cables from the PC to the board, one for programming (Digilent USB device) and one for the UART terminal (FT232R USB UART).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodMIC2_nexys3.jpg
   :alt: PmodMIC2 and Nexys™3
   :width: 200px

Avnet ZedBoard
~~~~~~~~~~~~~~

To begin, connect the PmodMIC2 to JD connector of ZedBoard (see image below). You can use an extension cable for ease of use. Connect the USB cables from the PC to the board, one for programming (Digilent USB device) and one for the UART terminal (FT232R USB UART).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodmic2_zed.jpg
   :alt: PmodMIC2 and ZedBoard
   :width: 400px

FPGA Configuration for Nexys3 and LX-9 MicroBoard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start IMPACT, and double click "Boundary Scan". Right click and select Initialize Chain. The program should recognize the Spartan 6 device (see screenshot below). Start a UART terminal (set to appropiate baud rate) and then program the device using the bit file provided in the project \*.zip archive, located in the "sw" folder (../admp441/sw/ADMP441.bit). Launch "data_capture.bat" from the "../DataCapture" folder.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/PmodMIC2Impact.jpg
   :alt: Programming FPGA in IMPACT
   :width: 200px

FPGA Configuration for ZedBoard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the **download.bat** script from the "../bin" folder downloaded from the github (see the links in the download section of the wiki page). The script will automatically configure the ZYNQ SoC and download the \*.elf file afterwards.

.. tip::

   If the download script fails to run, modify the Xilinx Tools path in **download.bat** to match your Xilinx Installation path.


If programming was successful, you should see messages in the UART terminal.

| |UART|
| |Data Capture|
|

.. important::


| For reasons NOT depending on Analog Devices, the JTAG connection through which the stored data on the LX-9/Nexys3 is transfered to the \*.wav file is very slow. The process takes about 2 hours.


Functional Description
~~~~~~~~~~~~~~~~~~~~~~

The reference design is a custom I2S interface used to communicate with the device. An interrupt signal is used to tell the user when new data has been read, an also if data was read when WS was low or high.

The ZedBoard design uses DMA to transfer data from the I2S Core to DDR.

|

.. important::


| \* Connecting the PmodMIC2 to the boards using an extension cable provides ease of use.
   
   -  UART must be set to 115200 Baud Rate for the Avnet LX-9 Microboard and ZedBoard or 9600 Baud Rate for the Digilent Nexys™3 Board.
   
   |

   |


Downloads
---------

|

.. admonition:: Download
   :class: download

   | \**Avnet LX-9 MicroBoard: **
     \*** `Reference design source code for Avnet LX9 MicroBoard. <https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/admp441_lx9.zip>`__\ **
     **\ Digilent Nexys™3:**
     \*** `Reference design source code for Digilent Nexys™3 Spartan-6 FPGA Board. <https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/admp441_nexys3.zip>`__\ **
     **\ Avnet ZedBoard:\*\*
   | \* :git-no-OS:`XPS Project <Pmods/PmodMIC2/cf_admp441_zed>`
   | \* :git-no-OS:`ADMP441 IPCore <Pmods/PmodMIC2/cf_lib/edk/pcores/axi_admp441_v1_00_a>`
   | \* :git-fpgahdl_xilinx:`Required Project Libraries <cf_lib>`
   | \* :git-no-OS:`PmodMIC2 Driver Files <Pmods/PmodMIC2>`
   | \* :git-no-OS:`Programming Script <Pmods/PmodMIC2/bin>`
   |


More information
----------------

-  :ez:`ask questions about the FPGA reference design <community/fpga>`
-  Example questions:

|//ez.analog.com/community/feeds/allcontent/atom|

.. |UART| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodmic2_menu1.jpg
   :width: 600px
.. |Data Capture| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/pmodmic2_menu2.jpg
   :width: 600px
.. |//ez.analog.com/community/feeds/allcontent/atom| image:: https://wiki.analog.com/_media/rss>http///ez.analog.com/community/feeds/allcontent/atom
