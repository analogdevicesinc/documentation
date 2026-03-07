Self Calibration Guide for ADALM1000 in ALICE 1.3
=================================================

Objective:
----------

This document serves as the Self Calibration section of the User’s Guide in the ALICE 1.3 Desktop software interface written for use with the ADALM1000 active learning kit hardware.

.. important::

   Note that Revision F of the M1k is calibrated in the Factory and does not need the user to perform any calibration. The purpose of this Document is codify the steps contained in the software and remains here for legacy Revision D of the M1k hardware.


Steps performed by ALICE Desktop Self Calibration:
--------------------------------------------------

ALICE Desktop can perform a self-calibration sequence. An accurate 2.5 V reference source such as the AD584 precision reverence from the ADALP2000 analog parts kit is used. Plug it into a solderless breadboard and connect as shown in figure 1. The AD584 is configured as a 2.5V reference by connecting pins 1 and 3 together. A more permanent suggestion is soldering the circuit onto a small piece of circuit board rather than using a solderless breadboard as shown in figure 2. Connect both input channels to the 2.5V output of the AD584 when directed to do so.

.. image:: https://wiki.analog.com/_media/university/tools/volt-meter-fig4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, AD584 2.5 V reference connections


.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/ad584-calibrator.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, AD584 2.5 V reference on a circuit board


First, the program asks if user wishes to reset internal calibration values to default. The program expects the default values to exist in a file named: calib_default.txt and will ask for file if it is not found in the local directory.

If a calibration file from a previous self calibration for this board exists the program will ask if you want to load the settings from the previous file.

Next the programs requests user to: Connect an External Voltage reference (AD584) to both CHA and CHB inputs.

With both AWGs in disabled Hi-Z mode, program takes average of 1000 samples ( for this and all subsequent measurements ).

Program checks if measured values for CHA and CHB are within 2.2V and 2.8V to make sure the external reference was attached. If it measures results outside this range it asks user to check connections and tries again. Program assumes external voltage is exactly 2.5 V but variable AD584act can be adjusted if actual value is known ( see section on customizing ALICE below ). Program uses measured values and variable AD584act to calculate channel gain factors to adjust all subsequent measurements.

Next the program requests user to : Disconnect everything from CHA and CHB pins.

Program sets the following switches, CHA 2.5 V switch to open, CHA GND switch to closed, CHB 2.5 V switch to open, CHB GND switch to closed. With the AWG mode set to disabled ( Hi-Z ) it then measures the input offset ( ground voltage ).

Program sets the following switches, CHA 2.5 V switch to closed, CHA GND switch to open, CHB 2.5 V switch to closed, CHB GND switch to open. With the AWG mode set to disabled ( Hi-Z ) it then measures the internal 2.5 V rail. This voltage is later used in calculating actual current in ( internal ) resistor.

Program sets all the switches to open. Sets both CHA and CHB to SVMI mode DC voltage of 0.0 V. It measures the actual output when forcing 0.0 V.

Program sets all the switches to open. Sets both CHA and CHB to SVMI mode DC voltage of 2.5 V. It measures the actual output when forcing 2.5 V.

Program sets the following switches, CHA 2.5 V switch to open, CHA GND switch to closed, CHB 2.5 V switch to open, CHB GND switch to closed. Sets both CHA and CHB to SVMI mode DC voltage of 5 V. It measures the current when forcing 5 V into the internal 50 ohm resistors ( connected to ground). Program uses measured voltage and current values and variable OnBoardRes ( set = 50.83 to allow for switch Ron but can be set by user, see section on customizing ALICE below ) to calculate actual current.

Program sets the following switches, CHA 2.5 V switch to closed, CHA GND switch to open, CHB 2.5 V switch to closed, CHB GND switch to open. Sets both CHA and CHB to SVMI mode DC voltage of 0 V. It measures the current when forcing 0 V into the internal 50 ohm resistors connected to internal 2.5V rail. Program uses measured voltage and current values and variable OnBoardRes ( set = 50.83 to allow for switch Ron ) to calculate actual current.

