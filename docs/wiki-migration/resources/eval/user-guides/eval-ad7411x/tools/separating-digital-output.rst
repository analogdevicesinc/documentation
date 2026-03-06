Separating Digital Output from I/O Terminal
===========================================

Copyright, Disclaimer Statements

Copyright Information
---------------------

Copyright © 2022 Analog Devices, Inc. All Rights Reserved. This software is proprietary and confidential to Analog Devices, Inc. and its licensors. This document may not be reproduced in any form without prior, express written consent from Analog Devices, Inc.

Disclaimer
----------

Analog Devices, Inc. reserves the right to change this product without prior notice. Information furnished by Analog Devices is believed to be accurate and reliable. However, no responsibility is assumed by Analog Devices for its use; nor for any infringement of patents or other rights of third parties which may result from its use. No license is granted by implication or otherwise under the patent rights of Analog Devices, Inc.

Description
~~~~~~~~~~~

This Document explains how to modify the hardware and software setup to allow AD74115H to operate in Digital Output mode as well as Digital Input/Analog Input/Analog Output at the same time. Currently the AD74115H is set up with one pair of terminals which may be used for any of its modes of operation. With some minor modifications to the board and some simple writes to the register, it is possible to create a separate terminal set for the digital output functions and utilize it independently of the multiple other functions which operate through the original set of terminals.

Hardware Setup
~~~~~~~~~~~~~~

The only hardware required is the AD74115H evaluation board and the SDP_K1 board. Figures 1 and 2 below shows the hardware required to set up the device:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7411x/tools/ad74115h_evaluation_board.jpg
   :width: 600px

*Figure 1: AD74115H Evaluation Board*

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7411x/tools/sdpk1_board.jpg
   :width: 600px

*Figure 2: SDP_K1 Board*

The AD74115H Evaluation Board must then be connected to the SDP_K1 Board as demonstrated in Figure 3.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7411x/tools/ad74115h_evalboard_sdpk1board_stack.jpg
   :width: 600px

*Figure 3: Hardware Connected*

All required connections can now be made to the connected boards. A USB-C cable must be connected to the SDP_K1 board to power it. A power supply is required to be connected to the AD74115H Evaluation Board’s power terminal plug. To separate out the digital output functionality, P11 pin 3 and P13 pin 3 must be connected to one another. This connection acts as the new terminal for measuring the digital output of the device. Separate terminal plugs can then be connected to the I/O EXTx terminal plug-in order to utilise a separate board functionality, such as analogue output. Ensure that terminal polarities are not mismatched. Figure 4 shows the set up with all necessary connections made.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7411x/tools/ad74115h_do_separated.jpg

*Figure 4: All connections made to boards*

Configuration of AD74115H
~~~~~~~~~~~~~~~~~~~~~~~~~

In standard operation, the AD74115H performs all of its functionalities through the pre-existing I/O EXTx terminal plug. Therefore, it is programmed to only operate in one mode at a time. The following steps explain how to configure the AD74115H so that it may operate in Digital Output mode and one other mode at the same time (This guide uses Digital Output and Analogue Current Input as an example):

-  Device Reset: Toggle the RESETb pin for a second at the start-up
-  Clear the ALERT_STATUS register. Write 0x7FFF to the ALERT_STATUS register.
-  Blink the LED for 1s Toggle GPIOA so that the green LED on the evaluation board blinks. This is done as a diagnostic step to ensure that the GPIO peripherals and SPI is correctly configured and working.
-  Configuring the AD74115H

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7411x/tools/digitaloutput_register_table.png

The device is now capable of measuring an input current from an external current source connected to the I/O EXTx terminal plug as well as outputting a 24 V digital signal and the junction between P13 Pin3 and P11 Pin 3. The following script can be copied and pasted in order to set up the registers correctly:

WRITE 0x01 0x0005

WRITE 0x0B 0x0CCC

WRITE 0x08 0x6E01

WRITE 0x41 0xFFFF
