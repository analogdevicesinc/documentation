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

At this point everything is set up and it is possible to start the evaluation of the ADI hardware through the controls in the uC-Probe application provided in the reference design.

Configure uC-Probe
==================

Launch **uC-Probe** from the **Start -> All Programs -> Micrium -> uC-Probe**.

Select **uC-Probe** options.

-  Click on the **uC-Probe** icon on the top left portion of the screen.
-  Click on the **Options** button to open the dialog box.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/ucprobeoptionsbtn.png
   :alt: ucprobeoptionsbtn.png
   :align: center
   :width: 300px

Set target board communication protocol as **RS-232**

-  Click on the **Communication** tab icon on the top left portion of the dialog box
-  Select the **RS-232** option.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/ucprobe_comm.png
   :alt: ucprobe_comm.png
   :align: center
   :width: 300px

Setup **RS-232** communication settings

-  Select the **RS-232** option from the **Communication** tab.
-  Select the COM port to which the KC705 board is connected.
-  Set the Baud Rate to 115200 bps.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/interposer/ucprobe_rs232.png
   :alt: ucprobe_rs232.png
   :align: center
   :width: 300px

-  Press **Apply** and **OK** to exit the options menu.

Load and Run the Demonstration Project
======================================

-  Click the **Open** option from the **uC-Probe** menu and select the **.wsp** file from the **ucProbeInterface** folder provided within the reference design files.

-  Before opening the interface **uC-Probe** will ask for a symbols file that must be associated with the interface. Select the file **ucProbeInterface/ADIEvalBoard.elf** to be loaded as a symbol file.

-  Run the demonstration project by pressing the **Play** button.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image081.png
   :alt: image081.png
   :align: center
   :width: 200px

.. tip::

   
   -  In some cases it is possible that the uC-Probe interface will not respond to the commands the first time it is ran. In this situation just stop the interface by pressing the **Stop** button and run it again by pressing the **Play** button.
   -  After starting the uC-Probe interface wait until the status of the connection with the board displayed on the bottom of the screen is set to **Connected**. It is possible to use the interface only after the status is changed to **Connected** and the data transfer speed displayed next to the connection status is different than 0.
   

