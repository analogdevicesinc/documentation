Hardware Setup
==============

.. important::

   Before connecting the ADI evaluation board to the Xilinx KC705 make sure that the VADJ_FPGA voltage of the KC705 is set to 3.3V. For more details on how to change the setting for VADJ_FPGA visit the Xilinx KC705 product page.


-  Use the FMC-SDP interposer to connect the ADI evaluation board to the Xilinx KC705 board on the FMC LPC connector.
-  Connect the JTAG and UART cables to the KC705 and power up the FPGA board.
-  Start IMPACT, and double click “\ *Boundary Scan*\ ”. Right click and select *Initialize Chain*. The program should recognize the Kintex 7 device (see screenshot below).

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/impact_config.png
   :alt: impact_config.png
   :align: center
   :width: 300px

-  Program the KC705 FPGA using the "*Bit/download.bit*" file provided in the reference design archive.
-  Power the ADI evaluation board.

Configure Tera Term
===================

Launch **Tera Term** from the **Start -> All Programs -> Tera Term Pro -> Tera Term Pro**

Select **Setup -> Serial port...** and set the baud rate to 115200.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/teraterm_baud.png
   :alt: teraterm_baud.png
   :align: center
   :width: 400px

Select **Setup -> Terminal..** and enable **Local Echo**.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/teraterm_setup.png
   :alt: teraterm_setup.png
   :align: center
   :width: 400px

Upload Application Software
===========================

After the configuration of the terminal was finished, the software application has to be uploaded and started on the configured system. This can be done by running the *Loadapp.bat* batch script, which can be found in the **LoadApp** directory.

.. tip::

   If the script threw an error, verify if the Xilinx EDK path specified in the **Loadapp.bat** script is corresponding with the current install path. If not change it to the correct one.

