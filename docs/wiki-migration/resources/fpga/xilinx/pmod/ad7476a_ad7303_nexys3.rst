Quick Start Guide
=================

The bit file provided in the project \*.zip file combines the FPGA bit file and the SDK elf files. It may be used for a quick check on the system.

Required Hardware
-----------------

-  `Nexys™3 Spartan-6 FPGA Board (Digilent) <http://digilentinc.com/Products/Detail.cfm?NavPath=2,400,897&Prod=NEXYS3>`_
-  `Pmod-AD1 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-AD1>`_
-  `Pmod-DA1 (Digilent) <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-DA1>`_

Required Software
-----------------

-  Xilinx 13.2 Design Suite (contains ISE, XPS, SDK and ChipScope Pro).
-  `Digilent Adept Runtime <http://digilentinc.com/Products/Detail.cfm?NavPath=2,66,828&Prod=ADEPT2>`_.
-  `Digilent Plugin for Xilinx Tools <http://digilentinc.com/Products/Detail.cfm?NavPath=2,66,768&Prod=DIGILENT-PLUGIN>`_.

Running Demo (SDK) Program
--------------------------

|

.. tip::

   | If you are not familiar with Nexys3 and/or Xilix tools, please visit
   | http://digilentinc.com/Products/Detail.cfm?NavPath=2,400,897&Prod=NEXYS3 for details.


To begin, connect the PmodAD1 to JA1 connector of Nexys3 board, pins 1 to 6 (see image below) and the PmodDA1 to JB1 connector of Nexys3 board, pins 1 to 6. You can use an extension cable for ease of use. Connect the USB cables from the PC to the board.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/nexys3_pmods.jpg
   :alt: Connecting Pmods to Nexys3
   :align: center
   :width: 300px

Start IMPACT, and double click "Boundary Scan". Right click and select Initialize Chain. The program should recognize the Spartan 6 device (see screenshot below). Program the FPGA using the **download.bit** file provided in the project \*.zip archive, located in the "*sw*" folder (../ad7303_ad7476/sw/download.bit).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/PmodDA1Impact.jpg
   :alt: Programming FPGA in IMPACT
   :width: 300px

Start the ChipScope Pro Analyzer provided with the Xilinx ISE Design Suite 13.2 and load the project **Nexys3_ChipScope_Demo.cpj** located in the "*chipscope*" folder (../ad7303_ad7476/chipscope/Nexys3_ChipScope_Demo.cpj). Click the **Open Cable/Search JTAG Chain** button and afterwards double click **Bus Plot** and select **Repetitive Trigger Run Mode**. Click the **Apply Settings and Arm Trigger** button. On the main screen you will se the waveforms change once every 25 seconds, between Sine, Square, Sawtooth and Triangle waveforms. Each waveform has a period of 25ms. You can compare the waveform displayed in ChipScope Pro with the waveform displayed on an oscilloscope from the DAC output.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/chipscope_open_project5.jpg
   :alt: Viewing Waveforms in ChipScope Pro
   :width: 300px

.. important::

   
   -  Connecting the Pmod-AD1 and/or Pmod-DA1 to the Nexys3 Board using an extension cable provides ease of use.
   -  UART must be set to 57600 baudrate.
   -  The reference voltage for both the AD7476A and AD7303 is 3.3V (if using Nexys3 Board).
   -  A loopback cable is connected between the output of the AD7303 DAC (A1 out) and the input of the AD7476 ADC present on the PmodAD1 board (pin1 in = A0 in).
   


Downloads
=========

|

.. admonition:: Download
   :class: download

   | `Reference design source code <https://wiki.analog.com/_media/resources/fpga/xilinx/pmod/AD7303_AD7476.zip>`_

