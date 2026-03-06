Register Read
=============

| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| \|\| This module reads any user accessible register from the DSP and gives out in the output Pin.

| 
| |image1|
| ===== Input Pins ===== None

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

| The module currently supports growth. Both the control and pins are grown for each growth. Add algorithm functionality is not supported. The figure below shows the module when grown for 5.
| |image2|
| ===== Configurations =====

+------------------+---------------+-----------------+------------------------------+
| GUI Control Name | Default Value | Range           | Function Description         |
+==================+===============+=================+==============================+
| Register Address | 0xF000        | 0xF000 - 0xF890 | Register Address to be read. |
+------------------+---------------+-----------------+------------------------------+

**Note:** Address control will be repeated for each channels when grown. And address can be specified either in hexadecimal or decimal.

DSP Parameter Information
-------------------------

+------------------+----------------------------------------------------------------------------------------------+----------------------+
| GUI Control Name | Compiler Name                                                                                | Function Description |
+==================+==============================================================================================+======================+
| Mute             | <fc #008000>RegisterReadAlg</fc><fc #ff0000>1</fc><fc #000080>address</fc><fc #800000>0</fc> | Register Address     |
+------------------+----------------------------------------------------------------------------------------------+----------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000> Brown</fc> - Growth Number (Changes for each register address when grown)

Supported ICs
-------------

-  ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/regread.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/readread2.png
