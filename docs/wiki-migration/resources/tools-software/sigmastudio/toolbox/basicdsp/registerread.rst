Register Read
=============

:doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`


This module reads any user accessible register from the DSP and gives out in the output Pin.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/regread.png
   :align: center

Input Pins
----------

None

Output Pins
-----------

+---------------+------------------------------------+-------------------------------------+
| Name          | Format [int/dec] - [control/audio] | Function Description                |
+===============+====================================+=====================================+
| Pin 1: Output | int- control                       | Value read at the register address. |
+---------------+------------------------------------+-------------------------------------+

| 

Grow Algorithm
--------------

The module currently supports growth. Both the control and pins are grown for each growth. Add algorithm functionality is not supported. The figure below shows the module when grown for 5.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/readread2.png
   :align: center

Configurations
--------------

+------------------+---------------+-----------------+------------------------------+
| GUI Control Name | Default Value | Range           | Function Description         |
+==================+===============+=================+==============================+
| Register Address | 0xF000        | 0xF000 - 0xF890 | Register Address to be read. |
+------------------+---------------+-----------------+------------------------------+

**Note:** Address control will be repeated for each channels when grown. And address can be specified either in hexadecimal or decimal.

DSP Parameter Information
-------------------------

================ ======================== ====================
GUI Control Name Compiler Name            Function Description
================ ======================== ====================
Mute             RegisterReadAlg1address0 Register Address
================ ======================== ====================


| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name
-   Brown - Growth Number (Changes for each register address when grown)

Supported ICs
-------------

-  ADAU145x