Program sets the following switches, CHA 2.5 V switch to closed, CHA GND switch to open, CHB 2.5 V switch to closed, CHB GND switch to open. Sets both CHA and CHB to SIMV mode DC current of 0.0 mA. It measures the current and voltage when forcing 0mA into the internal 50 ohm resistors connected to internal 2.5V rail. Program uses measured voltage and current values and variable OnBoardRes ( set = 50.83 to allow for switch Ron ) to calculate actual current.

Program sets the following switches, CHA 2.5 V switch to open, CHA GND switch to closed, CHB 2.5 V switch to open, CHB GND switch to closed. Sets both CHA and CHB to SIMV mode DC current of +100.0 mA. It measures the current and voltage when forcing +100mA into the internal 50 ohm resistors connected to ground rail. Program uses measured voltage and current values and variable OnBoardRes ( set = 50.83 to allow for switch Ron ) to calculate actual current.

Program sets the following switches, CHA 2.5 V switch to closed, CHA GND switch to open, CHB 2.5 V switch to closed, CHB GND switch to open. Sets both CHA and CHB to SIMV mode DC current of -45 mA. ( -45 is used because internal 2.5 V may actually be less than 2.5 V and resistor is greater than 50 so that voltage does not go below ground ). It measures the current and voltage when forcing -45mA into the internal 50 ohm resistors connected to internal 2.5V rail. Program uses measured voltage and current values and variable OnBoardRes ( set = 50.83 to allow for switch Ron ) to calculate actual current.

Program returns all switches to open.

Program calculates all needed calibration factors from measured data and writes out values to a calibration file named based on last 16 digits of board serial number.

Program throws up a message window: "Finish" , "Successfully measured cal factors! "

Program asks user if they wish to actually write new calibration settings to board.

Your ALM1000 is now calibrated.

Checking the Calibration
~~~~~~~~~~~~~~~~~~~~~~~~

The way to check the calibration results is to set both AWG channels to Sine shape with 0.25 Min and 4.75 Max values set in SVMI mode. Also under Mode set the termination to the 2.5 V rail to on. You should now see about -45 mA to +45 mA or 90 mA p-p in the current traces, a little less due to the Switch Ron. Then turn off the termination (Open) and connect a known 50 Ω resistor from the outputs to the 2.5 V pin. The current traces should now be much closer to 90 mA p-p.

You can then switch to SIMV mode with -45 Min and +45 Max settings. Again with the termination to 2.5V rail turned on you should get 90 mA p-p but the voltage traces will be slightly larger due to the Switch Ron. And again you can compare to an external accurate 50 Ω resistor.

If the p-p values are more than 1 mA off from what is expected you can try changing the OnBoardRes variable and recalibrating. This can be done by entering the following line in the Command Interface window:

global OnBoardRes; OnBoardRes = Your_new_value

What if I don't have an AD584
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you don't have access to an AD584 ( or other accurate 2.5 V reference ) but do have access to an accurate DMM with enough resolution to measure 2.5 volts with 4 decimal places you can do the following. Plug in the ADALM1000 to the USB port to power it on. Let it set for ideally 10 minutes to reach a constant operating temperature. With your DMM set to the optimal range measure the on board fixed 2.5V supply pin on the analog connector with respect to the GND pin. Write this value down ( ideally with 4 decimal places i.e. 2.XXXX ). Open the Command Interface screen and enter the following line to change the AD584act variable to the value you just measured:

global AD584act; AD584act = Your_new_value

Run the Self Calibration as usual. When asked to connect the AD584 reference, connect the 2.5V pin to both CH A and CH B inputs using a Y shaped jumper wire with 3 male pins on each end. Remove the wire jumpers when prompted to disconnect everything from CH A and CH B. The program will now calibrate based on the now accurately measured value for the on board 2.5 V rail.

**For Further Reading:**

**Return to the** :doc:`ALICE Main Page </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`\ **.**
