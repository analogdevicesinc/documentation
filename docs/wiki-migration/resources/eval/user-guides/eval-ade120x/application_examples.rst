ADE1201 Example Application
===========================

This demo will use **EVAL-ADE1201EBZ** and **EVAL-SDP-K1** evaluation boards to demonstrate how the ADE1201 binary input device can be used to monitor the voltage of a substation battery bank. Also refer to application AN-XXXX for further details.

Overview
--------

This example project demonstrates how a host microprocessor can communicate with the ADE1201 via the SPI bus and how to calculate the register values for the ADE1201.

Measurement Requirements
------------------------

The following is a list of items required to carry out the measurement.

-  Hardware

   -  EVAL-ADE1202EBS
   -  EVAL-SDP-K1
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port
   -  Voltage source such as Keithley 2400 to simulate substation battery voltage

-  Software

   -  ADE120x_Demo Example Project on MBED
   -  Serial Terminal Program, Such as Putty or RealTerm

Setting up the Hardware
-----------------------

-  For this example only one ADE1201 device is used. Connect the EVAL-SDP-K1 to the EVAL-ADE1201EBZ as shown in the diagram below.
-  Connect the positive output of the Keithley to connector P0 pin 1 and connect the negative output of the Keithley to P0 pin 2.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ade120x/hardware_setup.jpg
   :align: center
   :width: 600px

ADE1201 Software
----------------

The ADE1201 software drivers were developed using the MBED platform.

This example simulates a a 250VDC nominal binary input powered from a substation battery. Typically, a substation battery system will be made up of multiple batteries connected in series and the voltage at charge can vary as much as 20%. The maximum charged voltage of the battery is 300VDC. The minimum charged voltage can be as low as 200V. The ADE1201 threshold registers are configured to warn the host MCU when the battery voltage is in certain ranges. For the purpose of this example, the voltages have been scaled by a factor of 1/10. The ADC PGA gain is set to 10 to emulate the real world application.

To edit and compile the source code:

-  Navigate to the `ADE120x MBED repository <https://os.mbed.com/teams/AnalogDevices/code/EVAL-ADE120x>`__
-  Click on Import into Compiler button to add the project to the MBED compiler app.
-  Ensure the SDP-K1 is the selected platform in the top right hand corner of the screen

|image1|

-  Open the main.cpp file to review the main program code.
-  Click the Compile button on the top toolbar. It may take a number of seconds for the program to compile. Once it is finished it will automatically download the binary file
-  To load the firmware to the SDP-K1 board simply drag and drop the file to the SDP-K1 virtual drive in Windows explorer.

Verifying Functionality
-----------------------

The measurement results are sent to the PC via UART. To establish a connection over UART, connect the Micro-USB cable to the PC and to the EVAL-SDP-K1 board. A terminal program such as RealTerm or Putty is required to display the results

Following is the UART configuration.

::

     Select COM Port
     Baud rate: 230400
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ade120x/sdp_k1_mbed.png
   :width: 600px
