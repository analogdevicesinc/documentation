ADXL362 Datalogger & Development Board
======================================

|

.. important::

   Thanks for visiting!

   | This page is UNDER CONSTRUCTION.
   | If your board does not look like the one pictured below, you may have a Rev 0 board. Instructions for Rev 0 of the Datalogger Board have been moved :doc:`here </wiki-migration/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/eval-adxl362z-db_rev0>`.


Resources
---------

PDF User Guides
~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| `English <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/eval-adxl362z-db_full_user_guide.pdf>`__ | `Japanese <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/eval-adxl362z-db_jp.pdf>`__ |
+---------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

Kit Contents
~~~~~~~~~~~~

| 1 x ADXL362 Datalogger / Development Board
| 1 x MicroSD card with USB reader
| 1 x USB cable
| 1 x E-Ink electronic paper display
| 1 x Piece of double-sided foam tape

Not Included
^^^^^^^^^^^^

| 1 x CR2450 coin cell battery, required only if stand-alone operation is desired. Full functionality of the board is availabe using USB power.
| Multimeter or ammeter for measuring current consumption

System Requirements
~~~~~~~~~~~~~~~~~~~

| PC running Windows
| USB 2.0 Port

Design and Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Schematics: | `PDF <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362z-db_rev_2_schematic.pdf>`__ |                                                                                                                                       |
+=============+==========================================================================================================================================+=======================================================================================================================================+
| Layouts:    |                                                                                                                                          | `PDF <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362z-db_rev_2_layout.pdf>`__ |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

Drivers
~~~~~~~

| Download and install these drivers to connect the board to your PC, then follow these :doc:`written instructions </wiki-migration/resources/eval/user-guides/inertial-mems/evalsystem/installdrivers>` or :adi:`video instructions <static/imported-files/eval_boards/InstallDrivers.zip>` for installation.
| `32-bit <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/vcomusbdriver_v2040a_32bit.zip>`__ or `64-bit <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/vcomusbdriver_v2040a_64bit.zip>`__

Programming Environment
~~~~~~~~~~~~~~~~~~~~~~~

| The firmware for the EVAL-ADXL362Z-DB was developed for the Renesas RL78/G13 microcontroller using the Renesas Electronics CubeSuite+ environment. The links below offer downloads and installation instructions for these tools:
| http://www.renesas.eu/products/tools/evaluation_software/downloads.jsp (Global site)
| https://www.renesas.com/us/en/design-support/software-and-tool (US site)

Getting Started
===============

If this is your first time using this board, you will need to follow these steps to get started.

-  Assemble the board.
   <wrap>

| - Insert the EInk display in to the connector by lifting the brown tab on the connector, inserting the tail of the display, and pressing the brown tab back into place.
| - Optional: use the double-sided tape to fix the display in place. Stick the foam square to the board first, then gently press the display down onto the tape.
| </wrap>

-  Power the board.
   <wrap>

| - This board ships pre-programmed with the MultiDemo firmware that allows is to be used as a motion switch, data logger, or input to a real-time PC-connected user interface. The motion switch functionality can be used with the coin cell battery alone, without downloading any drivers or connecting to USB. Just insert a CR2450 coin cell batter in the holder on the back of the board, ensure all jumpers and switches are in the appropriate positions, and turn the board on. (this shows the back side of the board with the battery orientation - positive side of battery facing out\ |image1|)
| - To use the data logger or real-time evaluation functionality, you will need to install drivers and other files. Proceed to the next step for instructions.
| </wrap>

-  Install the drivers and verify COM port.
   - Download drivers `above <https://wiki.analog.com/>`__.
   - For instructions on verifying your COM port, click :doc:`here </wiki-migration/resources/eval/user-guides/inertial-mems/evalsystem/findyourcomport>`.

Using the Board
===============

Firmware Options
~~~~~~~~~~~~~~~~

Analog Devices has developed firmware for implementing the following functions via the EVAL-ADXL362Z-DB:

