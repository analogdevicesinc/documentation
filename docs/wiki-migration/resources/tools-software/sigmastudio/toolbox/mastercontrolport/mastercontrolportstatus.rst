Master Control Port Status (ADAU145x)
=====================================

| :doc:`Click here to return to the Master Control Port page </wiki-migration/resources/tools-software/sigmastudio/toolbox/mastercontrolport>`
| |image1|
| The master control port Status block sends out the Master control port status in the output pins. Master control errors can be cleared by setting input pin to non-zero value.

Input Pins
----------

+----------------------------------------+------------------------------------+----------------------------------------------------+
| Name                                   | Format [int/dec] - [control/audio] | Function Description                               |
+========================================+====================================+====================================================+
| Pin 0: Master Control Port Error Clear | decimal - control                  | Any non -zero value in the input clears the error. |
+----------------------------------------+------------------------------------+----------------------------------------------------+

Output Pins
-----------

+-----------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------------+
| Name                              | Format [int/dec] - [control/audio] | Function Description                                                                                     |
+===================================+====================================+==========================================================================================================+
| Pin 0: Master Control Port Status | decimal - control                  | Outputs 1 while the Master control port is busy, otherwise outputs 0                                     |
+-----------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------------+
| Pin 1: Master Control Port Error  | decimal - control                  | It is a 2 bit value. Bit-0 is set if I2C error is encountered. Bit-1 is set when timeout error occurred. |
+-----------------------------------+------------------------------------+----------------------------------------------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/mastercontrolport/status.jpg
