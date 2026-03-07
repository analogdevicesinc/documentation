DMA_EXAMPLE demo
================

DMA_EXAMPLE is a standard example that sends a sinewave on Tx channels using DMA from a lookup table. If you physically loopback a Tx channel to an Rx channel via an electrical wire, you may run the DMA_EXAMPLE and read the received data at Rx from particular memory address.

To build the DMA_EXAMPLE demo, edit the Makefile and add **-DDMA_EXAMPLE** to CFLAGS and rebuild. Alternatively, you may simply add a **#define DMA_EXAMPLE** in a suitable place in code and rebuild.

To run the DMA_EXAMPLE, you simply need to run the application as usual by:

-   making sure it was built with the **DMA_EXAMPLE** flag, as already mentioned
-   monitoring the serial terminal for messages printed by the application

The application will eventually print something like this:

::

   DMA_EXAMPLE: address=0x7f170 samples=65536 channels=4 bits=16

This means that the memory address where the data at Rx is stored is 0x7f170, there are in total 65536 samples, 16-bit wide across 4 channels, which is equivalent to 16384, 16-bit samples per channel.

At this point you may use a Tcl script to retrieve data from memory and store it into .csv files for processing. In the terminal where you built the project, run the following command while being in the no-OS/projects\ */project_name* folder

::

   for Zynq-7000:
   xsct ../../tools/scripts/platform/xilinx/capture.tcl ZYNQ_PS7 0x7f170 65536 4 16

   for ZynqMP:
   xsct ../../tools/scripts/platform/xilinx/capture.tcl ZYNQ_PSU 0x7f170 65536 4 16

   for Versal:
   xsct ../../tools/scripts/platform/xilinx/capture.tcl VERSAL 0x7f170 65536 4 16

After running the xsct command, some .csv files will be created in your directory. Now you need to run the Python script for plotting, specifying the number of channels you want to plot, like this:

::

   python3 ../../tools/scripts/platform/xilinx/plot.py 4

and a plot window will open showing the Rx channels.