-  **Datalogger and GUI (includes real-time data viewer and tilt sensor)**: logs data onto (supplied) microSD card. *(includes .hex firmware and .exe GUI)*\ `eval-adxl362z-db <https://wiki.analog.com/ftp/ftp.analog.com/pub/imems_sensor_eval/eval-adxl362z-db>`__
-  **Tilt Sensor**: shows tilt measurement on E-Ink display. `HEX <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362db_inclinometer.zip>`__ \| `Source Code <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362db_inclinometer_proj.zip>`__
-  **Ultralow Power Motion switch**: turns display icons on or off based on presence or absence of motion. `HEX <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362db_motionswitch.zip>`__ \| `Source Code <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362db_motionswitch_proj.zip>`__
-  Pedometer & fall detector coming soon

Reconfiguring the Board
-----------------------

| The EVAL-ADXL362Z-DB firmware can be rewritten using the Renesas Flash Programmer (click `here <https://wiki.analog.com/>`__ for download links). Follow these instructions to flash a firmware ``.hex`` file to the board.
| \* If you haven't done so already, download the desired firmware ``.hex`` file from `here <https://wiki.analog.com/>`__, or create one of your own. Save it in a known location.

-  Set the programming switch to the PROG setting, as shown in the image below. (The setting of the ON/OFF switch is ignored when using USB power.) <WRAP>

|Front of board showing switch settings| </WRAP>

-  If a battery is plugged in to the board, remove it or ensure that jumper J2 is in the USB position.
-  Plug the USB cable in to the computer and to the USB port on the board.
-  Launch the **Renesas Flash Programmer V1.03** (download `here <https://wiki.analog.com/>`__). If you followed the default install configuration, the programmer will be under ``Start`` --> ``All Programs`` --> ``Renesas Electronics CubeSuite+`` --> ``Programming Tools`` --> ``Renesas Flash Programmer V1.03``.
-  Set up the programming environment in one of two ways:

   -  If you have programmed the board before, choose "Open latest workspace" and click Next. Skip to step 7.
   -  If this is your first time programming the board, or if the above does not work, follow these steps to set up the programming environment:

      -  Choose "Create new workspace"

         -  Input RL78/G13 in the Filter text box. Select the entry with Device Name "R5F100LJ", and enter a workspace name. Click Next.
         -  In the "Select Communication Interface" screen, use the pull-down menu next to "Select Tool" to choose the appropriate COM port for the board. Click Next.
         -  On the "Setting Power Supply" screen, leave the default settings and click Next.
         -  On the "Setting Oscillator" screen, and select the corresponding COM port for the board. Click Next.
         -  The "Information Settings" screen shows a summary of inputted settings. Click Complete. The Workspace is now set up.

-  Next to "User/Data area", browse to the desired ``.hex`` file (see step **1**.)
-  Click “Start”.
-  When flashing is complete, disconnect the USB cable (to power the board off) and set the programming switch back to the VIEW position. Leave J2 where it is for USB power, or move it to the 1-2 position for battery power.
-  Reconnect the USB cable OR plug in the battery and turn on the switch to begin using the board.

Firmware User Guides
====================

This section describes operation of the firmware options provided by Analog Devices for this development board. To download firmware, click `here <https://wiki.analog.com/>`__ or scroll up to the Firmware Options section above.

Multi-Demo Firmware
-------------------

The Multi-Demo firmware is pre-programmed onto the Datalogger Board, so out of the box, the behavior of the board will match the description in this section. This firmware may always be re-programmed onto the board using `these instructions <https://wiki.analog.com/>`__ and the .hex file posted `here <https://wiki.analog.com/>`__.

To use the MultiDemo firmware:

-  On power-up, the board behaves as a motion switch: the entire display lights up when the board is moved. When the board is still for a few seconds, most icons turn off and only the logos, power and battery icons remain on. Initial power up state: |image2| After movement, all of the logos, digits, power and battery icons will light:


|image3|

-  To log data, at any time, insert the microSD card into the slot and press the SW3 button in the top right-hand corner of the board. The word "LOg" will be shown on the display. The hand icon, if present, indicates a logging error. Generally this appears when the microSD card is not inserted fully into the slot. If no hand icon lights up, data logging begins when the word "LOg" is shown, and continues until power is removed from the board.
-  To download logged data onto a computer, use the GUI provided here. Installation of the GUI is straightforward:
-  The GUI also enables adjustment of output data rate and measurement range for data logging.

