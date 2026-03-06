Evaluation Board for the ADA4250 & ADA4230 Low Power Programmable-Gain Instrumentation Amplifiers
=================================================================================================

Features
--------

**Arduino form-factor enables rapid prototyping
Several Power Management options
Terminal blocks and test points provided for easy connection to test equipment
Multiple firmware options available to take advantage of all product features**

General Description
-------------------

The EV-ADA4250CP-ARDZ and EV-ADA4230CP-ARDZ are designed to aid in the evaluation of the ADA4250 (SPI) and ADA4230 (Pin-strap) low power programmable-gain instrumentation amplifiers

Initial Setup
-------------

.. image:: https://wiki.analog.com/_media/resources/eval/sdp-eval.jpg
   :align: right
   :width: 200px

-   Select the 3.3V power option on the SDP-K1 using the VIO Adjust header (right position for 3.3V)
-   Connect the EVAL-ADA4250CP-ARDZ daughter board to connectors P3, P4, P5, P6, and P7 of the SDP-K1 Board.
-   Connect the desired input signal to the IN+ and IN- test points or the corresponding terminal block sockets.
-   Plug in the USB cable from the PC to the SDP-K1 base board via the mini USB port (P2).
-   The SDP-K1 will appear as a standard USB drive on the PC. Drag and drop the **mbed-os-ADA4250.bin** file to the Microcontroller Disk. The Status LED on the SDP-K1 board will flash as the PC writes the file. Press the Reset button to reset the microcontroller and the application will begin to run.

Default Power and Reference Buffer Configuration
------------------------------------------------

| By default, the ADA4250 ships with the following configuration:
| |image1|

-  **S1 is the in USB position** (assuming the base board is being powered by USB). AVDD and IOVDD are shorted together and their supply is controlled by S2.
   \* **S2 is in the VIO position** (power to IOVDD and AVDD will come from the IO/IOREF pin of the Arduino header. When pairing with the SDP-K1 board, this will be selected by the VIO Adjust header).
-  **P3 and P16 are in the left position**, disabling the optional LDOs on board.
-  **P11 and P13 are installed**. This drives the REFIN pin to AVDD/2. See the Reference Buffer Section for more information.
-  **P7 is installed**. This connects AVDD to Pin 1 of the P8 terminal block.

Power Options
~~~~~~~~~~~~~

| There are several power options possible with the EVAL-ADA4250-ARDZ Eval board. S1 is the main power switch that controls what AVDD and IOVDD are connected to.
| |image2|

The silkscreen indicates each of the possible options:

-  **S1, USB Position:** Default position, Shorts AVDD and IOVDD together & connects them to the S2 switch with options to power the board with: VIO (1.8V or 3.3V for the SDP-K1, 5V for some Arduino boards – this is the microcontroller’s supply), 3.3V (3.3V pin on the Arduino header), or 5V (5V pin on the Arduino header).

   -  When using this option, the user should select whatever supply matches the microcontroller’s supply. Flexibility was given here in case the base board doesn’t regulate some supplies.
   -  The position of S2 does not matter for the WALL or EXT/WALL positions of S1.

-  **S1, WALL Position:** Connects IOVDD to the output of the IOVDD LDO and AVDD to the output of the AVDD LDO. The base board with the microcontroller must be plugged into the wall with a 7V-12V DC power supply to use this option as this sets the VIN voltage. P18 and P3 should both be in the “ON” position (to the right, labeled on the silkscreen) to enable the LDO. Figure below shows the LDOs in the default “OFF” position.


|image3|

   -  The default LDO output is 3.3V and is set by resistors R20 and R21 for the IOVDD LDO and R17 and R18 for the AVDD LDO.
   -  To change supplies, swap R20 and R17 with: 1.24MΩ for 1.8V supply, 2.8MΩ for 3.3V supply (default), or 4.53MΩ for a 5V supply.

-  **S1, EXT/WALL Position:** Disconnects AVDD and IOVDD so that they can be driven separately at the test points:

   -  Again, be sure that AVDD>=IOVDD and IOVDD=Base board microcontroller supply.
   -  There is an option to install R29 and R30 with 0Ω resistors to short both AVDD and IOVDD to the AVDD LDO.

-  In any of the possible configurations, be sure that AVDD>=IOVDD and IOVDD=Base board microcontroller supply.
-  AVSS and IOVSS are shorted & connected to AGND by default (accessible by and GND test point or the VSS test point)
-  If using the microcontroller’s internal ADC, note that AREF is connected to the VIO/IOREF supply to ensure no damage to the microcontroller. If AVDD >IOVDD (Ex. AVDD = 5V and IOVDD = 3.3V) and the full output range of the ADA4250 will be used, R9 and R10 can be installed on the EVALADA4250- ARDZ to divide down the output within the AREF/IOVDD range.

Reference Buffer
~~~~~~~~~~~~~~~~

There is an on-board 10MΩ voltage divider to divide the AVDD supply down by 2 and apply this voltage to the input of the ADA4250’s reference buffer on pin REFIN. The reference buffer is not enabled by default but can be done using menu option 2 in the mbed-os-ADA4250 program. If the user does not wish to use the provided voltage divider and supply their own voltage, they may:

-  Disconnect P11 and P13 and apply a voltage within the specified range directly to REFOUT (ensuring the reference buffer has not already been enabled).
-  Disconnect P11 and P13 and apply a voltage within the specified range to the REFIN pin and enable the reference buffer within the program.

Input Signal
------------

| The inputs of the ADA4250 Evaluation Board are terminal block sockets or connected in test points. The user can connect AC or DC signals in the connectors.
| |image4|

.. _input-signal-1:

Input Signal
~~~~~~~~~~~~

Here are suggested input levels and offset voltage for ADA4250 evaluation using the transfer function: |image5| << insert table >>

ADA4250 Evaluation GUI
----------------------

.. image:: https://wiki.analog.com/_media/resources/eval/ada4250_gui.png
   :align: center
   :width: 600px

Software Operation
------------------

Port Select
~~~~~~~~~~~

In the upper left part of the evaluation program, click ‘Refresh Port List’ and in the drop-down menu, select a COM port (found in Device Manager) where your SDP-K1 is connected.


|image6|

Gain Selection and Mode
~~~~~~~~~~~~~~~~~~~~~~~

|image7| At startup, the default option is G=1. Once an option is selected, the gain selection will be executed after a few seconds. Check the led indicator of the SDP to see if the software is still executing.

|image8| By default, BW mode is low (typical gain-bandwidth product), SLP mode is disabled, and SDN is disabled. Select your desired mode in the drop-down menu. **High BW** mode will extend the bandwidth for higher gains (See the ADA4250 spec table for typical values). **Sleep (SLP) mode** disables the amplifier but retains the register settings. **Shutdown (SDN) mode** disables the amplifier and clears the register settings, restoring them to their default state.

.. _reference-buffer-1:

Reference Buffer
~~~~~~~~~~~~~~~~

There is an on-board 10MΩ voltage divider to divide the AVDD supply down by 2 and apply this voltage to the input of the ADA4250’s reference buffer on pin REFIN. By default, the reference buffer is disabled on power up. The EVAL-ADA4250-ARDZ is configured to use the on-board voltage divider to drive REFIN and set REFOUT to AVDD/2, so it is recommended to enable this once the program has started unless using an external reference supply. |image9| If the user does not wish to use the provided voltage divider and supply their own voltage, they may:

-  Disconnect P11 and P13 and apply a voltage within the specified range directly to REFOUT (ensuring the reference buffer has not already been enabled).
-  Disconnect P11 and P13 and apply a voltage within the specified range to the REFIN pin and enable the reference buffer within the program.

Sensor Offset Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~

| |image10| This configures the settings for the sensor offset calibration by first setting the range, followed by the bias, and the offset value to be calibrated. |image11| The default range setting is Range 1. The maximum offset that can be trimmed increases as the range increases and as the gain is reduced. |image12| The bias is disabled by default. Selecting the Bandgap Reference bias will allow the sensor calibration options shown in Table 1 below. Selecting the AVDD bias option will scale the offset calibration based on the AVDD supply, as shown in Table 2. Note that the Bandgap Reference Bias will approximately match AVDD bias when AVDD is 5V. |image13| Now that the sensor offset calibration settings are selected, the selections will be displayed, and the user will be prompted to enter in the number of LSBs of offset that they want to calibrate. Enter a value from 0-127. If the entered value is more than 127, this will cause error to the software and the software and hardware should be set to reset. |image14| Finally, the user will need to select whether they want a positive or negative offset. If the user wants to keep the range and bias settings, but just change the offset calibration value, this option can be used. After making this final selection, the calibration is complete.
| Table 1. Approximate Sensor Offset Calibration Range with Bandgap Reference Bias |image15|

Table 2. : Approximate Sensor Offset Calibration Range with AVDD Bias


|image16|

Read Register
~~~~~~~~~~~~~

This option lets the user read from any of the available registers and prints the hex value contents to the terminal.


|image17|

Sampling the ADA4250 Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The onboard ADC can be used to sample the ADA4250 output. The program will prompt the user for the number of samples they want to take, and then prompt for the desired sampling frequency. |image18| (In+ 1.7Vppac, 1.8Vos, In- 1Vdc) The samples (in Volts) will print out to the terminal and a waveform will be displayed. This software also has the feature to save its data to a csv file. Just click on the ‘Save CSV’ button and your data will be ready. If the user would need to sample another data, close the waveform window and sample again to avoid errors.


|image19|

Reset
~~~~~

|image20| The soft reset button clears the registers and restores them to its default value. The full system reset button performs a full reset on the part and microcontroller.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/board_view.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ada4250-power-options.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ada4250-ldo.png
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ada4250_input.png
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ada4250_tf.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ada4250_portselect.png
   :width: 200px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ada4250_gain.png
   :width: 200px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ada4250_mode.png
   :width: 200px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ada4250_refbuffer.png
   :width: 250px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/ada4250_calibset.png
   :width: 250px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/ada4250_read.png
   :width: 250px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/ada4250_sensorbias.png
   :width: 250px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/ada4250_offsetvalue.png
   :width: 250px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/ada4250_polarity.png
   :width: 250px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/ada4250_table1.png
   :width: 700px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/ada4250_table2.png
   :width: 700px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/ada4250_read.png
   :width: 250px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/ada4250_sampling.png
   :width: 250px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/ada4250_samplingwindow.png
   :width: 450px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/ada4250_reset.png
   :width: 250px
