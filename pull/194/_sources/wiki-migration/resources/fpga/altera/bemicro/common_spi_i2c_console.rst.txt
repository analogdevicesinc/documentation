The lab is delivered together with a set of design files that are used to evaluate the ADI part. The FPGA image that must be loaded into the BeMicroSDK FPGA is included in the design files. This section presents the components included in the FPGA image and also the procedure to load the image into the FPGA.

FPGA Components
===============

The following components are implemented in the FPGA design:

===================== ======= ===
Name                  Address IRQ
===================== ======= ===
CPU                   800     -
Main PLL              80      -
JTAG UART             90      0
EPCS FLASH CONTROLLER 1800    1
OnChip RAM            10000   -
LED GPIO              100     -
SPI_0_P0              2000    3
SPI_1_P0              2040    5
GPIO                  2080    -
CTRL GPIO             20A0    -
SPI_0_P1              0       4
SPI_1_P1              20      6
SYS ID                40      -
TIMER                 60      2
I2C_0                 C0      7
I2C_1                 E0      8
===================== ======= ===

Load the FPGA Image
===================

To load the FPGA image the following steps must be performed:

-  Plug in the **BeMicroSDK** Stick into a USB port
-  Start **Altera Quartus Web edition** and start the programmer by selecting the menu option **Tools->Programmer**
-  Select **Add File** and select the file **ADIEvalBoardLab/FPGA/SDP1_bemicro2.jic**
-  Check the **Program/Configure** box and press **Start**

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image020.jpg
   :alt: image020.jpg
   :align: center
   :width: 400px

After finishing, the image is permanently loaded to the configuration Flash and the system will start with a blinking LED after reset or power up.
