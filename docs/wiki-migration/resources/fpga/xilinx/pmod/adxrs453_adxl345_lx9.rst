Quick Start Guide
=================

The bit file provided in the project \*.zip file combines the FPGA bit file and the SDK elf files. It may be used for a quick check on the system.

Required Hardware
-----------------

-  `Spartan-6 LX9 Microboard (Avnet) <https://www.xilinx.com/products/boards-and-kits/AES-S6MB-LX9.htm>`__
-  `Pmod-ACL (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL>`__
-  `Pmod-GYRO2 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-GYRO2>`__

Required Software
-----------------

-  Xilinx 13.2 Design Suite (contains ISE, XPS, SDK and ChipScope Pro).
-  A UART terminal (Tera Term/Hyperterminal), Baud rate 57600.

Running Demo (SDK) Program
--------------------------

|

.. tip::

   | If you are not familiar with LX9 and/or Xilix tools, please visit
   | `AES-S6MB-LX9.htm <https://www.xilinx.com/products/boards-and-kits/AES-S6MB-LX9.htm>`__ for details.


To begin, connect the PmodGYRO2 to J5 connector of LX9 board, pins 7 to 12. You must use an extension cable or the `Pmod-TPH (Digilent) <http://digilentinc.com/Products/Detail.cfm?NavPath=2,401,549&Prod=PMOD-TPH>`__. Afterwards connect PmodACL to connector J4 of the LX9 Board (see image below).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/gyro2_acl_lx9.jpg
   :alt: Connecting Pmods to LX-9 MicroBoard
   :width: 300px

Start IMPACT, and double click "Boundary Scan". Right click and select Initialize Chain. The program should recognize the Spartan 6 device (see screenshot below). Program the FPGA using the **download.bit** file provided in the project \*.zip archive, located in the "*sw*" folder (../adxrs453_adxl345/sw/download.bit).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/PmodDA1Impact.jpg
   :alt: Programming FPGA in IMPACT
   :width: 300px

| Start a **Hyperterminal** program (Tera Term, puTTy, etc.), select the proper **COM Port** (look for the COM Port named Silicon Labs CP210x USB to UART Bridge in Windows Device Manager). Select **57600 Baud Rate** and **Odd Parity**. You should start seeing messeges in the Terminal Window, displayed on 4 columns, representing the rotation of the board in Degrees per Second, and the acceleration in g on each axis.
| |Messeges displayed in the terminal window|
| On the LX-9 MicroBoard D10 and D9 display the Tap/Double Tap status. If you tap the device once, D10 will turn on for a short period of time. If you double tap the device, D10 and D9 will both turn on at the same time.
|

.. important::

   
   -  Connecting the PmodGYRO2 must be done with an extension cable or a PmodTPH.
   -  Connecting the PmodACL to the board with an extension cable provides ease of use.
   -  UART must be set to 57600 baudrate.
   


Downloads
=========

|

.. admonition:: Download
   :class: download

   | `Reference design source code <https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/ADXRS453_ADXL345.zip>`__


.. |Messeges displayed in the terminal window| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/adxrs453_adxl345_hyper.jpg
   :width: 300px
