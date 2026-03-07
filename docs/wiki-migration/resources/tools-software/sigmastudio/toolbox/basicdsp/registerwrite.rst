Register Write
==============

| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| \|\| This module writes the value in the input pin to the DSP register address configured

| 
| |image1|
| ===== Input Pins =====

+--------------+------------------------------------+----------------------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description                         |
+==============+====================================+==============================================+
| Pin 1: Input | int- control                       | Value to be written to the register address. |
+--------------+------------------------------------+----------------------------------------------+

| 
| ===== Output Pins ===== None

Grow Algorithm
--------------

| The module currently supports growth. Both the control and pins are grown for each growth. Add algorithm functionality is not supported. The figure below shows the module when grown for 5.
| |image2|
| ===== Configurations =====

+------------------+---------------+-----------------+---------------------------------+
| GUI Control Name | Default Value | Range           | Function Description            |
+==================+===============+=================+=================================+
| Register Address | 0xF000        | 0xF000 - 0xF890 | Register Address to be written. |
+------------------+---------------+-----------------+---------------------------------+

**Note:** Address control will be repeated for each channels when grown. And address can be specified either in hexadecimal or decimal.

DSP Parameter Information
-------------------------

+------------------+-----------------------------------------------------------------------------------------------+----------------------+
| GUI Control Name | Compiler Name                                                                                 | Function Description |
+==================+===============================================================================================+======================+
| Mute             | <fc #008000>RegisterWriteAlg</fc><fc #ff0000>1</fc><fc #000080>address</fc><fc #800000>0</fc> | Register Address     |
+------------------+-----------------------------------------------------------------------------------------------+----------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000> Brown</fc> - Growth Number (Changes for each register address when grown)

Supported ICs
-------------

-  ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/regwrite1.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/regwrite2.png
