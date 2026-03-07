Tutorial: Running MicroPython on the SHARC Audio Module Main Board
==================================================================

The fastest way of getting MicroPython to run on the board, is by flashing a pre-built MicroPython loader binary into the on-board SPI Flash and run the MicroPython from there.

.. important::

   This would overwrite anything that is previously stored in the SPI Flash. If you only want to run MicroPython in RAM without erasing the Flash, refer to :doc:`Tutorial: Building MicroPython with CrossCore Embedded Stuidio </wiki-migration/resources/tools-software/sharc-audio-module/micropython/building>`. You may use the debug function of CrossCore Embedded Studio to run MicroPython from RAM.


Obtain the pre-built binary
---------------------------

Currently, you may get the binary here:

:git-micropython:`releases`

Flash it into the SHARC Audio Module
------------------------------------

There are various ways of doing this. Here I am using the CLDP (Command Line Device Programmer) bundled with the CrossCore Embedded Studio and the Bare Metal SDK.

-  Download the binary loader file (micropython-xxxxxx.ldr, xxxxxx is the build date).
-  Open up a Command Prompt window and navigate to the directory where you put the loader file. (By using ``dir`` you should be able to see the loader file in the current directory.)
-  Connect a power supply and the ICE-1000 to the main board. Connect the ICE-1000 to your PC using the USB cable that ships with the ICE-1000.
-  Use the following command to flash it into the board (assuming you have CCES 2.8.1, Bare Metal SDK 2.0.0, and the board is connected to PC via a ICE-1000, and MicroPython built on Feb 27, 2019): ``"C:\Analog Devices\CrossCore Embedded Studio 2.8.1\cldp.exe" -verbose -proc ADSP-SC589 -core 1 -emu 1000 -driver "C:\Analog Devices\SAM_BareMetal_SDK-Rel2.0.0\extras\flash-programmer\Supporting_Files\w25ql512fv_dpia_SC589_SHARC_Core1.dxe" -cmd prog -erase affected -format bin -file micropython-190227.ldr``
-  You should see something similar to this, and saying ``done`` in the end. If not, double check and make sure the micropython binary is in the current directory, the path for CCES and Bare Metal SDK are correct. ``Target          Emulation Debug Target
   Platform        ADSP-SC589 via ICE-1000
   Processor       ADSP-SC589
   Core            1
   Driver          C:\Analog Devices\SAM_BareMetal_SDK-Rel2.0.0\extras\flash-programmer\Supporting_Files\w25ql512fv_dpia_SC589_SHARC_Core1.dxe
   Program         micropython-190227.ldr
   .................................................................................................................. done``

Connect to the board
--------------------

Now MicroPython has been flashed into the board, follow these steps to connect to the board:

-  Connect an FTDI USB-serial cable to the board, and plug the USB into the PC.
-  You should be able to see a USB Serial Port device in the Device Manager, note the COM number.
-  Open up a serial terminal emulator such as PuTTY, connect to the COM port in the step above, use baud rate 115200.
-  Set JP1 on the board to 1-2 connected (SPI Boot)
-  Press the RESET button (SW2)
-  You should be able to see the Python console in the terminal window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/micropython/mpy.png

--------------

`Faust and the SHARC Audio Module#..micropython|MicroPython Overview#.peripherals|Using Hardware Peripherals <https://wiki.analog.com/_media/navigation SHARC Audio Module#..faust>`_
