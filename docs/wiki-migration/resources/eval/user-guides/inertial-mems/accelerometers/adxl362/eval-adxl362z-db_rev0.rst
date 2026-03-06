ADXL362 Datalogger & Development Board: Rev 0
=============================================

|

.. important::

   Thanks for visiting!

   | This page has has instructions that apply to the **Rev 0** Datalogger Board.
   | If your board is labeled **REV 2** (on the back), please visit :doc:`this page </wiki-migration/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/eval-adxl362z-db>` instead.


Resources
---------

Kit Contents
~~~~~~~~~~~~

| 1 x ADXL362 Datalogger / Development Board
| 1 x MicroSD card with USB reader
| 1 x USB cable
| 1 x E-Ink electronic paper display
| 1 x Piece of double-sided foam tape

Not Included
~~~~~~~~~~~~

1 x CR2450 coin cell battery, required only if stand-alone operation is desired. Full functionality of the board is availabe using USB power.

Design and Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Schematics: | `PDF <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/eval-adxl362z-db_schematic.pdf>`__ |                                                                                                                                      |
+=============+=========================================================================================================================================+======================================================================================================================================+
| Layouts:    | `PDF <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/eval-adxl362z-db_layout.pdf>`__    | `CAM <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/eval-adxl362z-db_layout.zip>`__ |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

Programming Environment
~~~~~~~~~~~~~~~~~~~~~~~

| The firmware for the EVAL-ADXL362Z-DB was developed for the Renesas RL78/G13 microcontroller using the Renesas Electronics CubeSuite+ environment. The links below offer downloads and installation instructions for these tools:
| http://www.renesas.eu/products/tools/evaluation_software/downloads.jsp (Global site)
| https://www.renesas.com/us/en/design-support/software-and-tool (US site)

Getting Started
---------------

Using the Board
---------------

Firmware Options
~~~~~~~~~~~~~~~~

Analog Devices has developed firmware for implementing the following functions via the EVAL-ADXL362Z-DB:

-  **Datalogger and GUI (includes real-time data viewer and tilt sensor)**: logs data onto (supplied) microSD card. `ZIP <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362db_datalogger_and_gui.zip>`__ *(includes .hex firmware and .exe GUI)*
-  **Tilt Sensor**: shows tilt measurement on E-Ink display. `HEX <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362db_inclinometer.zip>`__ \| `Source Code <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362db_inclinometer_proj.zip>`__
-  **Ultralow Power Motion switch**: turns display icons on or off based on presence or absence of motion. `HEX <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362db_motionswitch.zip>`__ \| `Source Code <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adxl362db_motionswitch_proj.zip>`__
-  Pedometer & fall detector coming soon

Reconfiguring the Board
-----------------------

| The EVAL-ADXL362Z-DB firmware can be rewritten using the Renesas Flash Programmer (click `here <https://wiki.analog.com/>`__ for download links). Instructions for rewriting the firmware are as follows:
| \* Download the desired firmware .hex file from `here <https://wiki.analog.com/>`__. Save it in a known location.

-  Set jumpers: J6, J7, J8, and J9 (between the USB connector and the switch) to the 1-2 position. Set jumper J2 (near the display connector) to the 2-3 position for USB power.<WRAP>

.. container:: indent

   :!: *We know the jumpers are a pain and we apologize in advance.*\


========== ============ = = ========
**Jumper** **Position**

|image1|

J2         1            2 3 :::
J6         1            2 3 :::
J7         1            2 3 :::
J8         1            2 3 :::
J9         1            2 3 :::
========== ============ = = ========

</WRAP>

-  Plug the USB cable in to the computer and to the USB port on the board.
-  Launch the **Renesas Flash Programmer V1.03** (download `here <https://wiki.analog.com/>`__)
-  Choose "Create new workspace"
-  Input RL78/G13 in the Filter text box. Select the entry with Device Name "R5F100LJ", and enter a workspace name. Click Next.
-  In the "Select Communication Interface" screen, use the pull-down menu next to "Select Tool" to choose the appropriate COM port for the board. Click Next.
-  On the "Setting Power Supply" screen, leave the default settings and click Next.
-  On the "Setting Oscillator" screen, and select the corresponding COM port for the board. Click Next.
-  The "Information Settings" screen shows a summary of inputted settings. Click Complete.
-  The Workspace is now set up. Next to "User/Data area", browse to the desired .hex file (that you downloaded and saved in step **1.**)
-  Click “Start”.
-  When flashing is complete, disconnect the USB cable (to power the board off) and set jumpers J6 - J9 back to the 2-3 position. Leave J2 where it is to USB power, or move it to the 1-2 position to power the board from the coin cell. <WRAP>

========== ============ = = ========
**Jumper** **Position**

|image2|

J2         1            2 3 :::
J6         1            2 3 :::
J7         1            2 3 :::
J8         1            2 3 :::
J9         1            2 3 :::
========== ============ = = ========

</WRAP>

-  Reconnect the USB cable OR plug in the battery and turn on the switch to begin using the board.

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/board_front_jumpers_labeled.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/board_front_jumpers_labeled.png
   :width: 400px
