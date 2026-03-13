Register Write
==============

:doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

This module writes the value in the input pin to the DSP register address
configured

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/regwrite1.png
   :align: center

Input Pins
----------

+--------------+------------------------------------+----------------------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description                         |
+==============+====================================+==============================================+
| Pin 1: Input | int- control                       | Value to be written to the register address. |
+--------------+------------------------------------+----------------------------------------------+

| 
| ===== Output Pins ===== None

Grow Algorithm
--------------

The module currently supports growth. Both the control and pins are grown for
each growth. Add algorithm functionality is not supported. The figure below
shows the module when grown for 5.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/regwrite2.png
   :align: center

Configurations
--------------

+------------------+---------------+-----------------+---------------------------------+
| GUI Control Name | Default Value | Range           | Function Description            |
+==================+===============+=================+=================================+
| Register Address | 0xF000        | 0xF000 - 0xF890 | Register Address to be written. |
+------------------+---------------+-----------------+---------------------------------+

**Note:** Address control will be repeated for each channels when grown. And address can be specified either in hexadecimal or decimal.

DSP Parameter Information
-------------------------

================ ========================= ====================
GUI Control Name Compiler Name             Function Description
================ ========================= ====================
Mute             RegisterWriteAlg1address0 Register Address
================ ========================= ====================

| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name
-   Brown - Growth Number (Changes for each register address when grown)

Supported ICs
-------------

-  ADAU145x
