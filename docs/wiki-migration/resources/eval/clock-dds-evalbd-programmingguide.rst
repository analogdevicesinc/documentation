Programming Guide for Clock and DDS Evaluation Boards
=====================================================

This guide will help debug and program/reprogram clock and DDS evaluation boards with connection issues.

Unknown Device \\ No Boards Found
---------------------------------

There are many reasons why an evaluation board may not be found by the evaluation software.

Board or Setup Issues
~~~~~~~~~~~~~~~~~~~~~

The following list highlights the most common issues.

-  Jumpers are not installed or configured correctly.
   Always check the evaluation board user guide for the correct jumper settings.
-  Jumpers are not making a good connection.
   Sometimes jumpers on older boards do not make a good connection.
   Reseat the jumpers to restore connections.
-  Power connections are not at the correct voltages.
   Some evaluation boards require a connection to a benchtop power supply. Double check all power supply voltages for this type of evaluation boards.

Unprogrammed Board
~~~~~~~~~~~~~~~~~~

An evaluation board can loose it's identity, if the onboard EEPROM gets erased, when this happens Windows will no longer recognize the evaluation board. To get Windows to recognize the board, it will need to be programmed.

To identify an unprogrammed evaluation board.

-  Check for unknown devices in device manager.

Board Needs to be Reprogrammed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