::

   * 

Motion Switch
-------------

This firmware implements a simple motion switch. When the board is moving, all of the display icons turn on. When the board is stationary for about 10 seconds, most icons turn off and only the power icon and the EInk and Analog Devices logos remain on.

The neat thing about this board is how little power it consumes. Between the low-power Renesas microcontroller, the e-paper display, and our ADXL362, the entire board design showcases low power.

.. tip::

   Can you tell us how much current consumption you measure, when the board is in motion and when it's not? Just edit the page and add your findings to the table!


======================== ================== ============
Current Consumption [µA]                    :::
======================== ================== ============
In Motion                Stationary         Measured by:
*Your measurement*       *Your measurement* *Your Name*
*Your measurement*       *Your measurement* *Your Name*
======================== ================== ============

Tilt Sensor
-----------

Gravity makes tilt sensing easy for an accelerometer. The earth's gravity exerts a 1\ *g* pull, by definition, on everything, toward the center of the earth (which, in general, would like a vector perpendicular to the floor). If the axis of acceleration sensitivity of an accelerometer is perfectly aligned with the gravity vector, then the accelerometer will "feel" a 1\ *g* acceleration. If the axis is at any angle away from that gravity vector, it will only feel a portion of that 1\ *g*. More accurately, it will feel an acceleration of 1\ *g*\ \*cos(angle).

The tilt sensor demo uses the 1\ *g*\ \*cos(angle) formula to convert measured acceleration to tilt angle, and then displays that angle on the e-paper display.

To begin using the tilt sensor, first load the firmware onto the board. Turn the board on (you can power the board using either USB or a coin cell), and place it on a flat surface, with the display facing up. The screen will display **CAL**, indicating that it is performing an offset calibration. Do not move the board during this time. When calibration is complete, the screen will display **0°**, and you can begin measuring tilt!

To measure tilt, stand the board up so that it is perpendicular to the floor (parallel to your computer monitor, probably) with the USB connector on the left. This is the 0° position, in which the sensitive axis is exactly perpendicular to the gravity vector, so none of the acceleration due to gravity is felt by the sensitive axis.

From this point, rotate the board clockwise and counter-clockwise, and watch the tilt measurement change.

Note that tilt measurement is, in general, a slow measurement. This is because at any given moment, the motion of your hand, for example, could be producing acceleration that would interfere with the tilt measurement. If we average the total acceleration measurement over time, we can get rid of the transient, or AC, effects, such as those due to your hand moving, and we are left only with long-term, or DC, effects -- in this case, gravity. So for best results, tilt slowly and wait for the display to refresh.

Write your own software
-----------------------

Talking to the development board can be done using your own program with the following commands:

Baud rate: 153600 8N1

Commands: 0xAA - Enable PC control, the board should respond (500+ ms) 0x55 and Eink display will show "PC"

0xB1 to start collecting data

::

     Start collection can be augmented with additional commands which specify different modes
        
     0xB1 0x0L 0x00 0xGS 0xN2
     Where L is the length: 1 for 8-bit; 0 for 12-bit
     G is the maximum G: 1 - 2G; 5 - 4G; 9 - 8G
     S is the sampling rate: 0-12.5hz;1-25hz;2-50hz;3-100hz;4-200hz;5-400hz
     N is the filtering: 0-Normal; 1-Low Noise; 2-Ultra low noise
     
     EG: 0xB1 0x00 0x00 0x15 0x02   would be start, 12-bit samples, 2G max, 400hz sampling, normal noise mode.    
     

0xB2 to end collecting data

Data is transmitted 16-bits for each direction, 2's compliment, little-endian, in groups of XYZ (48-bits at a time, or 6 bytes). The first block of data will be 8-bytes and can be discarded.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl326_battery.jpg
   :width: 300px
.. |Front of board showing switch settings| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362z-db_rev_2.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/poweridle.jpg
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/poweractive.jpg
   :width: 300px
