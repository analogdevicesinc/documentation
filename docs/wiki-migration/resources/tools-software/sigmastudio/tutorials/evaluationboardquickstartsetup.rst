Evaluation Board Quick Start Setup
==================================

| :doc:`Click here to return to the Tutorials section. </wiki-migration/resources/tools-software/sigmastudio/tutorials>`
| For detailed information regarding Evaluation Board configuration, refer to the evaluation board data sheets, available at www.analog.com/sigmadsp.

**AD1940/AD1941** The three AD 194x boards are almost identical. The EB1940 has switches; the MINIB 1940 does not. Both boards use SPI (serial-peripheral interface) communication, while the 1941 uses the I2C (also written I²C) communication protocol. Read through the first sets of steps below for global instructions, then continue past them to see differences with the mini and the 1941 boards.

**ADAU1701/ADAU1702** The ADAU1701 board provides for both analog and digital communication.

--------------------------------------------------------------------------------

*AD1940 (only) Evaluation Board Hardware Setup*, 6-channel Analog Input, Analog Output

(*For further help finding switches/jumpers on the board, or for other setup i/o configurations, see the* **EVAL-AD1941-AD1941EB_Datasheet** *on the SigmaStudio CD and the Evaluation Board Setup topic.)*

The switches and their settings:

| |evalsetuppic1.png|
| Any setting not listed may be considered unimportant (“don’t care”).

*Signal flow* Input will come from the six-channel analog inputs to AD1940 SDATA_IN0/1/2 and will output on whatever outputs (SDATA_OUTx) are designed in the software; defaults are SDATA_OUT0/1/2, or Analog Output 0-5. The AD1871 ADC is the master in this setup.

*Orientation*

-  With the eval board's power connector in the upper-left corner:
-  Input is connected to the stereo RCA connectors at the top of the board.
-  Output is connected to any of the 4 stereo or 8 RCA connectors at the right side of the board.
-  Signal path must be designed in Sigma Studio to send output to the desired port.

**AD1940 MINIB Evaluation Board Hardware Setup,** Stereo Analog Input, 6-Channel Analog Output

(To operate this board in standalone mode, connect the +6V power supply to the power connector, labeled J14.)

-  Attach the AD1940 MINIB board to the USB adapter board (J2 on both boards) and connect a USB cable between the USB board and the computer.
-  Connect your audio source to the 1/8” (mini) audio input jack (J1).
-  Connect your speakers or headphones to the1/8” audio output 1 jack (J4).
-  Set switch S2 to match the maximum level of your input source (either 1 or 2 Vrms).
-  Start SigmaStudio and follow steps 2-14 above.

--------------

**ADAU1701 Evaluation Board Setup** *Powering up the board*\ The board can be powered by either the USB connection or the included power supply. For the board to run independently from the computer, connect the power supply at J14 (colored red in the next figure). The power LED should be lit.

*Connecting the board to the computer*

-  Use the included USB cable to make a connection between the evaluation board and an available USB port on your computer. The USB jack is yellow in the next figure.
-  Windows should recognize the device, and Found New Hardware Wizard should display.
-  Select "Install from a list or specific location (Advanced)" and then "Search for the best driver in these locations." Ensure that "Search removable media" is unchecked and "Include this location in the search" is checked.
-  Browse to find the USB drivers folder. (By default, it should be at C:\\Program Files\\Analog Devices Inc\\Sigma Studio\\USB Drivers.) Click OK and Next to begin the installation. (Click Continue Anyway if you're prompted with "the software hasn’t passed Windows Logo testing.") Click Finish when done.

*Connecting the audio cables: Stereo analog inputs and outputs.*

-  Connect the audio source to the IN 0/1 jacks (blue in the below figure) on top of the board, using either RCA or 1/8” cables.
-  Connect the OUT 0/1 jacks (green below) to your speakers or headphones.

*Switch and jumper settings* To configure the board for stereo analog in and out, make sure the switches and jumpers are set as shown below.

.. image:: https://wiki.analog.com/_media/../gettingstarted/evalsetuppic2.png
   :alt: evalsetuppic2.png
   :align: center

.. |evalsetuppic1.png| image:: https://wiki.analog.com/_media/../gettingstarted/evalsetuppic1.png
